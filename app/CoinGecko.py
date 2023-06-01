import pycoingecko
import requests
import json
from URL_API_Request import simple__price, trending__coins, coins__historical_data, coins__markets_data, nfts__list, nfts__metadata, companies__list 

# CoinGeckoAPI Data Fetcher.
# Used for extra information that does not accessible from CoinMarketCapAPI.
# based on coin slug and fiat symbol ,from verify_currency_and_get_input_id function.
class CoinGeckoAPI:
    def __init__(self, currency_slug, fiat_symbol):
        self.currency_slug = currency_slug
        self.fiat_symbol = fiat_symbol


# Returns currency historical information, Use 'USD' and last 30 days as a default.
    def cryptocurrency_history(self):

        if (self.currency_slug is None) or (self.currency_slug is False):
            return False
        
        else:
            currency_slug = self.currency_slug[1]
            url_modify = (f"{coins__historical_data}".format(currency_slug=currency_slug))

            response = requests.get(url_modify)
            currency_history = response.json()

            return currency_history
        

# Returns addition cryptocurrencies Information based on user currency id and fiat symbol.
    def additional_currencies_information(self):

        if (self.currency_slug is None) or (self.currency_slug is False):
            return False
        
        fiat_symbol = (self.fiat_symbol[2]).lower()
        currency_slug =  self.currency_slug
        # currency_slug = 
     

        for item in currency_slug[1:]:
            currency_check = item.lower()
            url_modify = (f"{coins__markets_data}".format(currency_slug=currency_check, fiat_symbol=fiat_symbol))
            response = requests.get(url_modify)           
            data = response.json()

            if data ==  []:
                print ('empty')
                continue
            else:
                data = data[0]
                currency_info = {
                    'price_high_24h': data.get('high_24h'),
                    'price_low_24h': data.get('low_24h', 'N/A'),
                    'price_change_24h_usd': data.get('price_change_24h', 'N/A'),
                    'market_cap_change_24h_usd': data.get('market_cap_change_24h', 'N/A'),
                    'market_cap_change_24h_percent': data.get('market_cap_change_percentage_24h', 'N/A'),
                    'ath_price': data.get('ath', 'N/A'),
                    'ath_date': data.get('ath_date', 'N/A')[:10],
                    'ath_change_percent': data.get('ath_change_percentage', 'N/A'),
                    'atl_price': data.get('atl', 'N/A'),
                    'atl_date': data.get('atl_date', 'N/A')[:10],
                    'ath_change_percent': data.get('ath_change_percentage', 'N/A'),
                    'atl_change_percent': data.get('atl_change_percentage', 'N/A'),
                    'price_change_14d_percent': data.get('price_change_percentage_14d_in_currency', 'N/A'),
                    'price_change_200d_percent': data.get('price_change_percentage_200d_in_currency', 'N/A'),
                }
                
            return currency_info


# Returns currency price base on coin slug input.
    @staticmethod
    def simple_currency_price(simple_currency):
        response = requests.get(simple__price)
        data = response.json()
        currency_price = data[simple_currency]['usd']

        return currency_price
    

# Returns a list of the top 20 NFT Collection id, based on 24h volume.
    @staticmethod
    def top_nft_id():
        response = requests.get(nfts__list)
        data = response.json()

        top_nfts_id =[]

        for item in data:
            nfts_info = {}
            nfts_info['id'] = item['id']
            top_nfts_id.append(nfts_info)

        return top_nfts_id


