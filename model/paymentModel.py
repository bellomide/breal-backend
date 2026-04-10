from repository import database
from sqlalchemy import Column, Integer, String
class PaymentModel(database.Base):
    
    __tablename__ = "payments"
    
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_id : int = Column(Integer, index=True)
    amount: int = Column(Integer, index=True)
    email: str = Column(String,index=True, nullable=False)
    referece: str = Column(String,index=True, nullable=False)
    access_code: str = Column(String,index=True, nullable=False)
    status: str = Column(String, index=True,nullable=False)
    class Config:
        orm_mode: True
    