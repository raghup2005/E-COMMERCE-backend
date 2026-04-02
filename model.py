from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import*
from pydantic import BaseModel
class User(base):
    __tablename__ = "Users"
    id=Column(Integer,primary_key=True)
    username=Column(String,unique=True)
    password=Column(String)
    cart_items = relationship("Cart", back_populates="user")
    orders = relationship("Order", back_populates="user")
class Product(base):
    __tablename__ = "products"
    id =Column(Integer,primary_key=True)
    name=Column(String)
    price=Column(Integer)
    cart_items = relationship("Cart", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")

class Cart(base):
    __tablename__ = "carts"
    id=Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    quantity=Column(Integer)
    user = relationship("User", back_populates="cart_items")
    product = relationship("Product", back_populates="cart_items")
    

class Order(base):
    __tablename__ = "orders"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer)
    total_price=Column(Integer)
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
class OrderItem(base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")

class ProductCreate(BaseModel):
    name:str
    price:int

class UserCreate(BaseModel):
    username:str
    password:str

class CartCreate(BaseModel):
    product_id:int
    quantity:int
class Token(BaseModel):
    token_access:str
    token_type:str