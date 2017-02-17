import urllib2, os
from time import sleep

class GenerateNews:
    def __init__(self):
        self.url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=e147a8c2c320498195db15b3f6a8c831&q="

    def get_url_json(self, ticker):
        url = self.url + ticker
        response = urllib2.urlopen(url)
        data = response.read()
        return data

def get_all_tickers():
    tickers = []
    with open("techTickers.txt", "r") as f:
        tickers = [x.strip() for x in f.readlines()]
    return tickers

def generate_json_news_tickers():
    news_generator = GenerateNews()
    tickers = get_all_tickers()
    if not os.path.exists("newsdata"):
        os.makedirs("newsdata")
    for ticker in tickers:
        with open("newsdata/" + ticker + ".json", "w") as f:
            f.write(str(news_generator.get_url_json(ticker)))
        sleep(5)

if __name__ == "__main__":
    generate_json_news_tickers()
