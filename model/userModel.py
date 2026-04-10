from repository import database
from sqlalchemy import Column, String, Integer

class UserModel(database.Base):
    
    __tablename__="user"
    
    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email: str = Column(String, index=True, nullable=False)
    password: str = Column(String, index=True, nullable=False)
    role: str = Column(String, index=True, nullable=False)
    access_level: str = Column(String,index=True,nullable=False)
    
    class Config:
        orm_mode: True