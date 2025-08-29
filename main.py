# main.py
from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import ProductSchema
from database import engine,session
import database_model
from sqlalchemy.orm import Session
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

# In-memory product list
products = [
    ProductSchema(id=1, name="Phone", description="Smart phone", price=1000, quantity=10),
    ProductSchema(id=2, name="TV", description="TV", price=100, quantity=100),
]

database_model.Base.metadata.create_all(bind=engine)

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()
def init_db():
    db=session()

    count=db.query(database_model.Products).count
    if count==0:
        for product in products:
            db.add(database_model.Products(**product.model_dump()))
        db.commit()

init_db()
    


@app.get("/")
def greet():
    return "Welcome to fastapi tutorial"



@app.get("/products")
def get_all_product(db: Session= Depends(get_db)):
    db_products=db.query(database_model.Products).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id: int,db: Session= Depends(get_db)):
    db_product=db.query(database_model.Products).filter(database_model.Products.id==id).first()
    if db_product:
        return db_product
    return "Product not found"

@app.post("/products")
def add_product(product: ProductSchema,db: Session= Depends(get_db)):
    db.add(database_model.Products(**product.model_dump()))
    db.commit()
    return {"message": "Product added", "product": product}

@app.put("/products")
def update_product(id: int, product: ProductSchema,db: Session= Depends(get_db)):
    db_product=db.query(database_model.Products).filter(database_model.Products.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.quantity=product.quantity
        db_product.price=product.price
        db.commit()
        return "Product updated"
    else:
        return {"error": "No product found"}

@app.delete("/products")
def delete_product(id: int,db: Session= Depends(get_db)):
    db_product=db.query(database_model.Products).filter(database_model.Products.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return {"error": "Product not found"}
