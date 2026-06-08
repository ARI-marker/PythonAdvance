from pydantic import BaseModel


class Supplier(BaseModel):
    name: str
    phone: str
    email: str
    address: str


class Product(BaseModel):
    name: str
    category: str
    price: float
    quantity: int
    supplier_id: int