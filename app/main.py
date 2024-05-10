from fastapi import FastAPI, Query
from stock.real_time import stock, index
from typing import List

app = FastAPI()


@app.get("/stock")
def get_stock_data(code: str = Query(str)):
    return stock(code)


@app.get("/stock/multi")
def get_multi_stock_data(code: List[str] = Query([])):
    return stock(code)


@app.get("/index")
def get_index_data():
    return index()
