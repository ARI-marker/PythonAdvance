from fastapi import FastAPI
from database import create_tables, get_connection
from schemas import Supplier, Product

app = FastAPI(title="Inventory Management System")

create_tables()


@app.get("/")
def home():
    return {"message": "Inventory API Running"}


@app.post("/suppliers")
def add_supplier(supplier: Supplier):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO suppliers (name, phone, email, address)
    VALUES (?, ?, ?, ?)
    """, (
        supplier.name,
        supplier.phone,
        supplier.email,
        supplier.address
    ))

    conn.commit()
    conn.close()

    return {"message": "Supplier added successfully"}


@app.get("/suppliers")
def get_suppliers():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM suppliers")

    suppliers = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return suppliers


@app.post("/products")
def add_product(product: Product):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO products
    (name, category, price, quantity, supplier_id)
    VALUES (?, ?, ?, ?, ?)
    """, (
        product.name,
        product.category,
        product.price,
        product.quantity,
        product.supplier_id
    ))

    conn.commit()
    conn.close()

    return {"message": "Product added successfully"}


@app.get("/products")
def get_products():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM products
    """)

    products = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return products