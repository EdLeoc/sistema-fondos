from pydantic import BaseModel

# Schema para crear un producto
class ProductCreate(BaseModel):
    name: str
    min_amount: int
    category: str

# Schema para devolver un producto (incluyendo id)
class ProductResponse(ProductCreate):
    id: str
