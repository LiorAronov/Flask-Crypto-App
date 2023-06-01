from requests import Request, Session
import json
from keys.Keys import CoinMarketCap_API_KEY
from URL_API_Request import cryptocurrency__id_map, cryptocurrency__quotes, cryptocurrency__metadata, fiat__id_map, tools__Price_Conversion, globalmetrics__quotes, cryptocurrency__listings, exchange__id_map, exchange__metadata

# API Connection To CoinMarketCap.
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': CoinMarketCap_API_KEY
  }

session = Session()
session.headers.update(headers)

# CoinMarketCapAPI Data Fetcher.
class CoinMarketCapAPI:
    def __init__(self, user_cryptocurrency_input, user_fiatcurrencies_input=None):
        self.user_cryptocurrency_input = user_cryptocurrency_input
        self.user_fiatcurrencies_input = user_fiatcurrencies_input

        self.verify_user_cryptocurrency = self.verify_currency_and_get_input_id()
        self.verify_user_fiatcurrencies = self.verify_fiat_and_get_input_id()


# Verify the user currency input(id/name/symbol/slug), and return the currency id.
    def verify_currency_and_get_input_id(self):

        response = session.get(cryptocurrency__id_map)
        data = response.json()
        data_layer_1 = data['data']

        if self.user_cryptocurrency_input is None:
            return None
        
        elif self.user_cryptocurrency_input:
            user_cryptocurrency_input = self.user_cryptocurrency_input.strip().lower()
            for item in data_layer_1:
                if (str(item['id']) == user_cryptocurrency_input
                    or item['name'].lower() == user_cryptocurrency_input
                    or item['symbol'].lower() == user_cryptocurrency_input
                    or item['slug'].lower() == user_cryptocurrency_input):
                    return item['id'] ,item['slug'], item['name'], item['symbol']
        return False 


# Verify the user fiat input(id/name/sign/symbol/code), and return the fiat id.
    def verify_fiat_and_get_input_id(self):

        parameters = {
            'include_metals': 'true'} 

        response = session.get(fiat__id_map, params=parameters)
        # data = json.loads(response.text)
        data = response.json()
        data_layer_1 = data['data']

        if self.user_fiatcurrencies_input is None:
            return (2781,'United States Dollar', 'USD', '$')
        
        elif self.user_fiatcurrencies_input:
            user_fiatcurrencies_input = self.user_fiatcurrencies_input.strip().lower()    
            for item in data_layer_1:
                if (str(item['id']) == user_fiatcurrencies_input
                    or item['name'].lower() == user_fiatcurrencies_input
                    or item['symbol'].lower() == user_fiatcurrencies_input
                    or 'sign' in item and item['sign'].lower() == user_fiatcurrencies_input
                    or 'code' in item and item['code'].lower() == user_fiatcurrencies_input):
                    return item['id'], item['name'], item['symbol'], item['sign']
                 
        return  (2781,'United States Dollar', 'USD', '$')


