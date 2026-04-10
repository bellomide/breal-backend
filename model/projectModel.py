from repository import database
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
class ProjectModel(database.Base):
    
    __tablename__="project"
    
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: str = Column(String, index=True, nullable=False)
    client_id: int = Column(Integer, index=True)
    contractor_id: int = Column(Integer, index=True)
    status: str = Column(String, index=True,nullable=False)
    start_date: datetime = Column(DateTime,index=True, nullable=False)
    created_at: datetime = Column(DateTime,index=True, nullable=False)
    budget: str = Column(String,index=True, nullable=False),
    location: str = Column(String,index=True,nullable=False)
    class Config:
        orm_mode: True
    