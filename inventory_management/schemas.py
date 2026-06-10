from pydantic import BaseModel


class Supplier(BaseModel):
    name: str
    phone: int
    email: str
    address: str


class Product(BaseModel):
    name: str
    category: str
    price: float
    quantity: int
    supplier_id: int