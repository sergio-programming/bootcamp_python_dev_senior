from fastapi import FastAPI
from routers import auth_routes, task_routes
from core.logger import init_logger
from database.session import Base, engine
from models import user_task

app = FastAPI()

Base.metadata.create_all(bind= engine)
init_logger()
app.include_router(auth_routes.router)


