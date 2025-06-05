import requests


def get_selected_currency_rates():
    url = "https://api.monobank.ua/bank/currency"

    # код валют
    currency_map = {
        840: 'USD',  # долар
        978: 'EUR',  # євро
        392: 'JPY',  # єна
        980: 'UAH'
    }

    selected_codes = [840, 978, 392]

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("Курси валют до гривні (UAH):\n")

        for currency in data:
            code_a = currency['currencyCodeA']
            code_b = currency['currencyCodeB']

            if code_b == 980 and code_a in selected_codes:
                name = currency_map.get(code_a, str(code_a))
                rate_buy = currency.get('rateBuy')
                rate_sell = currency.get('rateSell')
                rate_cross = currency.get('rateCross')

                if rate_buy and rate_sell:
                    print(f"{name} → UAH | Купівля: {rate_buy} | Продаж: {rate_sell}")
                elif rate_cross:
                    print(f"{name} → UAH | Крос-курс: {rate_cross}")
                else:
                    print(f"{name} → UAH | Немає даних")

    except requests.RequestException as e:
        print(f"Помилка при запиті: {e}")


get_selected_currency_rates()
