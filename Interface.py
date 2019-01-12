#Interface Code with Robinhood.py. Call upon functions within Robinhood.py in order to interface with the website
#and log in. This code will eventually connect with analysis tool in order to determine whether to buy or sell.

import json
import sys
import gspread
import xlwt
import time
import oauth2client.service_account
#import ServiceAccountCredentials
from Robinhood1 import Robinhood1

#Interface class calls upon Robinhood to log in and initalize session while pulling cryptos of interest to buy and
#sell.
class Interface:

	#Assigning Crypto Currencies we will be researching
	Cryptos =  ["ETHUSD","LTCUSD","BCHUSD","BTCUSD","DOGE"]
	id = ["76637d50-c702-4ed1-bcb5-5b0732a81f48/","383280b1-ff53-43fc-9c84-f01afd0989cd/","2f2b77c4-e426-4271-ae49-18d5cb296d3a/",
		  "3d961844-d360-45fc-989b-f6fca761d511/","1ef78e1b-049b-4f12-90e5-555dcf2fe204/"]
	Cryptos_name = ["Ethereum", "Litecoin", "Bitcoin Cash","Bitcoin","Dogecoin",]
	Crypto_length = len(Cryptos)
	Cryptos_price = ["None"] * Crypto_length
	hours = 1
	hr = 25
	sheet = [None] *Crypto_length
	transprice = [0] * Crypto_length
	timeclock = 0
	counter = 0

	#Logging into Robinhood
	def __init__(self):
		username = raw_input("Please enter Robinhood username: ")
		password = raw_input("Please enter Robinhood password: ")
		self.login_instance = Robinhood1(username,password)
		self.xls_write()

	#Fetch crypto prices of irest
	def crypto_price(self, counter):
		self.Cryptos_price[counter] = self.login_instance.quote_data(self.Cryptos[counter],self.id[counter])
		Cryptos_price_data = self.Cryptos_price[counter]
		return Cryptos_price_data['bid_price']

	def xls_write(self):
		#Headers for XLS Sheets
		self.counter = 0
		while self.counter < self.Crypto_length :
			book = xlwt.Workbook(encoding="utf-8")
			self.sheet[self.counter] = book.add_sheet(self.Cryptos[self.counter])
			self.sheet[self.counter].write(0,0,"Second")
			self.sheet[self.counter].write(0,1,"Price")
			self.sheet[self.counter].write(0,2,"Execution")
			self.counter += 1
		open
		#Print Cyrpto Information in Initialized document
		self.counter = 0
		while self.timeclock < self.hr * self.hours :
			self.timeclock += 1
			print self.timeclock
			self.counter = 0
			while self.counter < self.Crypto_length :
				price = self.crypto_price(self.counter)
				print self.Cryptos[self.counter]+str(price)
				self.sheet[self.counter].write(self.timeclock, 0, self.timeclock)
				self.sheet[self.counter].write(self.timeclock, 1, price)
				if (price > self.transprice[self.counter]) :
					self.sheet[self.counter].write(self.timeclock, 2, "BUY")
				elif (price < self.transprice[self.counter]) :
					self.sheet[self.counter].write(self.timeclock, 2, "SELL")
				else :
					self.sheet[self.counter].write(self.timeclock, 2, "HOLD")
				self.transprice[self.counter] = price
				self.counter += 1
		book.save('Track.xls')

	# def xls_xport(self):
		#Opening Google Sheets
		# self.scope = ['https://spreadsheets.google.com/feeds']
		# self.creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
		# self.client = gspread.authorize(creds)

		#push data from track.py to google spreadsheet for analysis
		# self.sheet = client.open("CryptoAnalysis").sheet1
		# new_row = sheet.row)count +1
		# sheet.update_cell(new_row,1,track.tradeticker)
		# sheet.update_cell(new_row,2,track.price)
		# sheet.update_cell(new_row,3,track.timeclock)
		
		

		