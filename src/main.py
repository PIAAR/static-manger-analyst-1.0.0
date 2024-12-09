from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Static Manager Analyst 1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "OK"}
