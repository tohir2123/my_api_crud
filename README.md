# My API CRUD with SQLAlchemy

FastAPI + SQLAlchemy asosida yozilgan kichik CRUD API. Loyihada `Users`, `Posts` va `Todos` bo‘yicha endpointlar mavjud. Ma’lumotlar bazasi sifatida PostgreSQL ishlatiladi, migratsiyalar uchun Alembic mavjud.

## Asosiy imkoniyatlar
- Users, Posts, Todos CRUD
- Postlarga like/unlike va comment endpointlari
- Todos uchun complete/incomplete
- Swagger UI (`/docs`) va ReDoc (`/redoc`)

## Texnologiyalar
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Pydantic

## Talablar
- Python 3.9+ (tavsiya)
- PostgreSQL

## O‘rnatish va ishga tushirish
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

`.env` fayl yarating (namuna):
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASS=your_password
```

Migratsiyalar (agar Alembic sozlangan bo‘lsa):
```bash
alembic upgrade head
```

Serverni ishga tushirish:
```bash
uvicorn app.main:app --reload
```

## API Endpointlar

### Users
- `POST /users` — user yaratish
- `GET /users` — userlar ro‘yxati
- `GET /users/{user_id}` — bitta user
- `PUT /users/{user_id}` — userni yangilash
- `DELETE /users/{user_id}` — userni o‘chirish

### Posts (query param: `user_id`)
- `POST /posts?user_id=1`
- `GET /posts?user_id=1`
- `GET /posts/{post_id}?user_id=1`
- `PUT /posts/{post_id}?user_id=1`
- `DELETE /posts/{post_id}?user_id=1`
- `PUT /posts/{post_id}/like?user_id=1`
- `PUT /posts/{post_id}/unlike?user_id=1`
- `DELETE /posts?user_id=1` — userning barcha postlarini o‘chirish
- `PUT /posts/{post_id}/comment?user_id=1&comment=...`
- `DELETE /posts/{post_id}/comment?user_id=1&comment_id=...`

### Todos (query param: `user_id`)
- `POST /todos?user_id=1`
- `GET /todos?user_id=1`
- `GET /todos/{todo_id}?user_id=1`
- `PUT /todos/{todo_id}?user_id=1`
- `DELETE /todos/{todo_id}?user_id=1`
- `PUT /todos/{todo_id}/complete?user_id=1`
- `PUT /todos/{todo_id}/incomplete?user_id=1`
- `DELETE /todos?user_id=1` — userning barcha todolarini o‘chirish
- `PUT /todos/{todo_id}/like?user_id=1`
- `PUT /todos/{todo_id}/unlike?user_id=1`

## Misol so‘rovlar
User yaratish:
```bash
curl -X POST "http://127.0.0.1:8000/users" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","username":"test","password":"secret"}'
```

Post yaratish:
```bash
curl -X POST "http://127.0.0.1:8000/posts?user_id=1" \
  -H "Content-Type: application/json" \
  -d '{"title":"Hello","content":"First post"}'
```

Todo yaratish:
```bash
curl -X POST "http://127.0.0.1:8000/todos?user_id=1" \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn FastAPI","description":"CRUD project"}'
```

## Loyihaning tuzilishi
```
app/
  core/
  models/
  routers/
  schemas/
  services/
  main.py
alembic/
requirements.txt
```
