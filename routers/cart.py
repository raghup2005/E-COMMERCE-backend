from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import*
from model import*

router = APIRouter(prefix="/cart")
@router.post("/add")
def add_to_cart(cart: CartCreate, db: Session = Depends(get_db)):
    item = Cart(**cart.dict())
    db.add(item)
    db.commit()
    return {"message": "Added to cart"}