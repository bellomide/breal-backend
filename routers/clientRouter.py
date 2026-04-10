from email.policy import HTTP
from fastapi import status, Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from repository import database
from schema import clientSchema
from security import securityConfig
from service import clientService
from fastapi.security import HTTPAuthorizationCredentials
client_router = APIRouter()

@client_router.post('/clients/profile')
def create_client_profile(data: clientSchema.ClientProfileSchema, email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user), db: Session = Depends(database.get_db)):
    return clientService.create_client_profile(data,email,db)

@client_router.get('/clients/profile')
def fetch_client_profile(email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user), db: Session = Depends(database.get_db)):
    return clientService.get_client_profile(email,db)

@client_router.patch('/clients/profile')
def update_client_profile(data: clientSchema.UpdateClientProfileSchema,email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user), db: Session = Depends(database.get_db)):
    return clientService.update_client_profile(email,data,db)