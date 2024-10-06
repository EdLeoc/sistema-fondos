from app.models.Client import Client
from app.database import db
from app.models.Client import ClientUpdate

collection = db["clients"]

# Crear un nuevo cliente
async def create_client(client: Client):
    client_data = client.dict()
    result = await collection.insert_one(client_data)
    return str(result.inserted_id)

# Servicio para actualizar la información del cliente
async def update_client_info(client_id: str, client_data: ClientUpdate):
    result = await collection.update_one(
        {"id": client_id},
        {"$set": client_data.dict(exclude_unset=True)}
    )
    return result.modified_count > 0

# Obtener cliente por ID
async def get_client_by_id(client_id: str):
    client = await collection.find_one({"id": client_id})
    if client:
        return Client(**client)
    return None

# Obtener todos los clientes
async def get_all_clients():
    clients_cursor = await collection.find().to_list(length=100)
    return [Client(**client, id=str(client["_id"])) for client in clients_cursor]

# Actualizar balance del cliente
async def update_client_balance(client_id: str, new_balance: int):
    result = await collection.update_one({"id": client_id}, {"$set": {"balance": new_balance}})
    return result.modified_count > 0
