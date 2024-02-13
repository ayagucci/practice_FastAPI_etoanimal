from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    number: int


@app.post("/zodiac")
def double_number(item: Item):
    remainder = item.number % 12
    if remainder == 0:
        animal = "さる"
    elif remainder == 1:
        animal = "とり"
    elif remainder == 2:
        animal = "いぬ"
    elif remainder == 3:
        animal = "いのしし"
    elif remainder == 4:
        animal = "ねずみ"
    elif remainder == 5:
        animal = "うし"
    elif remainder == 6:
        animal = "とら"
    elif remainder == 7:
        animal = "うさぎ"
    elif remainder == 8:
        animal = "たつ"
    elif remainder == 9:
        animal = "へび"
    elif remainder == 10:
        animal = "うま"
    elif remainder == 11:
        animal = "ひつじ"    
    return {"result": animal}
