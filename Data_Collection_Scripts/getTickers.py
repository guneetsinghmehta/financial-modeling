'''
Created on Feb 6, 2017

@author: zeus
'''
#Saves list of tickers in a txt file tickerList.txt and also returns list of ticker Strings

import requests
import json
import re

#Credentials
username='7173f71ee9d7a0db67ab15aa149ab6c9'
password='e7baf09b41c222b9ccdbbb99f5fb1e23'

def getTickers():
    f = open('../Data/tickerList.txt', 'w+')
    tickerList=[]
    #there are 26 pages of tickers
    for page_number in range(1,27):
        url='https://api.intrinio.com/companies?page_number='+str(page_number)
        urlStr=requests.get(url,auth=(username,password)).content
        #parsing the string
        tickerJson=json.loads(urlStr);
        dataAll=tickerJson['data']
        for data in dataAll:
            tickerList.append(data['ticker'])
            #print(data['ticker'])
            f.write(data['ticker']+'\n')
    f.close()    
    return tickerList

getTickers()
   
