from fastapi import FastAPI
from src.models.categories import CategoryModel
from src.models.reception import ReceptionPointModel
from src.routers.router import router
import uvicorn

#import asyncio
#from db.database import create_all_tables


app = FastAPI(
    title='MyAPI'
)

app.include_router(router=router)