from fastapi import FastAPI, Query
from stock.real_time import stock, index
from typing import List
import twstock

app = FastAPI()


@app.get("/stock")
def get_stock_data(code: str = Query(str)):
    return stock(code)


@app.get("/stock/multi")
def get_multi_stock_data(code: List[str] = Query([])):
    return stock(code)


@app.get('/stock/update')
def get_update():
    twstock.__update_codes()
    return {
        "status": True
    }

@app.get("/index")
def get_index_data():
    return index()
