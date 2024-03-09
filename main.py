from fastapi import FastAPI
from routes.auth import auth_router
from db.models import Base
from db.settings import engine

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(auth_router, prefix="/api/v1")
# @AuthJWT.load_config
# def get_config():
#     return Settings()

# app.include_router(auth_router)


