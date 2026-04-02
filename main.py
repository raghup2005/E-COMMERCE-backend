from fastapi import FastAPI
from database import engine,base

from routers import authe, product, cart, order

app = FastAPI()

base.metadata.create_all(bind=engine)

app.include_router(authe.router)
app.include_router(product.router)
app.include_router(cart.router)
app.include_router(order.router)