# 📌 FastAPI CRUD Application

This is a simple **FastAPI** project demonstrating **CRUD operations** with a PostgreSQL database using **SQLAlchemy ORM** and **Pydantic**.

---

## ✨ Features

- ✅ FastAPI-based REST APIs  
- ✅ PostgreSQL database integration  
- ✅ SQLAlchemy ORM models  
- ✅ Pydantic schemas for request/response validation  
- ✅ CRUD operations:  
  - Get all products  
  - Get product by ID  
  - Add new product  
  - Update product by ID  
  - Delete product by ID  

---

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) 🚀  
- [SQLAlchemy](https://www.sqlalchemy.org/) 🗄️  
- [Pydantic](https://docs.pydantic.dev/) 🛡️  
- [PostgreSQL](https://www.postgresql.org/) 🐘  

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/SanyamBinayake/Fast-API.git
cd Fast-API
```

### 2. Create a virtual environment

```bash
python -m venv myenv
source myenv/bin/activate   # On Linux/Mac
myenv\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Update your database URL in `database_model.py` (or wherever you set it):

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/dataentry_db"
```

⚠️ Make sure PostgreSQL is installed and the database `dataentry_db` exists:

```bash
createdb dataentry_db
```

### 5. Run the FastAPI server

```bash
uvicorn main:app --reload
```

---

## 📡 API Endpoints

| Method | Endpoint                | Description          |
|--------|------------------------|----------------------|
| GET    | `/`                    | Welcome message      |
| GET    | `/products`            | Get all products     |
| GET    | `/product/{id}`        | Get product by ID    |
| POST   | `/add_product`         | Add a new product    |
| PUT    | `/update_by_id/{id}`   | Update product by ID |
| DELETE | `/delete/{id}`         | Delete product by ID |

---

## 📜 Example Request

### Add a Product

**Request**  
```http
POST /add_product
Content-Type: application/json

{
  "id": 1,
  "name": "Phone",
  "description": "Smart Phone",
  "price": 1000,
  "quantity": 10
}
```

**Response**  
```json
{
  "message": "Product added",
  "product": {
    "id": 1,
    "name": "Phone",
    "description": "Smart Phone",
    "price": 1000,
    "quantity": 10
  }
}
```

---

## 🧑‍💻 Author

👤 Sanyam Binayake
