#get real time stock prices and prints it for 30 seconds
import time
import yahoo_finance
from yahoo_finance import Share
google=Share('GOOG')
apple=Share('AAPL')
for i in range(30):
	google.refresh()
	apple.refresh()
	print "google="+google.get_price()+" \tapple="+apple.get_price()
	time.sleep(1)

