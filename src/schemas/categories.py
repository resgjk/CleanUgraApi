from pydantic import BaseModel

class CategoryCreate(BaseModel):
    title: str
    rules: str
    not_take: str

class CategoryImage(BaseModel):
    id: int
    img: str
