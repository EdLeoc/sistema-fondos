from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema para crear un cliente
class ClientCreate(BaseModel):
    name: str
    last_name: str
    city: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    balance: int = 500000

# Schema para devolver un cliente (incluyendo id)
class ClientResponse(ClientCreate):
    id: str
