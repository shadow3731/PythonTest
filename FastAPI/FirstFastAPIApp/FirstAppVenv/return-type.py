from fastapi import FastAPI, Response
from pydantic import BaseModel, EmailStr
from fastapi.responses import RedirectResponse, JSONResponse

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
    
class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):
    password: str


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> any:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]
    
# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn) -> any:
#     return user

@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user

@app.get('/teleport')
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]