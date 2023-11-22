from sqlalchemy import insert, delete, select, and_
from fastapi import APIRouter, Body

from db.database import async_session_maker
from models.categories import CategoryModel
from models.reception import ReceptionPointModel
from schemas.categories import *
from schemas.reception import Point, ShortPoint


router = APIRouter(prefix='/api/v1')

@router.get('/categories')
async def get_categories():
    async with async_session_maker() as session:
        categories = select(CategoryModel)
        res = await session.execute(categories)
        return {'categories': res.scalars().all()}

@router.get('/reception/categories/{title}', response_model=list[ShortPoint])
async def get_reception_by_title(title: str):
    async with async_session_maker() as session:
        query = select(
            ReceptionPointModel).where(ReceptionPointModel.category == select(CategoryModel.id).where(CategoryModel.title == title))
        points = await session.execute(query)
        return points.scalars().all()
