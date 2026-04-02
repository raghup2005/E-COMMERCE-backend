# 🛒 E-Commerce Backend (FastAPI)

## 🚀 Overview

This is a **production-style E-commerce Backend API** built using **FastAPI**.
It includes authentication, product management, cart system, and order processing.

---

## 🧠 Features

* 🔐 JWT Authentication (Login & Signup)
* 👤 User Management
* 📦 Product APIs
* 🛒 Cart System (User-specific)
* 📑 Order Management
* 🔎 Search & Pagination
* 🧱 Clean Architecture (Routers, Services, Models)

---

## 🛠️ Tech Stack

* **FastAPI**
* **SQLAlchemy**
* **SQLite**
* **Pydantic**
* **JWT (python-jose)**
* **Passlib (bcrypt)**

-

## 📌 API Endpoints

### 🔐 Auth

* POST `/auth/signup`
* POST `/auth/login`

### 📦 Products

* GET `/products`
* POST `/products`

### 🛒 Cart

* POST `/cart/add`
* GET `/cart`

### 📑 Orders

* POST `/order`
* GET `/orders`

---

##  Authentication

* Uses **JWT Tokens**
* Pass token in header:

```
Authorization: Bearer <your_token>
```

---

##  Testing

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

##  Future Improvements

* Payment Integration (Stripe)
* Product Images Upload
* Admin Dashboard
* Caching (Redis)

---

##  Author

**Raghu**
backend developer-FASTAPI

---

##  Notes

This project demonstrates:

* Clean backend architecture
* REST API design
* Authentication & security
* Database relationships

Perfect for **internship & backend roles** 🚀
