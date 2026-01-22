import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import all models to ensure SQLAlchemy relationships are resolved
from app.models import User, Post, Todo
from app.core.database import engine
from app.core.database import init_db
from app.core.database import get_db
from fastapi import FastAPI
from app.routers.user_router import router as users_router
from app.routers.post_router import router as posts_router
from app.routers.todo_router import router as todos_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    engine.connect()
    init_db()
    db = next(get_db())
    db.execute("SELECT 1")
    db.close()

@app.on_event("shutdown")
def shutdown_event():
    engine.dispose()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
app.include_router(users_router)
app.include_router(posts_router)
app.include_router(todos_router)