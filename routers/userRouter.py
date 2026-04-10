from fastapi import APIRouter, Depends, status
from service import userService
from schema import userSchema
from repository import database
from sqlalchemy.orm import Session
from fastapi.security import HTTPAuthorizationCredentials
from security import securityConfig
user_router = APIRouter()

@user_router.post('/auth/register', response_model=userSchema.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user_account(data: userSchema.UserSchema, db: Session = Depends(database.get_db)):
    return userService.register_user(data,db)

@user_router.post('/auth/login', response_model=userSchema.UserToken, status_code=status.HTTP_200_OK)
def login_into_account(data: userSchema.UserLogin, db: Session = Depends(database.get_db)):
    return userService.login(data,db)


@user_router.get('/auth/me')
def get_user(email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user), db:Session = Depends(database.get_db)):
    return userService.get_user(email, userSchema.UserRole.client, db)


@user_router.patch('/users/{email}')
def update_user_by_email(data: userSchema.UserSchema, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return userService.update_user(email,data,db)

@user_router.delete('/users/{email}')
def delete_user_by_email(db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return userService.delete_user(email,db)

@user_router.post('/auth/refresh')
def refresh_token(data: userSchema.UserRefreshToken, db: Session = Depends(database.get_db)):
    return userService.get_refresh_token(data,db)
    
    