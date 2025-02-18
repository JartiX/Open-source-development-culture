from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str

class CSVDataResponse(BaseModel):
    user_id: int
    content: str