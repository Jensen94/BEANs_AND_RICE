#Interface Code with Robinhood.py. Call upon functions within Robinhood.py in order to interface with the website
#and log in. This code will eventually connect with analysis tool in order to determine whether to buy or sell.

import json
from Robinhood import Robinhood

#Assigning Crypto Currencies we will be researching
Cryptos =  ["ETH","LTC","BCH","QTUM","BTG","NEO"]
Cryptos_name = ["Ethereum", "Litecoin", "Bitcoin Cash", "Qtum", "Bitcoin Gold", "NEO"]
Crypto_length = len(Cryptos)
Cryptos_price = ["None"] * Crypto_length
Crypto_DataFetch = [0] * Crypto_length

#Logging into Robinhood and initializin Crypto Currency searches

login_instance = Robinhood("username","password")

counter = 0
while counter < Crypto_length :
	#Crypto_DataFetch[counter] = login_instance.instruments(Cryptos[counter])
	#print Crypto_DataFetch[counter]
	Cryptos_price[counter] = login_instance.quote_data(Cryptos[counter])
	Cryptos_price_data = Cryptos_price[counter]
	#Crypto_DataFetch[counter] = json.loads(Cryptos_price[counter].text)
	#export1 = json.dumps(Crypto_DataFetch[counter], sort_keys=True, indent=4)
	print Cryptos_name[counter] +" "+ Cryptos_price_data[0]['bid_price']
	counter += 1
	#json.loads(requester1.text)
	#export1 = json.dumps(data1, sort_keys=True, indent=4)
#Printing function for information requested.
#counter = 0
#while counter < Crypto_length :
#	print Cryptos_name[counter] +" "+ str(Crypto_DataFetch[counter])
#	counter += 1