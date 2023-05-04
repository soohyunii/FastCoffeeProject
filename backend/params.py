from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Params(BaseModel):
    now_stock: int
    order_stock: int
    store: str
