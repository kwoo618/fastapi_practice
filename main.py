from fastapi import FastAPI
from controller import items, users

app=FastAPI()

app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/hello")
async def hello():
	return{"message":"hello world"}