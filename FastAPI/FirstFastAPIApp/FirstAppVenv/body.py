from typing import Annotated

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title='Item description', max_length=300
    )
    price: float = Field(
        gt=0, description='Must be greater than 0'
    )
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None
    
class User(BaseModel):
    username: str
    full_name: str | None = None


# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: str | None = None,
#     item: Item | None = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results

@app.put("/items/{item_id}")
async def update_item(
    item_id: int, 
    user: User, 
    importance: Annotated[int, Body()],
    item: Item = Body(embed=True)
):
    results = {"item_id": item_id, "item": item, "user": user, 'importance': importance}
    return results

@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images