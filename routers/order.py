from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import *
from model import *

router = APIRouter(prefix="/orders")

@router.post("/")
def create_order(db: Session = Depends(get_db)):
    cart_items = db.query(Cart).all()
    total = sum(item.quantity * 100 for item in cart_items)

    order = Order(user_id=1, total_price=total)
    db.add(order)
    db.commit()

    return {"total": total}