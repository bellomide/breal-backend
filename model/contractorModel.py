from repository import database
from sqlalchemy import Column, Float, String, Integer

class ContractorModel(database.Base):
    
    __tablename__="contractor"
    
    id: int = Column(Integer, primary_key=True,index=True, autoincrement=True)
    first_name: str = Column(String, index=True, nullable=False)
    last_name: str = Column(String, index=True, nullable=False)
    nin: str = Column(String, index=True, nullable=False, unique=True)
    email: str = Column(String,index=True,nullable=False, unique=True)
    
    class Config:
        orm_mode: True
        
class ContractorProfile(database.Base):
    __tablename__ = "contractor_profile"
    id: int = Column(Integer, primary_key=True,index=True, autoincrement=True)
    user_id: int = Column(Integer, index=True)
    contractor_id: int = Column(Integer,index=True)
    company_name: str = Column(String,index=True,nullable=False)
    rating: float = Column(Float,index=True)
    approval_status: str = Column(String,index=True, nullable=False)
    years_experience: int = Column(Integer,index=True)
    
    class Config:
        orm_mode: True
        
        