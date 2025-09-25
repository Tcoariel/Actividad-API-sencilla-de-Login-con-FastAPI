from fastapi import FastAPI

app = FastAPI()

@app.post("/login")
async def login(data: dict):
    if data.get("username") == "admin" and data.get("password") == "1234":
        return {"resp": "login exitoso"}
    return {"resp": "login fallido"}
