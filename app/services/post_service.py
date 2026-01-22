from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate

def create_post(db: Session, post: PostCreate, user_id: int):
    new_post = Post(
        title=post.title,
        content=post.content,
        user_id=user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post 

def get_posts(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def update_post(db: Session, post_id: int, post_data: PostUpdate, user_id: int):
    db_post = get_post_by_id(db, post_id)
    if not db_post:
        return None
    update_data = post_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int, user_id: int):
    db_post = get_post_by_id(db, post_id)
    if not db_post:
        return None
    if db_post.user_id != user_id:
        return None
    db.delete(db_post)
    db.commit()
    return True

def like_post(db: Session, post_id: int, user_id: int):
    db_post = get_post_by_id(db, post_id)
    if not db_post:
        return None
    if db_post.user_id != user_id:
        return None
    db_post.likes = db_post.likes + 1
    db.commit()
    db.refresh(db_post)
    return db_post

def unlike_post(db: Session, post_id: int, user_id: int):
    db_post = get_post_by_id(db, post_id)
    if not db_post:
        return None
    if db_post.user_id != user_id:
        return None
    db_post.likes = db_post.likes - 1
    db.commit()
    db.refresh(db_post)
    return db_post