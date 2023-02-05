from typing import Union, Optional
from fastapi import FastAPI, Header, Response, Cookie
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    decricao: str
    valor: float


app = FastAPI()


@app.get("/")
def read_root(user: Optional[str] = Header("123")):
    return {"user-agent": user}


@app.get("/cookie")
def cookie(response: Response):
    response.set_cookie(key="meu_cookie", value="12345678")
    return {"cookie": True}


@app.get("/get-cookie")
def get_cookie(meu_cookie: Optional[str] = Cookie(None)):
    return {"Cookie": meu_cookie}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/item")
def add_item(novo_item: Item, outro_item: Item):
    return [novo_item, outro_item]
