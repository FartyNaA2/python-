from fastapi import FastAPI, Query, HTTPException
from typing import List
import requests

app = FastAPI()

currency_map = {"USD": 840, "EUR": 978, "JPY": 392}

@app.get("/")
def root():
    return {"message": "Сервіс працює! Щоб отримати курси валют, зверніться до /rates"}

@app.get("/rates")
def get_rates(
    currencies: List[str] = Query(..., description="Валюти для перевірки")
):
    response = requests.get("https://api.monobank.ua/bank/currency")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Monobank API error")

    all_data = response.json()
    result = {}

    for item in all_data:
        code_a = item.get("currencyCodeA")
        code_b = item.get("currencyCodeB")
        for name, code in currency_map.items():
            if code_a == code and code_b == 980 and name in currencies:
                result[name] = {
                    "rateBuy": item.get("rateBuy", "—"),
                    "rateSell": item.get("rateSell", "—")
                }

    return result
