# 📜 Quotes API (FastAPI + SQLite)

A production-ready **Quotes API** with CRUD, search, pagination, and JWT authentication. Built using **FastAPI**, **SQLAlchemy**, and **SQLite**.

---

## 🚀 Features

* List quotes with pagination
* Search quotes by author or keyword
* Add, update, delete quotes (secured with JWT token)
* SQLite + SQLAlchemy ORM
* Auto-generated Swagger docs (`/docs`)
* Ready for deployment

---

## 📂 Project Structure

```
quotes_api/
│── app/
│   ├── main.py          # FastAPI entrypoint
│   ├── database.py      # DB connection
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py          # CRUD logic
│   ├── auth.py          # Simple JWT auth
│── requirements.txt
│── README.md
```

---

## 🔧 Setup

### 1. Clone repo & install requirements

```bash
git clone git remote add origin https://github.com/mudassirejaz-art/Quotes_api.git
cd quotes_api
pip install -r requirements.txt
```

### 2. Run API

```bash
uvicorn app.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

## 🔑 Authentication

All **write operations** (POST, PUT, DELETE) require Bearer token.

Use header:

```
Authorization: Bearer secret123
```

---

## 📌 Endpoints

### 1. List Quotes

`GET /quotes/?skip=0&limit=10`

### 2. Search Quotes

`GET /quotes/search?author=Einstein&keyword=life`

### 3. Add Quote (Auth)

`POST /quotes/`

```json
{
  "author": "Einstein",
  "text": "Life is like riding a bicycle. To keep balance you must keep moving.",
  "category": "Motivation"
}
```

### 4. Update Quote (Auth)

`PUT /quotes/{id}`

```json
{
  "text": "Life is like riding a bicycle. To keep balance you must keep moving."
}
```

### 5. Delete Quote (Auth)

`DELETE /quotes/{id}`

---

## 🧪 Example cURL Request

```bash
curl -X POST "http://127.0.0.1:8000/quotes/" \
-H "Authorization: Bearer secret123" \
-H "Content-Type: application/json" \
-d '{"author":"Einstein","text":"Life is like riding a bicycle.","category":"Motivation"}'
```

---

## 📷 Screenshots

<img width="1366" height="716" alt="qoutes-APi" src="https://github.com/user-attachments/assets/3db51bcf-d073-42ce-b9e2-8bb7a4c062ad" />

---

## 📜 License

MIT License
