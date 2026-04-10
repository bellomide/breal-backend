from model import userModel
from fastapi import HTTPException, status
from security import securityConfig
from repository import database
from schema import userSchema

userModel.database.Base.metadata.create_all(database.engine)


def register_user(data,db):
    if data:
        accessLevel = None
        user = db.query(userModel.UserModel).filter(userModel.UserModel.email == data.email).first()
        if user:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='User account already exist')
        else:
            if data.role == "CLIENT" or data.role == "CONTRACTOR":
                accessLevel = "TEMPORARY"
            else:
                accessLevel = "FULL"
            user = userModel.UserModel(email=data.email,password=data.password, role=data.role, access_level=accessLevel)
            #hash password
            if user.password:
                user.password = securityConfig.hash_password(user.password)
            
            db.add(user)
            db.commit()
            db.refresh(user)
            
            print('user account created')
            user_data = userSchema.UserData(id=user.id, role=user.role, access_level=user.access_level)
            return userSchema.UserResponse(status="success", data=user_data)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Invalid details')

def login(data,db):
    if data:
        user = db.query(userModel.UserModel).filter(userModel.UserModel.email == data.email).first()
        if user:
            if securityConfig.verify_password(data.password,user.password):
                return securityConfig.create_token(data)
            else:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid user email and password')
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Invalid details')
            

def get_user(email, role, db):
    user_data = db.query(userModel.UserModel).filter(userModel.UserModel.email == email).filter(userModel.UserModel.role == role).first()
    return user_data

def fetch_all_user(db):
    user_list = db.query(userModel.UserModel).filter(userModel.UserModel.role == userSchema.UserRole.client).all()
    return user_list
    
def update_user(email, data, db):
    user_data = db.query(userModel.UserModel).filter(userModel.UserModel.email == email).first()
    
    if user_data:
        updated_user_data = userModel.UserModel(email=email, password=user_data.password, access_level=user_data.access_level, role=user_data.role)
        
        if data.password:
            updated_user_data.password = data.password
        if data.access_level:
            updated_user_data.access_level = data.access_level
        if data.role:
            updated_user_data.role = data.role
        db.commit()
        db.refresh(updated_user_data)
        return updated_user_data
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid user details')
    
def delete_user(email,db):
    user_data = db.query(userModel.UserModel).filter(userModel.UserModel.email == email).first()
    if user_data:
        db.delete(user_data)
        return {
            "status": "success",
            "message": "user details deleted successfully",
            "email": email
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid user details')
    
def get_refresh_token(data,db):
    email, token_type = securityConfig.decode_token(data.token)
    if email == data.email:
        if token_type == "refresh":
            return securityConfig.create_token(data)
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Invalid refresh token')
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Invalid email')