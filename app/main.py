from fastapi import FastAPI
from app.routers.auth import router as auth_router

app = FastAPI()
app.include_router(auth_router)

@app.get("/")
def root():
   return {"message": "Welcome to LogisticsFlow"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
