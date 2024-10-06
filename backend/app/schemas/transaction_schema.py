from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema para crear una transacción
class TransactionCreate(BaseModel):
    client_id: str
    product_id: str
    amount: float
    type: str
    notification_method: str
    #date: Optional[datetime]

# Schema para devolver una transacción
class TransactionResponse(TransactionCreate):
    id: Optional[str]
    #date: Optional[datetime]
