from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str


class RecipeBase(BaseModel):
    title: str
    description: str
    category_id: int