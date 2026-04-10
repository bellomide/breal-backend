from repository import database
from sqlalchemy import Column, Integer, String
from enum import Enum

class ConsultationType(str,Enum):
    virtual = "VIRTUAL"


class ConsultationModel(database.Base):
    
    __tablename__ = "consultation"
    
    id: int = Column(Integer, primary_key=True,index=True, autoincrement=True)
    type: str = Column(String,index=True, nullable=False)
    scheduled_at: str = Column(String,index=True, nullable=False)
    project_stage: str = Column(String,index=True, nullable=False)
    site_location: str = Column(String,index=True, nullable=False)
    budget_range: str = Column(String,index=True, nullable=False)
    key_concerns: str = Column(String,index=True, nullable=False)
    client_email: str = Column(String,index=True,nullable=False)
    status: str = Column(String,index=True, nullable=False)
    
    class Config:
        orm_mode: True