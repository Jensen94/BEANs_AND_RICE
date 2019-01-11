#Track the increase and decrease of any provided ticker taken off Interface.py

import json
import time
import xlwt
from Robinhood import Robinhood
#from Interface import Interface

timeclock = 0
price = 0
transprice = 0
size = 0
hr = 3600
productid = ""

login_instance = Robinhood("JoelLawson93@gmail.com","slkAslk!9slkAslk!9")

hours = 1
tradeticker = "ETH"

#def hourtrack(hours, tradeticker):

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(0,0,"Second")
sheet1.write(0,1,"Price")
sheet1.write(0,2,"Execution")

while (timeclock < hr*hours):
		timeclock += 1
		productid = login_instance.quote_data(tradeticker)
		price = productid[0]['bid_price']
		#print productid[0]['bid_price']
		if (price > transprice):
#			print "Current price of " + tradeticker + " is $" + price + " HIGHER than last price $" + str(transprice) + " execute a BUY"
			sheet1.write(timeclock, 0, timeclock)
			sheet1.write(timeclock, 1, price)
			sheet1.write(timeclock, 2, "Buy")
		elif (price < transprice):
#			print "Current price of " + tradeticker + " is $" + price + " LOWER than last price $" + str(transprice) + " execute a SELL"
			sheet1.write(timeclock, 0, timeclock)
			sheet1.write(timeclock, 1, price)
			sheet1.write(timeclock, 2, "Sell")
		else:
#			print "Current price of " + tradeticker + " is $" + price + " NO CHANGE from last price $" + str(transprice) + ", HOLD"
			sheet1.write(timeclock, 0, timeclock)
			sheet1.write(timeclock, 1, price)
			sheet1.write(timeclock, 2, "Hold")
		
		transprice = price
		#print "Current price of " + tradeticker + " is $" + price
		time.sleep(1)
		
book.save('Track.xls')