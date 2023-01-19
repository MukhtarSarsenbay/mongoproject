from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str
    height: float
    weight: float
