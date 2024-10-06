from app.models.Product import Product
from app.database import db

collection = db["products"]

# Crear un nuevo producto
async def create_product(product: Product):
    product_data = product.dict()
    result = await collection.insert_one(product_data)
    return str(result.inserted_id)

# Obtener producto por id
async def get_product_by_id(product_id: str):
    product = await collection.find_one({"id": product_id})
    if product:
        return Product(**product)
    return None

# Obtener todos los productos
async def get_all_products():
    products_cursor = await collection.find().to_list(length=100)
    return [Product(**product) for product in products_cursor]
