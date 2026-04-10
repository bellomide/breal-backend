from pydantic import BaseModel
from enum import Enum

class PaymentStatus(str,Enum):
    pending = "PENDING"
    completed = "COMPLETED"   

class PaymentSchema(BaseModel):
    project_id: int
    amount: int
    
class VerifyPayment(BaseModel):
    reference: str