'''
Created on Feb 1, 2017

@author: zeus
'''
# get items from - http://docs.intrinio.com/tags/intrinio-public#data-point
import requests
import json
import re
#url='https://api.intrinio.com/companies?ticker=AAPL'
#url='https://api.intrinio.com/companies?'
#url='https://api.intrinio.com/data_point?identifier={GOOGL}&item={price_date}'

#gets tickers
url='https://api.intrinio.com/companies?'

username='7173f71ee9d7a0db67ab15aa149ab6c9'
password='e7baf09b41c222b9ccdbbb99f5fb1e23'
urlStr=requests.get(url,auth=(username,password)).content

#parsing the string
tickerJson=json.loads(urlStr);
#print(tickerJson)
dataAll=tickerJson['data']
tickerList=[]
for data in dataAll:
    tickerList.append(data['ticker'])

tickerList=["GOOGL","AMZN"]

#gets data
#url='https://api.intrinio.com/data_point?identifier={GOOGL}&item=price_date,close_price,percent_change'
counter=0;
for ticker in tickerList:
    url='https://api.intrinio.com/data_point?identifier={'+ticker+'}&item={close_price,bid_price}'
    urlStr=requests.get(url,auth=(username,password)).content
    companyJson=json.loads(urlStr);
    print companyJson
    if counter==1:
        break
    counter=counter+1
    