# Returns the latest cryptocurrencies Information based on user currency id.
    def cryptocurrency_information(self):

        if (self.verify_user_cryptocurrency is None) or (self.verify_user_cryptocurrency is False):
            return  False                 
        else:
            coin_id = str(self.verify_user_cryptocurrency[0])
            fiat_id = str(self.verify_user_fiatcurrencies[0])

            parameters = {
                'id': coin_id,
                'convert_id': fiat_id}
            
            response = session.get(cryptocurrency__quotes, params=parameters)
            data = response.json()
            data_layer_2 = data['data'][coin_id]

            currency_info = {}
            currency_info['id'] = data_layer_2['id']
            currency_info['name'] = data_layer_2["name"]
            currency_info['symbol'] = data_layer_2["symbol"]
            currency_info['slug'] = data_layer_2["slug"]
            currency_info['market_rank'] = data_layer_2['cmc_rank']
            currency_info['circulating_supply'] = '{:,.1f}'.format(data_layer_2['circulating_supply'])
            currency_info['total_supply'] = '{:,.0f}'.format(data_layer_2['total_supply']) if data_layer_2['total_supply'] else 'N/A'
            currency_info['max_supply'] = '{:,.0f}'.format(data_layer_2['max_supply']) if data_layer_2['max_supply'] else 'N/A'
            currency_info['market_cap'] = '{:,.0f}'.format(data_layer_2['quote'][fiat_id]['market_cap'])
            currency_info['dominance_percent'] = '{:,.0f}'.format(data_layer_2['quote'][fiat_id]['market_cap_dominance'])
            currency_info['vol_24h'] = '{:,.0f}'.format(data_layer_2['quote'][fiat_id]['volume_24h']) 

            currency_info['vol_change_24h'] = '{:,.1f}'.format(data_layer_2['quote'][fiat_id]['volume_change_24h']) #####
            
            currency_info['price_change_1h_percent'] = '{:,.1f}'.format(data_layer_2['quote'][fiat_id]['percent_change_1h']) 
            currency_info['price_change_24h_percent'] = '{:,.1f}'.format(data_layer_2['quote'][fiat_id]['percent_change_24h']) 
            currency_info['price_change_7d_percent'] = '{:,.1f}'.format(data_layer_2['quote'][fiat_id]['percent_change_7d']) 
            currency_info['price_change_30d_percent'] = '{:,.1f}'.format(data_layer_2['quote'][fiat_id]['percent_change_30d'])

            price = data_layer_2["quote"][fiat_id]["price"]
            if price >= 1.0: currency_info['price'] = "{:,.2f}".format(price) # Presents the price => 1 as 2f.
            elif price < 1.0 and price > 0.001: currency_info['price'] = "{:.3f}".format(price) # Presents the price > 0.001 as 3f.
            elif price < 0.001 and price > 0.00001: currency_info['price'] = "{:.5f}".format(price) # Presents the price > 0.00001 as 5f.
            else: # Produces 2 versions if price is > 0.00001.
                currency_info['price'] = "{:.11f}".format(price) # Presents the full price up to 14f.
                currency_info['short_price'] = "0.0..{}".format(str(currency_info['price'])[7:]) # Presents the price "0.0...{[7:11]}".

            return currency_info


# Returns cryptocurrencies static metadata Information, based on user currency id.
    def cryptocurrency_metadata(self):

        if (self.verify_user_cryptocurrency is None) or (self.verify_user_cryptocurrency is False):
            return  False   
        else:
            coin_id = str(self.verify_user_cryptocurrency[0])

            parameters = {
                'id': coin_id}

            response = session.get(cryptocurrency__metadata, params=parameters)
            data = response.json()
            data_layer_2 = data['data'][coin_id]
            
            # currency_data = []
            currency_info = {}
            currency_info['website_url'] = data_layer_2['urls']['website'] if data_layer_2['urls']['website'] else 'N/A'
            currency_info['whitepaper_url'] = data_layer_2['urls']["technical_doc"] if data_layer_2['urls']['technical_doc'] else 'N/A'
            currency_info['source_code_url'] = data_layer_2['urls']["source_code"] if data_layer_2['urls']['source_code'] else 'N/A'
            currency_info['coin_twitter_url'] = data_layer_2['urls']["twitter"] if data_layer_2['urls']['twitter'] else 'N/A'
            currency_info['coin_reddit_url'] = data_layer_2['urls']['reddit'] if data_layer_2['urls']['reddit'] else 'N/A'
            currency_info['logo'] = data_layer_2['logo'] if data_layer_2['logo'] else 'N/A'
            currency_info['description'] = data_layer_2['description'] if data_layer_2['date_launched'] else 'N/A'
            currency_info['date_launched'] = data_layer_2['date_launched'][:10] if data_layer_2['date_launched'] else 'N/A'

            return currency_info
        

