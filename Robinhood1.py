import requests
import urllib

class Robinhood1:

	endpoints = {
			"login": "https://api.robinhood.com/oauth2/token/",
			"investment_profile": "https://api.robinhood.com/user/investment_profile/",
			"accounts":"https://api.robinhood.com/accounts/",
			"ach_iav_auth":"https://api.robinhood.com/ach/iav/auth/",
			"ach_relationships":"https://api.robinhood.com/ach/relationships/",
			"ach_transfers":"https://api.robinhood.com/ach/transfers/",
			"applications":"https://api.robinhood.com/applications/",
			"dividends":"https://api.robinhood.com/dividends/",
			"edocuments":"https://api.robinhood.com/documents/",
			"instruments":"https://api.robinhood.com/instruments/",
			"margin_upgrades":"https://api.robinhood.com/margin/upgrades/",
			"markets":"https://api.robinhood.com/markets/",
			"notifications":"https://api.robinhood.com/notifications/",
			"orders":"https://api.robinhood.com/orders/",
			"password_reset":"https://api.robinhood.com/password_reset/request/",
			"quotes":"https://api.robinhood.com/marketdata/forex/quotes/",
			"document_requests":"https://api.robinhood.com/upload/document_requests/",
			"user":"https://api.robinhood.com/user/",
			"watchlists":"https://api.robinhood.com/watchlists/",
	}

	session = "None"

	username = "None"

	password = "None"

	headers = "None"

	auth_token = "None"

	account_url = "None"

	def __init__(self, username, password):
		self.session = requests.session()
		self.session.proxies = urllib.getproxies()
		self.username = username
		self.password = password
		self.grant_type = "password"
		self.client_id = "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS"
		self.headers = {
			"Accept": "*/*",
			"Accept-Encoding": "gzip, deflate",
			"Accept-Language": "en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5",
			"Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
			"X-Robinhood-API-Version": "1.0.0",
			"Connection": "keep-alive",
			"User-Agent": "Robinhood/823 (iPhone; iOS 7.1.2; Scale/2.00)"
		}
		
		self.session.headers = self.headers
		self.login()

		## set account url
		acc = self.get_account_number()
		self.account_url = self.endpoints['accounts'] + acc + "/"


	def login(self):
		data = "password=%s&username=%s&grant_type=%s&client_id=%s" % (self.password, self.username, self.grant_type, self.client_id)
		res = self.session.post(self.endpoints['login'], data=data)
		res = res.json()
		self.oauth_token = res['access_token']
		self.headers['Authorization'] = 'Bearer '+self.oauth_token

	def get_account_number(self):
		res = self.session.get(self.endpoints['ach_relationships'])
		res = res.json()['results'][0]
		account_number = res['account'].split('accounts/', 1)[1][:-1]
		print account_number
		return account_number

	def investment_profile(self):
		self.session.get(self.endpoints['investment_profile'])

	def instruments(self, stock):
		res = self.session.get(self.endpoints['instruments'], params={'query':stock.upper()})
		res = res.json()
		return res['results']

	def quote_data(self, stock, id):
		params = { 'symbols': stock }
		res = self.session.get(self.endpoints['quotes']+id, params=params)
		res = res.json()
		return res

	def place_order(self, instrument, quantity=1, bid_price = None, transaction=None):
		if bid_price == None:
			bid_price = self.quote_data(instrument['symbol'])[0]['bid_price']
		data = 'account=%s&instrument=%s&price=%f&quantity=%d&side=%s&symbol=%s&time_in_force=gfd&trigger=immediate&type=market' % (urllib.quote(self.account_url), urllib.unquote(instrument['url']), float(bid_price), quantity, transaction, instrument['symbol'])
		res = self.session.post(self.endpoints['orders'], data=data)
		return res

	def place_buy_order(self, instrument, quantity, bid_price=None):
		transaction = "buy"
		return self.place_order(instrument, quantity, bid_price, transaction)

	def place_sell_order(self, instrument, quantity, bid_price=None):
		transaction = "sell"
		return self.place_order(instrument, quantity, bid_price, transaction)