# Returns all static metadata of all NFT id from top_nfts_id function. 
    @staticmethod
    def top_nft_metadata():

        top_nft_id = CoinGeckoAPI.top_nft_id() 

        top_nfts_data =[]

        for num, item in enumerate(top_nft_id):
            nft_id = str(item['id'])
            url_modify = (f"{nfts__metadata}".format(nft_id=nft_id))

            response = requests.get(url_modify)
            data = response.json()

            nft_info = {}
            nft_info['id'] = data['id']
            nft_info['name'] = data['name']
            nft_info['symbol'] = data['symbol']
            nft_info['logo'] = data['image']['small']
            nft_info['contract_address'] = data['contract_address']
            nft_info['Owners'] = data['number_of_unique_addresses']
            nft_info['Owners_change_24h_percent'] = data['number_of_unique_addresses_24h_percentage_change']
            nft_info['asset_platform_id'] = data['asset_platform_id']
            nft_info['native_currency'] = data['native_currency']
            nft_info['market_cap_native'] = data['market_cap']['native_currency']
            nft_info['market_cap_usd'] = data['market_cap']['usd']
            nft_info['total_supply'] = data['total_supply']
            nft_info['vol_24h'] = data['volume_24h']['usd']
            nft_info['vol_change_24h_usd_percent'] = data['volume_in_usd_24h_percentage_change']
            nft_info['floor_price_native'] = data['floor_price']['native_currency']
            nft_info['floor_price_usd'] = data['floor_price']['usd']
            nft_info['floor_price_change_24h_usd_percent'] = data['floor_price_in_usd_24h_percentage_change']
            nft_info['description'] = data['description']
            nft_info['website_url'] = data['links']['homepage']
            nft_info['twitter_url'] = data['links']['twitter']
            nft_info['discord_url'] = data['links']['discord']

            top_nfts_data.append(nft_info)

        return top_nfts_data


# Returns the top-7 trending coins on CoinGecko in the last 24 hours.
    @staticmethod
    def trending_currency():
        btc_price = CoinGeckoAPI.simple_currency_price('bitcoin') 

        response = requests.get(trending__coins)
        data = response.json()
        data_layer_1 = data['coins']

        top_7_trending = []
        
        for item in data_layer_1: 
            currency_info = {}
            currency_info['name'] = item['item']['name']
            currency_info['symbol'] = item['item']['symbol']
            currency_info['coin_rank'] = item['item']['market_cap_rank']
            currency_info['icon'] = item['item']["small"]

            price = item['item']["price_btc"] * btc_price
            if price >= 1.0: currency_info['price'] = "{:,.2f}".format(price) # Presents the price => 1 as 2f.
            elif price < 1.0 and price > 0.001: currency_info['price'] = "{:.3f}".format(price) # Presents the price > 0.001 as 3f.
            elif price < 0.001 and price > 0.00001: currency_info['price'] = "{:.5f}".format(price) # Presents the price > 0.00001 as 5f.
            else: # Produces 2 versions if price is > 0.00001.
                currency_info['price'] = "{:.11f}".format(price) # Presents the full price up to 14f.
                currency_info['short_price'] = "0.0..{}".format(str(currency_info['price'])[7:]) # Presents the price "0.0...{[7:11]}".
                # currency_info['short_price'] = "0.0...0{}".format(str(price)[7:11]) # Presents the price "0.0...0{[7:11]}".

            top_7_trending.append(currency_info)
        return top_7_trending


# Returns list of public companies that holdings bitcoin / ethereum.
    @staticmethod
    # def companies_holdings(btc_or_eth_user_input=None):
    def companies_holdings(btc_or_eth_user_input='bitcoin'):

        if (btc_or_eth_user_input =='bitcoin') or (btc_or_eth_user_input == 'ethereum'):
            url_modify = (f"{companies__list}".format(btc_or_eth=btc_or_eth_user_input))

            response = requests.get(url_modify)
            # response.raise_for_status()
            data = response.json()
            companies_data = []
    
            summary_company = {}
            summary_company['display_coin'] = btc_or_eth_user_input.capitalize()
            summary_company['summary_coin_holdings'] = data['total_holdings']
            summary_company['summary_holdings_usd'] = data['total_value_usd']
            summary_company['summary_market_cap_dominance'] = data['market_cap_dominance']

            for item in data['companies']:
                company_info = {}
                company_info['name'] = item['name']
                company_info['exchange_market'] = item['symbol'].split(':')[0]
                company_info['company_symbol'] = item['symbol'].split(':')[1]
                company_info['country'] = item['country']
                company_info['coin_holdings'] = item['total_holdings']
                company_info['holdings_usd'] = item['total_current_value_usd']
                company_info['avg_buy_usd'] = item['total_entry_value_usd']
                company_info['p/l_usd'] = ((company_info['holdings_usd']) - (company_info['avg_buy_usd']))                
                company_info['market_cap_dominance'] = item['percentage_of_total_supply']
                companies_data.append(company_info)

            companies_data.append(summary_company)
            return companies_data

        else:
            return False
