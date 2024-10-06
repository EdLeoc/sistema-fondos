# app/models/Product.py
from pydantic import BaseModel

class Product(BaseModel):
    id: str
    name: str
    min_amount: int
    category: str