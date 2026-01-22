from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate

def create_todo(db: Session, todo: TodoCreate, user_id: int):
    new_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=False,  # default False for new todos
        user_id=user_id
    )
    db.add(new_todo)
    db.commit()  
    db.refresh(new_todo)
    return new_todo

def get_todos(db: Session, user_id: int):
    return db.query(Todo).filter(Todo.user_id == user_id).all()

def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

def update_todo(db: Session, todo_id: int, todo_data: TodoUpdate, user_id: int):
    db_todo = get_todo_by_id(db, todo_id)
    if not db_todo:
        return None
    
    update_data = todo_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int, user_id: int):
    db_todo = get_todo_by_id(db, todo_id)
    if not db_todo:
        return None
    if db_todo.user_id != user_id:
        return None
    db.delete(db_todo)
    db.commit()
    return True

def complete_todo(db: Session, todo_id: int, user_id: int):
    db_todo = get_todo_by_id(db, todo_id)
    if not db_todo:
        return None
    if db_todo.user_id != user_id:
        return None
    db_todo.completed = db_todo.completed + 1
    db.commit()
    db.refresh(db_todo)
    return db_todo

def incomplete_todo(db: Session, todo_id: int, user_id: int):
    db_todo = get_todo_by_id(db, todo_id)
    if not db_todo:
        return None
    if db_todo.user_id != user_id:
        return None
    db_todo.completed = 0
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_all_todos(db: Session, user_id: int):
    db_todos = get_todos(db, user_id)
    if not db_todos:
        return None
    for todo in db_todos:
        db.delete(todo)
    db.commit()
    return True