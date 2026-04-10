from fastapi import APIRouter, Depends, status, HTTPException
from schema import paymentSchema, userSchema
from repository import database
from sqlalchemy.orm import Session
from security import securityConfig
from service import paymentService, userService
from fastapi.security import HTTPAuthorizationCredentials


payment_router = APIRouter()

def is_client(email,db):
    return userService.get_user(email,userSchema.UserRole.client,db)

@payment_router.post('/payments/initialize')
def initialize_payment(data: paymentSchema.PaymentSchema, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    if is_client(email,db) is not None:
        return paymentService.init_payment(data,email,db)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Client is only authorized')
    
@payment_router.post('/payments/verify')
def verify_payment(data: paymentSchema.VerifyPayment, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return paymentService.verify_payment(data.reference, db)

