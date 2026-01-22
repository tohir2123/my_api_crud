from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.post import PostCreate, PostOut, PostUpdate
from app.services import post_service

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/", response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, user_id: int, db: Session = Depends(get_db)):
    return post_service.create_post(db, post, user_id)

@router.get("/", response_model=list[PostOut])
def get_posts(user_id: int, db: Session = Depends(get_db)):
    return post_service.get_posts(db, user_id)

@router.get("/{post_id}", response_model=PostOut)
def get_post(post_id: int, user_id: int, db: Session = Depends(get_db)):
    db_post = post_service.get_post_by_id(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post topilmadi")
    return db_post

@router.put("/{post_id}", response_model=PostOut)
def update_post(post_id: int, post_data: PostUpdate, user_id: int, db: Session = Depends(get_db)):
    updated_post = post_service.update_post(db, post_id, post_data, user_id)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post topilmadi")
    return updated_post

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, user_id: int, db: Session = Depends(get_db)):
    success = post_service.delete_post(db, post_id, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post topilmadi")
    return None

@router.put("/{post_id}/like", response_model=PostOut)
def like_post(post_id: int, user_id: int, db: Session = Depends(get_db)):
    liked_post = post_service.like_post(db, post_id, user_id)
    if not liked_post:
        raise HTTPException(status_code=404, detail="Post topilmadi")
    return liked_post

@router.put("/{post_id}/unlike", response_model=PostOut)
def unlike_post(post_id: int, user_id: int, db: Session = Depends(get_db)):
    unliked_post = post_service.unlike_post(db, post_id, user_id)
    if not unliked_post:
        raise HTTPException(status_code=404, detail="Post topilmadi")
    return unliked_post

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_all_posts(user_id: int, db: Session = Depends(get_db)):
    success = post_service.delete_all_posts(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post topilmadi")
    return None

@router.put("/{post_id}/comment", response_model=PostOut)
def comment_post(post_id: int, comment: str, user_id: int, db: Session = Depends(get_db)):
    commented_post = post_service.comment_post(db, post_id, comment, user_id)
    if not commented_post:
        raise HTTPException(status_code=404, detail="Post topilmadi")
    return commented_post

@router.delete("/{post_id}/comment", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(post_id: int, comment_id: int, user_id: int, db: Session = Depends(get_db)):
    success = post_service.delete_comment(db, post_id, comment_id, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Comment topilmadi")
    return None