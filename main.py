import argparse
import requests
import json

URL = "http://api.exchangeratesapi.io/v1"
ENDPOINT = "latest"

class CurrencyChanger:
    def __init__(self, api_key, from_base = 'EUR', to_base = 'HUF') -> None:
        self.api_key = api_key

    def get_huf_currency(self):
        request = f"{URL}/{ENDPOINT}?access_key={self.api_key}&base=EUR"
        response = requests.get(request)
        current_huf_rate = dict(json.loads(response.content)).get('rates').get('HUF')
        return current_huf_rate

def main():
    api_key = ""
    parser = argparse.ArgumentParser(prog="EUR_to_HUF",
                                     description="Checks what is the current value of hungarian forint compared to euro.")
    parser.add_argument('-k', '--api-key', help="api-key for api.exchangeratesapi.io website", required=True)
    args = parser.parse_args()
    api_key = args.api_key
    cc = CurrencyChanger(api_key=api_key)
    current_huf_value_compared_to_euro = cc.get_huf_currency()
    print(f"1 EURO in HUF is: {current_huf_value_compared_to_euro}")


if __name__ == "__main__":
    main()

