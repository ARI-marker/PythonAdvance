import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Recipe Book PRO", layout="wide")

st.title("🍔 Recipe Book PRO")

menu = st.sidebar.selectbox("Menu", ["Categories", "Recipes"])

# ======================
# CATEGORIES
# ======================
if menu == "Categories":

    st.header("Categories")

    name = st.text_input("Category Name")

    if st.button("Add Category"):

        if name.strip() == "":
            st.error("Category name cannot be empty")
        else:
            res = requests.post(f"{API_URL}/categories/", json={"name": name})

            if res.status_code == 200:
                st.success("Added")
            else:
                st.error(res.json().get("error", "Error"))

    categories = requests.get(f"{API_URL}/categories/").json()

    for c in categories:
        col1, col2 = st.columns([4,1])

        with col1:
            st.write(f"🗂️ {c['name']} (ID: {c['id']})")

        with col2:
            if st.button(f"Delete {c['id']}"):
                requests.delete(f"{API_URL}/categories/{c['id']}")

# ======================
# RECIPES
# ======================
elif menu == "Recipes":

    st.header("Recipes")

    categories = requests.get(f"{API_URL}/categories/").json()

    category_map = {c["name"]: c["id"] for c in categories}

    title = st.text_input("Title")
    desc = st.text_area("Description")

    category = st.selectbox(
        "Category",
        list(category_map.keys()) if categories else []
    )

    if st.button("Add Recipe"):

        if not categories:
            st.error("Add a category first")
        else:
            requests.post(
                f"{API_URL}/recipes/",
                json={
                    "title": title,
                    "description": desc,
                    "category_id": category_map[category]
                }
            )
            st.success("Added")

    recipes = requests.get(f"{API_URL}/recipes/").json()

    for r in recipes:
        st.markdown("---")
        st.subheader(r["title"])
        st.write(r["description"])
        st.caption(f"Category ID: {r['category_id']}")

        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"Delete {r['id']}"):
                requests.delete(f"{API_URL}/recipes/{r['id']}")

        with col2:
            st.button(f"Edit {r['id']} (soon)")