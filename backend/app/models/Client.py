# app/models/Client.py
from pydantic import BaseModel, EmailStr

class Client(BaseModel):
    id: str = None
    name: str
    last_name: str
    city: str
    email: str = None
    phone: str = None
    balance: int = 500000

class ClientUpdate(BaseModel):
    name: str
    last_name: str
    city: str
    email: EmailStr
    balance: float

    class Config:
        schema_extra = {
            "example": {
                "name": "John",
                "last_name": "Doe",
                "city": "New York",
                "email": "johndoe@example.com",
                "balance": 1000.0
            }
        }
