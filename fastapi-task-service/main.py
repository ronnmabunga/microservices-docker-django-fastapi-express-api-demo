from fastapi import FastAPI, Request, Response

app = FastAPI()

data = ["zero", "one", "two"]


@app.get("/tasks/{item_id}")
async def read_item(item_id: int, request: Request, response: Response):
    user_agent = request.headers.get("Authorization")
    return {"item": data[item_id]}


@app.get("/tasks")
async def read_item(request: Request, response: Response):
    return {"items": data}
