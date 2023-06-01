from flask import Flask, render_template, request
from function_action import coinmarketcap_class_action
from CoinMarketCap import CoinMarketCapAPI
from CoinGecko import CoinGeckoAPI
import json


app = Flask(__name__)
@app.route('/')
def home():
    market_information = CoinMarketCapAPI.market_information()
    return render_template("home.html", market_information=market_information)


@app.route('/search', methods=["POST", "GET"])
def search():
    if request.method == "POST":
        user_cryptocurrency_input = request.form['user_cryptocurrency_input']
        coinmarketcap_class_output = coinmarketcap_class_action(user_cryptocurrency_input)

        cryptocurrency_information = coinmarketcap_class_output[0]
        cryptocurrency_metadata = coinmarketcap_class_output[1]
        coin_historical_data = coinmarketcap_class_output[2]
        if cryptocurrency_information is False or cryptocurrency_metadata is False or coin_historical_data is None:
            return render_template("home.html")
        else:
            return render_template("coin_data.html", cryptocurrency_information=cryptocurrency_information, cryptocurrency_metadata=cryptocurrency_metadata, coin_historical_data=coin_historical_data)
        
    elif request.method == "GET":
        user_cryptocurrency_input = request.args.get('user_cryptocurrency_input')
        coinmarketcap_class_output = coinmarketcap_class_action(user_cryptocurrency_input)

        cryptocurrency_information = coinmarketcap_class_output[0]
        cryptocurrency_metadata = coinmarketcap_class_output[1]
        coin_historical_data = coinmarketcap_class_output[2]

        return render_template("coin_data.html", cryptocurrency_information=cryptocurrency_information, cryptocurrency_metadata=cryptocurrency_metadata, coin_historical_data=coin_historical_data)


@app.route('/market_data')
def market_data():

    top_currency = CoinMarketCapAPI.top_cryptocurrency()
    trending_currency = CoinGeckoAPI.trending_currency()

    return render_template("market_data.html", top_currency=top_currency, trending_currency=trending_currency)


@app.route('/exchanges')
def exchanges():

    top_exchanges = CoinMarketCapAPI.top_exchanges_metadata()

    return render_template("exchanges.html", top_exchanges=top_exchanges)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
