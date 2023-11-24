from fastapi import FastAPI
from src.routers.router import router


app = FastAPI(
    title='MyAPI'
)

app.include_router(router=router)
