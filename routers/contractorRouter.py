from fastapi import APIRouter, Depends, status
from schema import contractorSchema
from service import contractorService
from sqlalchemy.orm import Session
from repository import database
from fastapi.security import HTTPAuthorizationCredentials
from security import securityConfig
contractor_router = APIRouter()

@contractor_router.post('/kyc/nin/verify', status_code=status.HTTP_201_CREATED)
def create_contractor(data: contractorSchema.ContractorSchema, email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    contractorService.verifyContractor(data)
    
@contractor_router.post('/contractors/profile')
def create_contractor_profile(data: contractorSchema.ContractorProfileSchema, email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user), db: Session = Depends(database.get_db)):
    return contractorService.create_contractor_profile(data,email,db)

@contractor_router.get('/contractors/profile')
def fetch_contractor_profile(db: Session = Depends(database.get_db), email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user)):
    return contractorService.get_contractor_profile(email,db)

@contractor_router.patch('/contractors/profile')
def update_contractor_profile(data: contractorSchema.UpdateContractorProfile, email: HTTPAuthorizationCredentials = Depends(securityConfig.get_current_user), db: Session = Depends(database.get_db)):
    return contractorService.update_contractor_profile(email,data,db)