# Convert cryptocurrency to fiat
    def price_conversion(self,amount_convert=None):

        if (amount_convert is None) or (not isinstance(amount_convert, (int, float))) or (self.verify_user_cryptocurrency[0] is None):
            return False

        else:
            coin_id = str(self.verify_user_cryptocurrency[0])
            fiat_id = str(self.verify_user_fiatcurrencies[0])

            parameters = {
                'amount': amount_convert,
                'id': coin_id,
                'convert_id': fiat_id}
                
            response = session.get(tools__Price_Conversion,  params=parameters)
            data = response.json()
            data_layer_1 = data['data']

            convert_data = []
            convert_info = {}
            convert_info['currency_id'] = data_layer_1['id']
            convert_info['currency_name'] = data_layer_1['name']
            convert_info['currency_symbol'] = data_layer_1['symbol']
            convert_info['currency_amount_convert'] = "{:.2f}".format(data_layer_1['amount'])

            price = data_layer_1["quote"][fiat_id]["price"]
            if price >= 1.0: convert_info['convert_fiat'] = "{:,.2f}".format(price) # Presents the price => 1 as 2f.
            elif price < 1.0 and price > 0.001: convert_info['convert_fiat'] = "{:.3f}".format(price) # Presents the price > 0.001 as 3f.
            elif price < 0.001 and price > 0.00001: convert_info['convert_fiat'] = "{:.5f}".format(price) # Presents the price > 0.00001 as 5f.
            else: # Produces 2 versions if price is > 0.00001.
                convert_info['convert_fiat'] = "{:.11f}".format(price) # Presents the full price up to 14f.
                convert_info['short_convert_fiat'] = "0.0..{}".format(str(convert_info['convert_fiat'])[7:]) # Presents the price "0.0...{[7:11]}".
                
            convert_data.append(convert_info)
        return convert_data 
    

# Returns the latest global cryptocurrency market Information. Use 'USD' as a default  option.
    @staticmethod
    def market_information():

        parameters = {
            'convert_id': '2781'}  # USD ID 
            
        response = session.get(globalmetrics__quotes, params=parameters)
        data = response.json()
        data_layer_1 = data['data']

        market_data = []
        market_info = {}
        market_info['btc_dominance'] = '{:,.1f}'.format(data_layer_1['btc_dominance'])
        market_info['eth_dominance'] = '{:,.1f}'.format(data_layer_1['eth_dominance'])
        market_info['active_cryptocurrencies'] = '{:,.0f}'.format(data_layer_1['active_cryptocurrencies'])
        market_info['active_exchanges'] = '{:,.0f}'.format(data_layer_1['active_exchanges'])
        market_info['market_cap'] = '{:,.0f}'.format(data_layer_1['quote']['2781']['total_market_cap'])
        market_info['vol_24h'] = '{:,.0f}'.format(data_layer_1['quote']['2781']['total_volume_24h'])
        market_info['defi_market_cap'] = '{:,.0f}'.format(data_layer_1['quote']['2781']['defi_market_cap'])
        market_info['defi_vol_24h'] = '{:,.0f}'.format(data_layer_1['quote']['2781']['defi_volume_24h'])
        market_info['stablecoin_market_cap'] = '{:,.0f}'.format(data_layer_1['quote']['2781']['stablecoin_market_cap'])
        market_info['stablecoin_vol_24h'] = '{:,.0f}'.format(data_layer_1['quote']['2781']['stablecoin_volume_24h'])

        market_data.append(market_info)       
        return market_data
    
    
