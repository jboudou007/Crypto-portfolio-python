
#Importing all the necessary dependencies
import csv
import numpy 
import pandas 
import requests
import math
import xlsxwriter

import requests
import csv
from secrets_2 import API_TOKEN

# CoinMarketCap API endpoint for retrieving top 50 coins by market cap
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Your CoinMarketCap API key

api_key = API_TOKEN

# Send GET request to CoinMarketCap API
params = {
    'start': '1',
    'limit': '50',
    'sort': 'market_cap',
    'sort_dir': 'desc'
}
headers = {'X-CMC_PRO_API_KEY': api_key}
response = requests.get(url, params=params, headers=headers)

# Parse JSON response
data = response.json()['data']

# Calculate total market cap
total_market_cap = sum([coin['quote']['USD']['market_cap'] for coin in data])

# Write data to CSV file
with open('top_50_coins.csv', mode='w') as csv_file:
    fieldnames = ['name', 'symbol', 'market_cap', 'price', 'percentage', 'number_of_coins_to_buy']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for coin in data:
        coin_market_cap = coin['quote']['USD']['market_cap']
        percentage = coin_market_cap / total_market_cap * 100
        coin_price = coin['quote']['USD']['price']
        number_of_coins_to_buy = (1000 * percentage) / coin_price
        writer.writerow({'name': coin['name'], 'symbol': coin['symbol'], 'market_cap': coin_market_cap, 'price': coin_price,'percentage': percentage, 'number_of_coins_to_buy': number_of_coins_to_buy})