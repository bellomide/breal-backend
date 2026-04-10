from repository import database
from sqlalchemy import Column, String,Integer, null

class ClientProfile(database.Base):
    
    __tablename__ = "client"
    
    id: int = Column(Integer, primary_key=True,index=True, autoincrement=True)
    user_id:int = Column(Integer, index=True),
    full_name: str = Column(String, index=True, nullable=False)
    country: str = Column(String,index=True, nullable=False)
    phone: str = Column(String, index=True, nullable=False)
    preferred_currency: str = Column(String, index=True, nullable=False)
    
    class Config:
        orm_mode: True