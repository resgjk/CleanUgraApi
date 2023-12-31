from sqlalchemy import select, desc
from fastapi import APIRouter
from typing import List

from src.db.database import async_session_maker
from src.models.categories import CategoryModel
from src.models.reception import ReceptionPointModel
from src.models.news import NewsModel
from src.schemas.reception import ShortPoint
from src.schemas.message import ReceiveMsg
from src.utils.change_message import change_message


router = APIRouter(prefix='/api/v1')

@router.get('/categories')
async def get_categories():
    async with async_session_maker() as session:
        categories = select(CategoryModel)
        res = await session.execute(categories)
        return {'categories': res.scalars().all()}

@router.get('/reception/categories/{title}')
async def get_receptions_by_category_title(title: str):
    async with async_session_maker() as session:
        query = select(
            ReceptionPointModel).where(
                ReceptionPointModel.category == select(
                    CategoryModel.id).where(CategoryModel.title == title))
        points = await session.execute(query)
        return points.scalars().all()

@router.get('/reception/{title}')
async def get_reception_by_title(title: str):
    async with async_session_maker() as session:
        query = select(ReceptionPointModel).where(
            ReceptionPointModel.title == title
        )
        point = await session.execute(query)
        return {'reception': point.scalar_one()}

@router.get('/news')
async def get_all_news():
    async with async_session_maker() as session:
        query = select(NewsModel).order_by(desc(NewsModel.id))
        news = await session.execute(query)
        return {'news': news.scalars().all()}

@router.post('/message/')
async def send_msg(message: ReceiveMsg):
    async with async_session_maker() as session:
        msg_dict = message.dict()
        cur_msg = change_message(msg_dict['message'])
        return {'message': cur_msg}
