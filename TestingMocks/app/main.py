import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from app.routes import users
from app.database import Base, engine
import uvicorn


Base.metadata.create_all(bind=engine)
app = FastAPI(title="FastAPI CSV API")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(files.router, prefix="/files", tags=["Files"])

@app.get("/")
async def root():
    return {"message": "FastAPI is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
