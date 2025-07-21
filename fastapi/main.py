from fastapi import FastAPI
from routers.user_route import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/users")



