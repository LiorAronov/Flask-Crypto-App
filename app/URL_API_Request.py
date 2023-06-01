# Coin Market Cap - API Endpoints .
# Cryptocurrency Category.
cryptocurrency__id_map = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
cryptocurrency__metadata = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
cryptocurrency__listings = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
cryptocurrency__quotes = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

# Exchange Category.
exchange__id_map = 'https://pro-api.coinmarketcap.com/v1/exchange/map'
exchange__metadata = 'https://pro-api.coinmarketcap.com/v1/exchange/info'

# Global-Metrics Category.
globalmetrics__quotes = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'

# Tools Category.
tools__Price_Conversion = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'

# Fiat Category.
fiat__id_map = 'https://pro-api.coinmarketcap.com/v1/fiat/map'



# Coin Gecko - API Endpoints.
# Simple Category.
simple__price = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

# Trending Category.  
trending__coins  = "https://api.coingecko.com/api/v3/search/trending"

# Coins Category.  
coins__historical_data = 'https://api.coingecko.com/api/v3/coins/{currency_slug}/market_chart?vs_currency=usd&days=1'
coins__markets_data = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency={fiat_symbol}&ids={currency_slug}&sparkline=false&price_change_percentage=14d%2C200d&precision=18'

# NFT Category.  
nfts__list = 'https://api.coingecko.com/api/v3/nfts/list?order=market_cap_usd_desc&per_page=50'
nfts__metadata = 'https://api.coingecko.com/api/v3/nfts/{nft_id}'


# Companies Category.  
companies__list = 'https://api.coingecko.com/api/v3/companies/public_treasury/{btc_or_eth}'