'''
Created on Feb 7, 2017

@author: zeus
'''
#https://pypi.python.org/pypi/yahoo-finance
from yahoo_finance import Share
import time
import os
import json

def getCompanyDataYahoo(ticker):
    start_date='2007-1-1'
    end_date='2017-1-1'
    newpath = '../Data/yahoo_data/' + ticker
    try:                
        company=Share(ticker)
        historical_data=company.get_historical(start_date,end_date)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        fileHandle = open(newpath + '/data.json', 'wb')
        json.dump(historical_data, fileHandle)
        fileHandle.close()
        print ticker+" found"
    except Exception as error:
        print  ticker+" NOT found"
        print  error
    
def runAll():
    fileHandle=open('tickerList.txt','r')#contains list from Intrino
    #fileHandle=open('tickerListYahoo.txt','r')# contains 3200 list of companies from
    for line in fileHandle:
        ticker=line.strip()
        getCompanyDataYahoo(ticker)
        #print(ticker)
runAll()
   
