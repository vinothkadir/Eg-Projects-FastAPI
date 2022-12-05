from datetime import datetime, timedelta
from jose import JWTError, jwt
from .import schemas, database, models
from sqlalchemy.orm import session
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')
#secret key
#algorithm
#Expiration time

SECRET_KEY = "afd591aed7c785f10ecaa26a771f33a95aec8bb8fde594d3bd8f7227cf82149c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def creater_access_token(data: dict):
   to_encode = data.copy()
   expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_MINUTES)
   to_encode.update({"exp":expire})
   encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

   return encoded_jwt 

def verify_access_token(token:str, credentials_exception):
   try:
      payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
      id: str = payload.get("user_id")
      if id is None:
         raise credentials_exception
      token_data = schemas.TokenData(id=id)
   except JWTError:
      raise credentials_exception 
   return token_data

def get_current_user(token: str = Depends(oauth2_schema), db: session = Depends(database.get_db)):
   credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
   token = verify_access_token(token, credentials_exception)
   user = db.query(models.user).filter(models.user.id == token.id).first()

   return user
