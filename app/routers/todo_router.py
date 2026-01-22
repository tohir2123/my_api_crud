from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.todo import TodoCreate, TodoOut, TodoUpdate
from app.services import todo_service, post_service

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

@router.post("/", response_model=TodoOut, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, user_id: int, db: Session = Depends(get_db)):
    return todo_service.create_todo(db, todo, user_id)

@router.get("/", response_model=list[TodoOut])
def get_todos(user_id: int, db: Session = Depends(get_db)):
    return todo_service.get_todos(db, user_id)

@router.get("/{todo_id}", response_model=TodoOut)
def get_todo(todo_id: int, user_id: int, db: Session = Depends(get_db)):
    db_todo = todo_service.get_todo_by_id(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo topilmadi")
    return db_todo

@router.put("/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: int, todo_data: TodoUpdate, user_id: int, db: Session = Depends(get_db)):
    updated_todo = todo_service.update_todo(db, todo_id, todo_data, user_id)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo topilmadi")
    return updated_todo

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, user_id: int, db: Session = Depends(get_db)):
    success = todo_service.delete_todo(db, todo_id, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo topilmadi")
    return None

@router.put("/{todo_id}/complete", response_model=TodoOut)
def complete_todo(todo_id: int, user_id: int, db: Session = Depends(get_db)):
    completed_todo = todo_service.complete_todo(db, todo_id, user_id)
    if not completed_todo:
        raise HTTPException(status_code=404, detail="Todo topilmadi")
    return completed_todo
    
@router.put("/{todo_id}/incomplete", response_model=TodoOut)
def incomplete_todo(todo_id: int, user_id: int, db: Session = Depends(get_db)):
    incomplete_todo = todo_service.incomplete_todo(db, todo_id, user_id)
    if not incomplete_todo:
        raise HTTPException(status_code=404, detail="Todo topilmadi")
    return incomplete_todo

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_all_todos(user_id: int, db: Session = Depends(get_db)):
    success = todo_service.delete_all_todos(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo topilmadi")
    return None

@router.put("/{todo_id}/like", response_model=TodoOut)
def like_todo(todo_id: int, user_id: int, db: Session = Depends(get_db)):
    liked_todo = todo_service.like_todo(db, todo_id, user_id)
    if not liked_todo:
        raise HTTPException(status_code=404, detail="Todo topilmadi")
    return liked_todo

@router.put("/{todo_id}/unlike", response_model=TodoOut)
def unlike_todo(todo_id: int, user_id: int, db: Session = Depends(get_db)):
    unliked_todo = todo_service.unlike_todo(db, todo_id, user_id)
    if not unliked_todo:
        raise HTTPException(status_code=404, detail="Todo topilmadi")
    return unliked_todo

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_all_posts(user_id: int, db: Session = Depends(get_db)):
    success = post_service.delete_all_posts(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post topilmadi")
    return None