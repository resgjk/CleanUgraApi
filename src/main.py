from fastapi import FastAPI
from models.categories import CategoryModel
from models.reception import ReceptionPointModel
from routers.router import router
import uvicorn


app = FastAPI(
    title='MyAPI'
)

@app.get('/')
def hello():
    return 'Hello everybody'

def main():
    app.include_router(router)
    uvicorn.run(app=app, host='127.0.0.1', port=8080)
    

if __name__ == '__main__':
    main()
