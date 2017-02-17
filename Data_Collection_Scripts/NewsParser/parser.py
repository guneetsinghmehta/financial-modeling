from __future__ import print_function
from HTMLParser import HTMLParser
import urllib2
import sys
import os
from parse_and_extract_news import list_files_in_directory
reload(sys)
sys.setdefaultencoding('utf8')

class MyParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0
    self.data = []

  def handle_starttag(self, tag, attributes):
    if tag != 'p':
      return
    self.recording += 1

  def handle_endtag(self, tag):
    if tag == 'p' and self.recording:
      self.recording -= 1

  def handle_data(self, data):
    if self.recording:
      self.data.append(data.strip())

def get_article_from_url(url):
  response = urllib2.urlopen(url)
  page_source = response.read()
  parser = MyParser()
  parser.feed(page_source)
  data_str = ""
  for string in parser.data:
      data_str += " " + string
  data_str = [x.strip() for x in data_str.split(" ") if len(x.strip()) != 0]
  return " ".join(data_str)

def get_url_sets():
  if not os.path.exists("weburls"):
    print("Need to generate the urls!!!!!")
    return
  if not os.path.exists("newsarticles"):
    os.makedirs("newsarticles")
  files = list_files_in_directory("weburls")
  for file_name in files:
    ticker = file_name.split('.')[0]
    directory = "newsarticles/"+ticker
    if not os.path.exists(directory):
      os.makedirs(directory)
    with open(os.path.join("weburls", file_name), "r") as f:
        urls = [x.strip() for x in f.readlines()]
        counter = 0
        for url in urls:
            try:
                article = get_article_from_url(url)
                txt_file = directory + "/" + str(counter) + ".txt"
                written_file = open(txt_file, "w")
                print(article, file=written_file)
                counter += 1
            except:
                print("Exception for " + ticker + " and url " + url)

if __name__ == "__main__":
  get_url_sets()
