from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from schema import userSchema
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException, status

pwd_context = CryptContext(schemes=["argon2"])

SECRET_KEY='3af1230c48549649af617844f9c647dda2f22b926f84cd002ba75016e0caa102'
ACCESS_TOKEN_EXPIRY_IN_MINUTES=5
REFRESH_TOKEN_EXPIRY_IN_MINUTES=15
ALGORITHM = 'HS256'

security = HTTPBearer(bearerFormat="jwt")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def create_token(data):
    iat = datetime.utcnow()
    exp = iat + timedelta(minutes=ACCESS_TOKEN_EXPIRY_IN_MINUTES)
    
    access_token_data = {
        "iat": iat,
        "exp": exp,
        "sub": data.email,
        "type": "access"
    }
    
    access_token = jwt.encode(access_token_data, SECRET_KEY, algorithm=ALGORITHM)
    refresh_token, refresh_expiry = create_refresh_token(data)
    
    return userSchema.UserToken(access_token=access_token, access_token_expires_in=exp, refresh_token=refresh_token, refresh_token_expires_in=refresh_expiry)
    
def create_refresh_token(data):
    iat = datetime.utcnow()
    exp = iat + timedelta(minutes=REFRESH_TOKEN_EXPIRY_IN_MINUTES)
    
    refresh_token_data = {
        "iat": iat,
        "exp": exp,
        "sub": data.email,
        "type": "refresh"
    }
    
    refresh_token = jwt.encode(refresh_token_data, SECRET_KEY, algorithm=ALGORITHM)
    return refresh_token, exp


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get('sub')
        return email
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid jwt token')
    
def decode_token(token):
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get('sub')
        type = payload.get('type')
        return email, type
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid jwt token')
    