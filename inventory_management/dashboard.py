import streamlit as st
import pandas as pd
import requests
from database import get_connection

API_URL = "http://127.0.0.1:8000"

st.title("Inventory Management System")

page = st.sidebar.selectbox("Menu", ["Suppliers", "Products"])

conn = get_connection()
if page == "Products":

    st.subheader("Products Table")

    df = pd.read_sql_query("SELECT * FROM products", conn)

    st.dataframe(df, use_container_width=True)

    st.text("You can copy from table (CTRL + C)")

    st.divider()

    st.subheader("Delete Product")
    delete_id = st.number_input("Product ID", min_value=1)
    if st.button("Delete Product"):
        res = requests.delete(f"{API_URL}/products/{delete_id}")
        st.rerun()

    st.divider()

    st.subheader("Update Product")

    update_id = st.number_input("ID to update", min_value=1)

    name = st.text_input("Name")
    category = st.text_input("Category")
    price = st.number_input("Price", min_value=0.0)
    quantity = st.number_input("Quantity", min_value=0)
    supplier_id = st.number_input("Supplier ID", min_value=1)

    if st.button("Update Product"):
        data = {
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "supplier_id": supplier_id
        }

        res = requests.put(f"{API_URL}/products/{update_id}", json=data)
        st.rerun()


if page == "Suppliers":

    st.subheader("Suppliers Table")

    df = pd.read_sql_query("SELECT * FROM suppliers", conn)

    st.dataframe(df, use_container_width=True)

conn.close()