from ..import models, schemas,utils
from fastapi import status, HTTPException, Depends, APIRouter 
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(prefix="/users", tags=['Users'])

#@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.userout) 
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.userout) 
def create_user(user:schemas.usercreate,db: Session = Depends(get_db)):
   # hashing the password - user.password
   hashed_password = utils.pwd_context.hash(user.password)
   user.password = hashed_password
   new_user = models.user(**user.dict()) # the ** extracts all the schemas from Post class - model.py 
   db.add(new_user)
   db.commit()
   db.refresh(new_user) # after passing the response in decorator, here new_post is a sqlachemy model& pydantic dont know sqlachemy model. Need to configure in schemas(updated config class)
   return new_user 

#@router.get("/users/{id}",response_model=schemas.userout)
@router.get("/{id}",response_model=schemas.userout)
def get_user(id:int,db: Session = Depends(get_db)):
   user = db.query(models.user).filter(models.user.id == id).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"User with id:{id} does not exist")
   return user 