'''
Created on Feb 6, 2017

@author: Neha Mittal
'''
import requests
import json
import re
from parser import get_article_from_url

#gets tickers
url='https://newsapi.org/v1/sources?language=en'

tickerList=[]

apiKey='bd086be1b4544053ad6948886bc06b73'

urlStr=requests.get(url).content

#parsing the string
tickerJson=json.loads(urlStr);

dataAll=tickerJson['sources']
for data in dataAll:
    tickerList.append(data['id'])


#gets data
for ticker in tickerList:
    url='https://newsapi.org/v1/articles?source='+ticker+'&sortBy=top&apiKey=bd086be1b4544053ad6948886bc06b73'
    urlStr=requests.get(url).content
    companyJson=json.loads(urlStr);
    articleJson = companyJson['articles']
    for article in articleJson:
	f = open('../Data/news_articles/'+str(companyJson['source'])+'_'+str(article['publishedAt'])+'.txt', 'w')
	news = get_article_from_url(article['url'])
    	f.write(news)
	f.close()
    
