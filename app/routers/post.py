from fastapi import FastAPI, Response, status, HTTPException,Depends, APIRouter
from .. import models, schemas,oauth2
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from typing import List,Optional

router = APIRouter(
    prefix="/posts",
    tags=['Post']
)



@router.get("/",response_model=List[schemas.PostOut])
async def get_post(db : Session = Depends(get_db),user_id : int = Depends(oauth2.get_current_user),limit : int = 10,skip : int = 0,search : Optional[str] = ""):
    
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    results = db.query(models.Post, func.count(models.Post.id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id,isouter= True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
            
    posts = [{"Post": post, "votes": votes} for post, votes in results]
    
    return posts
 


@router.post("/",status_code=status.HTTP_201_CREATED,response_model= schemas.Post)
async def create_posts(post : schemas.PostCreate,db : Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id = current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}",response_model=schemas.PostOut)
async def get_post(id: int,db : Session = Depends(get_db),user_id : int = Depends(oauth2.get_current_user)):
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    
    post = db.query(models.Post, func.count(models.Post.id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id,isouter= True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post




@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_posts(id : int,db : Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    delete_posts = db.query(models.Post).filter(models.Post.id == id)
    post = delete_posts.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    if post.owner_id != current_user.id :
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN,detail="Not Authorized to perform requested action")
    delete_posts.delete(synchronize_session=False)
    db.commit()
    return {"message" : "Post deleted successfully"}




@router.put("/{id}",response_model= schemas.Post)
async def update_post(id : int, updated_post : schemas.PostUpdate,db : Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    if post.owner_id != current_user.id :
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN,detail="Not Authorized to perform requested action")
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()