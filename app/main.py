from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import file_router

app = FastAPI()
app.include_router(file_router.router, prefix="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
