from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT
from schema import Settings
from auth_routes import auth_router


app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router)


