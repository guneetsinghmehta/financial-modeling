'''
Created on Feb 6, 2017

@author: zeus
'''
#Saves list of tickers in a txt file tickerList.txt and also returns list of ticker Strings

import requests
import json
import re
#import getTickers
#Credentials
username='7173f71ee9d7a0db67ab15aa149ab6c9'
password='e7baf09b41c222b9ccdbbb99f5fb1e23'

#URLS
company_basic_info_url='https://api.intrinio.com/companies?identifier='
company_historical_data_url='https://api.intrinio.com/prices?ticker='


financial_statement_list=['income_statement','balance_sheet','cash_flow_statement','calculations','current']
quarter_list=['Q1','Q2','Q3',"Q4"]
year_list=['2010','2011','2012','2013','2014','2015','2016']

def get_company_data(ticker):
    f = open('trash.txt', 'w+')
    url=company_basic_info_url+ticker
    urlStr=requests.get(url,auth=(username,password)).content
    company_basic_info=json.loads(urlStr);
    json.dump(company_basic_info,f)
    #print company_basic_info
    
    url=company_historical_data_url+ticker
    urlStr=requests.get(url,auth=(username,password)).content
    company_historical_data=json.loads(urlStr);
    json.dump(company_historical_data,f)
    #print company_historical_data
    
    
    for financial_statement in financial_statement_list:
        print financial_statement
    
    f.close()
    
get_company_data("AAPL")
   