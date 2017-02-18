'''
Created on Feb 4, 2017

@author: zeus
'''
import requests
import json
import re
from parser import get_article_from_url

#gets tickers
url='https://api.intrinio.com/companies?'

tickerList=[]
username='7173f71ee9d7a0db67ab15aa149ab6c9'
password='e7baf09b41c222b9ccdbbb99f5fb1e23'
urlStr=requests.get(url,auth=(username,password)).content
#for i in range(1,26):
#	url='https://api.intrinio.com/companies?page_number='+str(i)+'&'
#	urlStr=requests.get(url,auth=(username,password)).content
#	#parsing the string
#	tickerJson=json.loads(urlStr);
#	#print(tickerJson)
#	dataAll=tickerJson['data']
#	for data in dataAll:
#	    tickerList.append(data['ticker'])
#
#tickerList=[ "MMM","T","ADBE","AA","GOOG","AXP","AIG","AMT","AAPL","AMAT","BAC","CA","CAT","CVX","CSCO","C","KO","DD","EMC","XOM","FSLR","GE","GS","HPQ","HD","IBM","IP","INTC","JPM","JNJ","MCD","MRK","MSFT","PFE","PG","TRV","UTX","VZ","WMT","DISWFC","YAHOO"]
tickerList=["DISWFC","YAHOO"]

#gets data
#https://api.intrinio.com/companies/filings?identifier=AAPL&report_type=10-K&
#url='https://api.intrinio.com/data_point?identifier={GOOGL}&item=price_date,close_price,percent_change'
counter=0;
for ticker in tickerList:
    #f = open('../Data/Intrino_news/'+ticker+'.txt', 'w')
    url='https://api.intrinio.com/news?identifier='+ticker+''
    urlStr=requests.get(url,auth=(username,password)).content
    companyJson=json.loads(urlStr);
    articleJson = companyJson['data']
    i = 0
    for article in articleJson:
	f = open('../Data/Intrino_news/'+ticker+'_'+str(i)+'.txt', 'w')
	try:
		news = get_article_from_url(article['url'])
    		print article['url']
    		f.write(news)
		f.close()
		i = i+1
	except:
                print("Exception for " + ticker + " and url " + article['url'])
	if i==30:
	   break
    	#json.dump(companyJson,f)
    	#print article['url']
    	#print companyJson
    	#f.close()
    
