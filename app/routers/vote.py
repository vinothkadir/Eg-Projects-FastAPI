from fastapi import Response, status, HTTPException, Depends,APIRouter
from ..import schemas, database, oauth2,models
from sqlalchemy.orm import session

router = APIRouter(prefix="/vote", tags=["vote"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.vote, db:  session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

   post = db.query(models.vote).filter(models.Post.id==vote.post_id).first()
   if not post:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id:{vote.post_id}does not exist")
   vote_query = db.query(models.vote).filter(models.vote.post_id == vote.post_id, models.vote.users_id == current_user.id)
   found_vote = vote_query.first()
   if vote.dir == 1:
      if found_vote:
         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on post {vote.post_id}")
      new_post = models.vote(post_id = vote.post_id, users_id = current_user.id)
      db.add(new_post)
      db.commit() 
      return {"message": "successfully added vote"}
   else:
      if not found_vote:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does note exist")
      vote_query.delete(synchronize_session=False)
      db.commit()  

      return {"message": "successfully deleted vote"} 