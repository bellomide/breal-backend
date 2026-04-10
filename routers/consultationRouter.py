from fastapi import APIRouter, HTTPException, status, Depends
from repository import database
from service import consultationService
from schema import consultationSchema, userSchema
from sqlalchemy.orm import Session
from security import securityConfig
from service import userService
from fastapi.security import HTTPAuthorizationCredentials

consultation_router = APIRouter()

@consultation_router.post('/consultations')
def create_consultations(data: consultationSchema.ConsultationSchema, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return consultationService.create_consultation(email,data,db)
    
@consultation_router.get('/consultations/my')
def get_my_consultation(db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return consultationService.get_my_consultations(email,db)

@consultation_router.get('/admin/consultations')
def get_all_consultation(db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    user_data = userService.get_user(email,db)
    if user_data.role == userSchema.UserRole.admin:
        return consultationService.get_consultations(db)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Admin is only authorized to use this api')

@consultation_router.post('/admin/consultations/{consultation_id}')
def update_consultation(consultation_id: int, data: consultationSchema.UpdateConsultation, db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    user_data = userService.get_user(email,db)
    if user_data.role == userSchema.UserRole.admin:
        return consultationService.update_consultation(consultation_id,data.db)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Admin is only authorized to use this api')
