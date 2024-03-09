from fastapi import FastAPI

from api.routes.auth import auth_router


app = FastAPI()

app.include_router(auth_router, prefix="/api/v1")
# @AuthJWT.load_config
# def get_config():
#     return Settings()

# app.include_router(auth_router)


