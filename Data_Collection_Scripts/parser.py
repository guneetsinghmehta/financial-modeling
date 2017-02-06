from HTMLParser import HTMLParser
import urllib2
import sys
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

if __name__ == "__main__":
  url = "https://techcrunch.com/2017/02/06/zenefits-names-jay-fulcher-as-new-ceo/"
  print get_article_from_url(url)
