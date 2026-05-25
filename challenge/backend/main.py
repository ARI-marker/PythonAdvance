from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ======================
# CATEGORIES
# ======================

@app.post("/categories/")
def create_category(category: schemas.CategoryBase, db: Session = Depends(get_db)):

    if not category.name.strip():
        return {"error": "Category name cannot be empty"}

    existing = db.query(models.Category).filter(models.Category.name == category.name).first()
    if existing:
        return {"error": "Category already exists"}

    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@app.get("/categories/")
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


@app.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):

    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()

    if not db_category:
        return {"error": "Category not found"}

    db.delete(db_category)
    db.commit()
    return {"message": "Deleted"}

# ======================
# RECIPES
# ======================

@app.post("/recipes/")
def create_recipe(recipe: schemas.RecipeBase, db: Session = Depends(get_db)):

    db_recipe = models.Recipe(
        title=recipe.title,
        description=recipe.description,
        category_id=recipe.category_id
    )

    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


@app.get("/recipes/")
def get_recipes(db: Session = Depends(get_db)):
    return db.query(models.Recipe).all()


@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):

    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

    if not db_recipe:
        return {"error": "Recipe not found"}

    db.delete(db_recipe)
    db.commit()
    return {"message": "Deleted"}