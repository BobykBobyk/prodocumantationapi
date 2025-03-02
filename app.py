from fastapi import FastAPI, Query, Path
from typing import List, Optional

description = """
ChimichangApp API glory to Ukraine!. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **eating borsch** (_not implemented_).
* **listening old town road** (_not implemented_).
"""

app = FastAPI(title="Putinloh Zelenskiy top",
    description=description,
    summary="minecraft is my favorite game. 1.9.9.9 ßßß.",
    version="0.0.1",
    terms_of_service="http://github/BobykBobyk",
    contact={
        "name": "Breaking bad is amazing",
        "url": "http://spacex",
        "email": "castrop.wd@gmail.com",
    },
    license_info={
        "name": "Leopard",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get('/q/{items_id}', summary='Looking for objekt in List')
async def index(
        qu: Optional[List[str]] = Query(
            None,
            title='giving a query answer',
            description='List of queries for filter',
            alias='query',
            min_length=3,
            max_length=50,
            deprecated=False
        ),
        _id: int = Path(..., title='id of the element', description='PRIMARY_KEY=True', alias='item_id', gt=0)
):
    return {'query': qu, 'item_id': _id}


@app.get("/users/", tags=["users"])
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]


@app.get("/items/", tags=["items"])
async def get_items():
    return [{"name": "wand"}, {"name": "flying broom"}]
