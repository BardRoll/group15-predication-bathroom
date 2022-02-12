from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
import datetime

from pymongo import MongoClient

app = FastAPI()

client = MongoClient('mongodb://localhost', 27017)
db = client["Bathroom"]
menu_collection = db['menu06']


class Menu(BaseModel):
    number: str
    available: bool
    start_time: str  # iso datetime format: 2020-07-10 15:00:00.000
    end_time: str
