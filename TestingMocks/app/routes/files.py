from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import CSVData


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/upload")
async def upload_file(user_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    db_entry = CSVData(user_id=user_id, content=content.decode())
    db.add(db_entry)
    db.commit()
    return {"message": "File uploaded successfully"}
