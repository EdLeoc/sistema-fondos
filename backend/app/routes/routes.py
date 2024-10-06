from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from app.models.Client import ClientUpdate
from app.schemas.client_schema import ClientCreate, ClientResponse
from app.services.client_service import create_client, get_client_by_id, get_all_clients, update_client_info
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.services.product_service import create_product, get_product_by_id, get_all_products
from app.schemas.transaction_schema import TransactionCreate, TransactionResponse
from app.services.transaction_service import create_transaction, cancel_transaction, get_transactions_by_client, get_all_transactions

router = APIRouter()

# Rutas para Clients
@router.post("/clients", response_model=ClientResponse)
async def create_client_endpoint(client: ClientCreate):
    client_id = await create_client(client)
    return {**client.dict(), "id": client_id}

@router.put("/clients/{client_id}")
async def update_client(client_id: str, client_data: ClientUpdate):
    updated = await update_client_info(client_id, client_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"message": "Información actualizada correctamente"}

@router.get("/clients/{client_id}", response_model=ClientResponse)
async def get_client_by_id_endpoint(client_id: str):
    client = await get_client_by_id(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.get("/clients", response_model=list[ClientResponse])
async def get_all_clients_endpoint():
    return await get_all_clients()


# Rutas para Products
@router.post("/products", response_model=ProductResponse)
async def create_product_endpoint(product: ProductCreate):
    product_id = await create_product(product)
    return {**product.dict(), "id": product_id}

@router.get("/products/{product_id}", response_model=ProductResponse)
async def get_product_by_id_endpoint(product_id: str):
    product = await get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/products", response_model=list[ProductResponse])
async def get_all_products_endpoint():
    return await get_all_products()

# Rutas para Transactions
@router.get("/transactions", response_model=list[TransactionResponse])
async def get_all_transactions_endpoint():
    return await get_all_transactions()

@router.post("/transactions", response_model=TransactionResponse)
async def create_transaction_endpoint(transaction: TransactionCreate):
    transaction_id = await create_transaction(transaction)
    return {**transaction.dict(), "id": transaction_id}

class CancelTransactionRequest(BaseModel):
    transaction_id: str

@router.post("/transactions/cancel")
async def cancel_transaction_endpoint(request: CancelTransactionRequest):
    try:
        result = await cancel_transaction(request.transaction_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error en el servidor")