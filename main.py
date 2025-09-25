from fastapi import FastAPI
from sqlmodel import SQLModel
from pydantic import BaseModel  

app = FastAPI()

class LoginData(SQLModel):
    username: str
    password: str

@app.post("/login")
async def login(data: LoginData):
    if data.username == "GRUPO9" and data.password == "admin123":
        return {"resp": "login exitoso"}
    return {"resp": "login fallido"}
