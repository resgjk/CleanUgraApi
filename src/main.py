from fastapi import FastAPI
from models.categories import CategoryModel
from models.reception import ReceptionPointModel
from routers.router import router
import uvicorn

#import asyncio
#from db.database import create_all_tables


app = FastAPI(
    title='MyAPI'
)

app.include_router(router=router)