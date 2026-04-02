from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from model import *

router = APIRouter(prefix="/products")

@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    return new_product

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()