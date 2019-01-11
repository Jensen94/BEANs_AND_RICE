#Interface Code with Robinhood.py. Call upon functions within Robinhood.py in order to interface with the website
#and log in. This code will eventually connect with analysis tool in order to determine whether to buy or sell.

import json
import sys
from Robinhood import Robinhood

#Interface class calls upon Robinhood to log in and initalize session while pulling cryptos of interest to buy and
#sell.
class Interface:

	#Assigning Crypto Currencies we will be researching
	Cryptos =  ["ETH","LTC","BCH","QTUM","BTG","NEO"]
	Cryptos_name = ["Ethereum", "Litecoin", "Bitcoin Cash", "Qtum", "Bitcoin Gold", "NEO"]
	Crypto_length = len(Cryptos)
	Cryptos_price = ["None"] * Crypto_length
	Crypto_DataFetch = [0] * Crypto_length

	#Logging into Robinhood
	def __init__(self):
		username = raw_input("Please enter Robinhood username: ")
		password = raw_input("Please enter Robinhood password: ")
		self.login_instance = Robinhood(username,password)
		self.crypto_price()

	#Fetch crypto prices of irest
	def crypto_price(self):
		counter = 0
		while counter < self.Crypto_length :
			#Crypto_DataFetch[counter] = login_instance.instruments(Cryptos[counter])
			#print Crypto_DataFetch[counter]
			self.Cryptos_price[counter] = self.login_instance.quote_data(self.Cryptos[counter])
			Cryptos_price_data = self.Cryptos_price[counter]
			print self.Cryptos_name[counter] +" "+ Cryptos_price_data[0]['bid_price']
			counter += 1
			#Crypto_DataFetch[counter] = json.loads(Cryptos_price[counter].text)
			#export1 = json.dumps(Crypto_DataFetch[counter], sort_keys=True, indent=4)
			#json.loads(requester1.text)
			#export1 = json.dumps(data1, sort_keys=True, indent=4)