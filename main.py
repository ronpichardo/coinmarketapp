import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, sys

with open('config.json') as json_data:
	config = json.load(json_data)
	if config['apikey'] != '':
		coin_api_key = config['apikey']
	else:
		print('Please update config with coinmarketcap apikey.  Sign up is required at coinmarketcap.com')
		sys.exit()

s = requests.Session()
headers = {
	'Accept': 'application/json',
	'X-CMC_PRO_API_KEY': coin_api_key
}
s.headers.update(headers)

main_url = 'https://pro-api.coinmarketcap.com'

latest_api_route = '/v1/cryptocurrency/listings/latest'

url = main_url + latest_api_route

data = {
	'start':'1',
	'limit':'10',
	'convert':'USD'
}

try:
	res = s.get(url, params=data)
	data = res.json()['data']

	for coin in config['symbol']:
		for crypto in data:
			rank = crypto['id']
			name = crypto['name']
			symbol = crypto['symbol'].lower()
			price = crypto['quote']['USD']['price']
			formattedPrice = format(price, '.3f')
			if symbol == coin:
				print(f'{rank} : {name}({symbol}) - {formattedPrice}')

except (ConnectionError, Timeout, TooManyRedirects) as e:
	print('Exception: %s' % e)



'''
Example Response from API
{
	"data": [{
		"id": 1,
		"name": "Bitcoin",
		"symbol": "BTC",
		"slug": "bitcoin",
		"cmc_rank": 5,
		"num_market_pairs": 500,
		"circulating_supply": 16950100,
		"total_supply": 16950100,
		"max_supply": 21000000,
		"last_updated": "2018-06-02T22:51:28.209Z",
		"date_added": "2013-04-28T00:00:00.000Z",
		"tags": [
			"mineable"
		],
		"platform": null,
		"quote": {
			"USD": {
				"price": 9283.92,
				"volume_24h": 7155680000,
				"percent_change_1h": -0.152774,
				"percent_change_24h": 0.518894,
				"percent_change_7d": 0.986573,
				"market_cap": 158055024432,
				"last_updated": "2018-08-09T22:53:32.000Z"
			},
			"BTC": {
				"price": 1,
				"volume_24h": 772012,
				"percent_change_1h": 0,
				"percent_change_24h": 0,
				"percent_change_7d": 0,
				"market_cap": 17024600,
				"last_updated": "2018-08-09T22:53:32.000Z"
			}
		}
	}],
	"status": {
		"timestamp": "2018-06-02T22:51:28.209Z",
		"error_code": 0,
		"error_message": "",
		"elapsed": 10,
		"credit_count": 1
	}
}'''
