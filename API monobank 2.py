from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

currency_map = {"USD": 840, "EUR": 978, "JPY": 392}

@app.get("/")
def root():
    return {
        "message": "Сервіс працює! Дані про курси валют доступні на /rates"
    }

@app.get("/rates")
def get_rates():
    response = requests.get("https://api.monobank.ua/bank/currency")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Monobank API error")

    all_data = response.json()
    result = {}

    for item in all_data:
        code_a = item.get("currencyCodeA")
        code_b = item.get("currencyCodeB")

        for name, code in currency_map.items():
            if code_a == code and code_b == 980:
                result[name] = {
                    "rateBuy": item.get("rateBuy", "—"),
                    "rateSell": item.get("rateSell", "—")
                }

    return result
