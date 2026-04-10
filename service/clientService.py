from model import clientModel
from service import userService
from schema import userSchema
from fastapi import HTTPException, status
from repository import database

clientModel.database.Base.metadata.create_all(database.engine)


def create_client_profile(data,email ,db):
    user_data = userService.get_user(email,userSchema.UserRole.client,db)
    client_data = db.query(clientModel.ClientProfile).filter(clientModel.ClientProfile.user_id == user_data.id).first()
    if client_data:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Client Profile Already Exists')
    else:
        new_client = clientModel.ClientProfile(user_id=user_data.id,full_name=data.full_name,country=data.country,phone=data.phone,preferred_currency=data.preferred_currency)
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
        return {
            "status":"success",
            "message":"Client Profile Created"
        }
    
def get_client_profile(email,db):
    user_data = userService.get_user(email,userSchema.UserRole.client,db)
    client_data = db.query(clientModel.ClientProfile).filter(clientModel.ClientProfile.user_id == user_data.id).first()
    if client_data:
        return client_data
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Client Profile Not Found')

def update_client_profile(email,data,db):
    user_data = userService.get_user(email,userSchema.UserRole.client,db)
    client_data = db.query(clientModel.ClientProfile).filter(clientModel.ClientProfile.user_id == user_data.id).first()
    if client_data:
        if data.full_name:
            client_data.full_name = data.full_name
        if data.phone:
            client_data.phone = data.phone
        if data.preferred_currency:
            client_data.preferred_currency = data.preferred_currency
            
        db.commit()
        db.refresh(client_data)
        return {
            "status":"success",
            "message":"Client profile updated"
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Client profile not found')
    
    