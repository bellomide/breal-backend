from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class UserRole(str,Enum):
    client = "CLIENT"
    contractor = "CONTRACTOR"
    admin = "ADMIN"


class UserSchema(BaseModel):
    email: str
    password: str
    role: UserRole
    

class UserLogin(BaseModel):
    email: str
    password: str
    
class UserData(BaseModel):
    id: int
    role: str
    access_level: str
    
class UserResponse(BaseModel):
    status: str
    data: UserData
    
class UserRefreshToken(BaseModel):
    email: str
    token: str
    
class UserToken(BaseModel):
    access_token: str
    access_token_expires_in: datetime
    refresh_token: str
    refresh_token_expires_in: datetime
    