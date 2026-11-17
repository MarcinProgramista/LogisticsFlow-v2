from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
   return {"message": "Welcome to LogisticsFlow"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
