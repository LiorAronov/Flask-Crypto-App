from CoinMarketCap import CoinMarketCapAPI
from CoinGecko import CoinGeckoAPI
from MongoDB import MongoDB
# 
def coinmarketcap_class_action(user_cryptocurrency_input, user_fiatcurrencies_input=None):

    coinmarketcap_class = CoinMarketCapAPI(user_cryptocurrency_input, user_fiatcurrencies_input=None)

    cryptocurrency_information = coinmarketcap_class.cryptocurrency_information()
    cryptocurrency_metadata = coinmarketcap_class.cryptocurrency_metadata()

    coin_slug = coinmarketcap_class.verify_currency_and_get_input_id()
    fiat_symbol = coinmarketcap_class.verify_fiat_and_get_input_id()

    price_conversion = coinmarketcap_class.price_conversion(amount_convert=None)

    mongodb_class = MongoDB(cryptocurrency_information)
    coingecko_class = CoinGeckoAPI(coin_slug, fiat_symbol)

    coin_historical_data = coingecko_class.cryptocurrency_history()
    additional_cryptocurrency_information = coingecko_class.additional_currencies_information()

    return cryptocurrency_information, cryptocurrency_metadata, coin_historical_data, price_conversion, additional_cryptocurrency_information











    # top_currency = coinmarketcap_class.top_cryptocurrency()
