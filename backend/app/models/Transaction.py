# app/models/Transaction.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Transaction(BaseModel):
    client_id: str
    product_id: str
    amount: float
    type: str
    notification_method: str
    #date: Optional[datetime] = None