from fastapi import FastAPI

app = FastAPI(title="Project 2 API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Project 2 API is alive"}
