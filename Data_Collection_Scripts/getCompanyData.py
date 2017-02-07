'''
Created on Feb 6, 2017

@author: zeus
'''
# Saves list of tickers in a txt file tickerList.txt and also returns list of ticker Strings

import requests
import json
import re
import os

# import getTickers
# Credentials - Guneet
#username = '7173f71ee9d7a0db67ab15aa149ab6c9'
#password = 'e7baf09b41c222b9ccdbbb99f5fb1e23'

username = 'd30ad4040b16f8f390682f623ed8ab92'
password = '79be5cf07afffc316be02e4bc7609fe4'

# Credentials - Neha
#username = '140880a8f82720ec4c79184d48569637'
#password = '5cc95d190174dca7166f566994a9d3c6'

# URLS
url_dict = {
'prices': 'https://api.intrinio.com/prices?ticker='}
#'basic_info':'https://api.intrinio.com/companies?identifier=',
#'metrics':'https://api.intrinio.com/historical_data?ticker=',
#'statements':'https://api.intrinio.com/financials/standardized?identifier=',
#'news':'https://api.intrinio.com/news?ticker=',
#'news':'https://api.intrinio.com/news?ticker=',
company_basic_info_url = 'https://api.intrinio.com/companies?identifier='
company_historical_data_url = 'https://api.intrinio.com/prices?ticker='

statement_list = ['income_statement', 'balance_sheet', 'cash_flow_statement', 'calculations', 'current']
quarter_list = ['Q1', 'Q2', 'Q3', "Q4"]
#year_list = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']
year_list = [ '2016']
metrics_list=[]
    
def get_metric_list():
    f=open("metrics.csv",'r')
    list=[];
    for line in f:
        line=line.strip()
        list.append(line)
    return list
    
def get_company_data(ticker, saveBoolean):
    metrics_list=get_metric_list()
    # make a folder for each company
    newpath = '../Data/intrino_data/' + ticker
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    company_data = {}
    for key in url_dict:
        url = url_dict[key]
        print(key)
        if(key == 'basic_info' or key == 'prices'):
            url = url + ticker;
            urlStr = requests.get(url, auth=(username, password)).content
            try:
                data = json.loads(urlStr);
            except:
                data=None
            company_data[key] = data;
        elif(key=='news'):
            url = url + ticker;
            urlStr = requests.get(url, auth=(username, password)).content
            try:
                data = json.loads(urlStr);
            except:
                data=None
            company_data[key] = data;
        elif(key=='statements'):
            statement_data={}
            for statement in statement_list:
                for year in year_list:
                    for quarter in quarter_list:
                        url=url+ticker+'&statement='+statement+'&fiscal_period='+quarter+'&fiscal_year='+year
                        urlStr = requests.get(url, auth=(username, password)).content
                        try:
                            data = json.loads(urlStr);
                        except:
                            data=None
                        print(statement+year+quarter)
                        statement_data[statement+'-'+year+'-'+quarter]=data
            company_data[key]=statement_data
        elif(key=='metrics'):
            metric_data={}
            for metric in metrics_list:
                url = url + ticker +'&item='+metric;
                urlStr = requests.get(url, auth=(username, password)).content
                try:
                    data = json.loads(urlStr);
                except:
                    data=None
                metric_data[metric]=data;
            company_data[key] = metric_data;
    fileHandle = open(newpath + '/data.json', 'wb')
    json.dump(company_data, fileHandle)
    fileHandle.close()
    print(ticker+"done")        

def runAll():
    fileHandle=open('tickerList.txt','r')
    for line in fileHandle:
        ticker=line.strip()
        get_company_data(ticker,False)
        print(ticker)

runAll()
   
