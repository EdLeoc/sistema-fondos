from app.config import settings
from aiosmtplib import send
from app.models.Transaction import Transaction
from app.schemas.transaction_schema import TransactionCreate, TransactionResponse
from app.database import db
from datetime import datetime
from bson import ObjectId
import aiosmtplib
from email.message import EmailMessage
from twilio.rest import Client
from aiosmtplib import send as send_email

transaction_collection = db["transactions"]
client_collection = db["clients"]

# Función para enviar notificaciones por correo electrónico
async def send_email_notification(email: str, transaction: TransactionCreate):
    message = EmailMessage()
    message["From"] = settings.MAIL_FROM
    message["To"] = email
    message["Subject"] = "Suscripción Exitosa"
    # Acceder a los atributos del objeto transaction usando notación de punto
    message.set_content(f"Te has suscrito exitosamente al fondo {transaction.product_id} por un valor de {transaction.amount}.")

    # Conexión y envío del correo
    await aiosmtplib.send(
        message,
        hostname=settings.MAIL_SERVER,
        port=settings.MAIL_PORT,
        start_tls=settings.MAIL_STARTTLS,
        username=settings.MAIL_USERNAME,
        password=settings.MAIL_PASSWORD,
    )

# Función para enviar notificaciones por SMS
async def send_sms_notification(phone: str, transaction: TransactionCreate):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"Suscripción exitosa al fondo {transaction.product_id} por un valor de {transaction.amount}.",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone
    )

# Crear una nueva transacción
async def create_transaction(transaction: Transaction):
    try:
        # Obtener los detalles del cliente basado en su client_id
        client = await client_collection.find_one({"id": transaction.client_id})

        if not client:
            raise ValueError("Cliente no encontrado")

        # Verificar si el cliente tiene suficiente saldo
        if client["balance"] < transaction.amount:
            raise ValueError("Saldo insuficiente para realizar la suscripción")

        # Registrar la transacción
        transaction_data = transaction.dict()
        result = await transaction_collection.insert_one(transaction_data)

        # Restar el monto de la suscripción del balance del cliente
        new_balance = client["balance"] - transaction.amount
        await client_collection.update_one(
            {"id": transaction.client_id},
            {"$set": {"balance": new_balance}}
        )

        # Aquí manejar el envío de notificación
        if transaction.notification_method == "email":
            await send_email_notification(client["email"], transaction)
        elif transaction.notification_method == "sms":
            await send_sms_notification(client["phone"], transaction)

        return str(result.inserted_id)

    except Exception as e:
        raise ValueError(str(e))

# Obtener todas las transacciones de un cliente
async def get_transactions_by_client(client_id: str):
    transactions_cursor = await transaction_collection.find({"client_id": client_id}).to_list(length=100)
    return [Transaction(**transaction) for transaction in transactions_cursor]

# Obtener todas las transacciones
async def get_all_transactions():
    transactions = []
    async for transaction in transaction_collection.find():
        transaction["_id"] = str(transaction["_id"])
        transaction["id"] = transaction["_id"]
        transactions.append(transaction)
    return transactions


async def cancel_transaction(transaction_id: str):
    try:
        # Buscar la transacción
        transaction = await transaction_collection.find_one({"_id": ObjectId(transaction_id)})
        if not transaction:
            raise ValueError("Transacción no encontrada")

        # Verificar si ya está cancelada
        if transaction.get("type") == "cancelation":
            raise ValueError("La transacción ya está cancelada")

        # Obtener el cliente relacionado
        client = await client_collection.find_one({"id": transaction["client_id"]})
        if not client:
            raise ValueError("Cliente no encontrado")

        # Sumar el monto al balance del cliente
        new_balance = client["balance"] + transaction["amount"]
        await client_collection.update_one(
            {"id": transaction["client_id"]},
            {"$set": {"balance": new_balance}}
        )

        # Actualizar el estado de la transacción
        await transaction_collection.update_one(
            {"_id": ObjectId(transaction_id)},
            {"$set": {"type": "cancelation"}}
        )

        return {"message": "Transacción cancelada con éxito", "new_balance": new_balance}

    except Exception as e:
        raise ValueError(str(e))