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
    start_date_list=['2007-1-1','2012-1-1','2014-1-1','2015-1-1','2016-1-1','2017-1-1']
    end_date='2017-2-2'
    newpath = '../Data/yahoo_data_2/' + ticker
    for start_date in start_date_list:
        try:                
            company=Share(ticker)
            historical_data=company.get_historical(start_date,end_date)
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            fileHandle = open(newpath + '/data.json', 'wb')
            json.dump(historical_data, fileHandle)
            fileHandle.close()
            print ticker+" found"
            return
        except Exception as error:
            pass
            #print  ticker+" NOT found"
            #print  error
    print  ticker+" NOT found"
    
def runAll():
    #fileHandle=open('tickerList.txt','r')#contains list from Intrino
    fileHandle=open('NASDAQNYSEYahooFinanceTickers.txt','r')# contains 3200 list of companies from
    for line in fileHandle:
        ticker=line.strip()
        getCompanyDataYahoo(ticker)
        #print(ticker)
runAll()
   
