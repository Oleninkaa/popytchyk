from pydantic import BaseModel
import datetime

class Trips(BaseModel):
    name:str
    surname:str
    phone:str
    email:str
    start:str
    finish:str
    date:str
    comment:str = None


 