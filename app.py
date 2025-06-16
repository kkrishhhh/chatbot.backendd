from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()

    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name'][0]

    print(source_currency)
    print(amount)
    print(target_currency)

    # Call the conversion function
    conversion_rate = fetch_conversion_factor(source_currency, target_currency)
    converted_amount = float(amount) * conversion_rate

    # Create and print final answer
    response_text = f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}"
    print(response_text)  # 👈 This will show in terminal

    return jsonify({
        "fulfillmentText": response_text
    })


def fetch_conversion_factor(source, target):
    url = f"https://api.currencyapi.com/v3/latest?apikey=cur_live_hT1yFzUywA6naAy14dikMyweED8vCRoM79ru4Veg&currencies={target}&base_currency={source}"
    response = requests.get(url)
    data = response.json()

    # Example API response: { 'data': { 'INR': { 'code': 'INR', 'value': 86.03 } } }
    return data['data'][target]['value']


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    data = request.get_json()

    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name'][0]

    print(source_currency)
    print(amount)
    print(target_currency)

    # Call the conversion function
    conversion_rate = fetch_conversion_factor(source_currency, target_currency)
    converted_amount = float(amount) * conversion_rate

    # Create and print final answer
    response_text = f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}"
    print(response_text)  # 👈 This will show in terminal

    return jsonify({
        "fulfillmentText": response_text
    })


def fetch_conversion_factor(source, target):
    url = f"https://api.currencyapi.com/v3/latest?apikey=cur_live_hT1yFzUywA6naAy14dikMyweED8vCRoM79ru4Veg&currencies={target}&base_currency={source}"
    response = requests.get(url)
    data = response.json()

    # Example API response: { 'data': { 'INR': { 'code': 'INR', 'value': 86.03 } } }
    return data['data'][target]['value']


if __name__ == '__main__':
    app.run(debug=True)
