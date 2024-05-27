from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None, 
#         Query(min_lenght=3, max_length=50, pattern='^fixedquery$')
#     ] = None
# ):
#     results = {
#         "items": [
#             {"item_id": "Foo"}, 
#             {"item_id": "Bar"},
#         ]
#     }
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(min_length=3)] = ...
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: Annotated[list[str], None, Query()] = None):
#     query_items = {"q": q}
#     return query_items

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, 
        Query(
            title="Query string", 
            min_length=3,
            description='Query string for the items to search in the database',
            alias='item_query',
            deprecated=True,
        )
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results