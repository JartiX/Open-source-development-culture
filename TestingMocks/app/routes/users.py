from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User, CSVData
from app.schemas import UserCreate
import hashlib

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
    db_user = User(username=user.username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User registered successfully"}

@router.get("/", response_model=list[dict[str, str]])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"username": user.username, "id": str(user.id)} for user in users]
@router.get("/{user_id}/data", response_model=list[dict[str, str]])

async def get_user_data(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    data = db.query(CSVData).filter(CSVData.user_id == user_id).all()
    return [{"id": str(entry.id), "content": entry.content} for entry in data]