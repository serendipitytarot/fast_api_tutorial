from typing import Union

from fastapi import FastAPI

import os

from dotenv import load_dotenv

import psycopg2

db_name = 'kris'
db_user = 'kris'
db_password = 'SJuALVOkZGDG8lqPsi8rVGU5AyQRuWNS'
db_host = 'dpg-cs1trb08fa8c73d4p4u0-a.oregon-postgres.render.com'
db_port = 5432

load_dotenv()

key = os.getenv("FAKE_VALUE")

app = FastAPI()

@app.get("/")
async def main():
    return {"message": key}
# def read_root():
#     return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q":q}

@app.get("/getdata/{location_name}")
def get_date(location_name: Union[str, None] = None):
    conn = psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )

    cur = conn.cursor()
    select_query = "select * from weather where city = '"+location_name+"' "
    cur.execute(select_query)
    records = cur.fetchall()
    conn.close()


    return {"city": records[0][1], "low": records[0][2], "high": records[0][3]}