# Returns a list of the top 40 cryptocurrency information, based on market cap.
    @staticmethod
    def top_cryptocurrency():

        parameters = {
            'start': '1',
            'limit': '40'}
            
        response = session.get(cryptocurrency__listings, params=parameters)
        data = response.json() 
        data_layer_1 = data['data']

        top_currency = []

        for item in data_layer_1:
            currency_info = {}
            currency_info['id'] = item['id']
            currency_info['coin_rank'] = item['cmc_rank']
            currency_info['name'] = item["name"]
            currency_info['symbol'] = item["symbol"]
            currency_info['slug'] = item["slug"]
            currency_info['circulating_supply'] = "{:,.0f}".format(item["circulating_supply"])
            currency_info['total_supply'] = "{:,.0f}".format(item["total_supply"])
            currency_info['max_supply'] = "{:,.0f}".format(item["max_supply"]) if item["max_supply"] else 'N/A'
            currency_info['vol_24h'] = "{:,.0f}".format(item["quote"]["USD"]["volume_24h"]) if item["quote"]["USD"]["volume_24h"] else 'N/A'
            currency_info['vol_change_24h'] = "{:,.1f}".format(item["quote"]["USD"]["volume_change_24h"]) if item["quote"]["USD"]["volume_change_24h"] else 'N/A'
            currency_info['price_change_1h_percent'] = "{:,.1f}".format(item["quote"]["USD"]["percent_change_1h"]) if item["quote"]["USD"]["percent_change_1h"] else 'N/A'
            currency_info['price_change_24h_percent'] = "{:,.1f}".format(item["quote"]["USD"]["percent_change_24h"]) if item ["quote"]["USD"]["percent_change_24h"] else 'N/A'
            currency_info['market_cap'] = "{:,.0f}".format(item["quote"]["USD"]["market_cap"]) 
            currency_info['dominance_percent'] = "{:,.1f}".format(item["quote"]["USD"]["market_cap_dominance"])

            # currency_info['price'] = "{:,.3f}".format(item["quote"]["USD"]["price"])
            price = item["quote"]["USD"]["price"]
            if price >= 1.0: currency_info['price'] = "{:,.2f}".format(price) # Presents the price => 1 as 2f.
            elif price < 1.0 and price > 0.001: currency_info['price'] = "{:.3f}".format(price) # Presents the price > 0.001 as 3f.
            elif price < 0.001 and price > 0.00001: currency_info['price'] = "{:.5f}".format(price) # Presents the price > 0.00001 as 5f.
            else: # Produces 2 versions if price is > 0.00001.
                currency_info['price'] = "{:.11f}".format(price) # Presents the full price up to 14f.
                currency_info['short_price'] = "0.0..{}".format(str(currency_info['price'])[7:]) # Presents the price "0.0...0{[7:11]}".

            top_currency.append(currency_info)
        return top_currency


# Returns a list of the top 20 cryptocurrency exchanges id, based on 24h volume.
    @staticmethod
    def top_exchanges_id():

        parameters = {
            'start': '1',
            'limit': '20',  
            'sort': 'volume_24h'}
            
        response = session.get(exchange__id_map, params=parameters)
        data = response.json() 
        data_layer_1 = data['data']

        top_exchanges_id =[]

        for item in data_layer_1:
            exchanges_info = {}
            exchanges_info['id'] = item['id']
            top_exchanges_id.append(exchanges_info)

        return top_exchanges_id


# Returns all static metadata of all cryptocurrency exchanges id from top_exchanges_id function. 
    @staticmethod
    def top_exchanges_metadata():

        top_exchanges_id = CoinMarketCapAPI.top_exchanges_id()
        top_exchanges_data = []

        for num, item in enumerate(top_exchanges_id):
            exchange_id = str(item['id'])
            parameters = {
                'id': exchange_id}
            
            response = session.get(exchange__metadata, params=parameters)
            data = response.json()
            data_layer_2 = data['data'][exchange_id]

            exchanges_info = {}
            exchanges_info['id'] = data_layer_2['id']
            exchanges_info['name'] = data_layer_2['name']
            exchanges_info['slug'] = data_layer_2['slug']
            exchanges_info['logo'] = data_layer_2['logo']
            exchanges_info['description'] = data_layer_2['description']
            exchanges_info['date_launched'] = data_layer_2['date_launched'][:10] 
            exchanges_info['website_url'] = data_layer_2['urls']['website']
            exchanges_info['twitter_url'] = data_layer_2['urls']['twitter']
            exchanges_info['fees_url'] = data_layer_2['urls']['fee']
            exchanges_info['maker_fees'] = data_layer_2['maker_fee']
            exchanges_info['taker_fees'] = data_layer_2['taker_fee']
            exchanges_info['weekly_visits'] = "{:,.0f}".format(data_layer_2['weekly_visits'])
            exchanges_info['spot_volume_24h'] = "{:,.0f}".format(data_layer_2['spot_volume_usd']) if data_layer_2["spot_volume_usd"] else 'N/A'

            top_exchanges_data.append(exchanges_info)
 
        return top_exchanges_data