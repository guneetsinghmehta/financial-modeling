from __future__ import print_function
from HTMLParser import HTMLParser
import os

class MyHTMLParser(HTMLParser):
    string = ""
    def handle_starttag(self, tag, attrs):
        # print("Encountered a start tag: ", tag)
        if tag == "strong":
            self.string += "<strong>"

    def handle_endtag(self, tag):
        # print("Encountered end tag: ", tag)
        if tag == "strong":
            self.string += "</strong>"

    def handle_data(self, data):
        # print("Encountered some data: ", data)
        self.string = self.string + data

    def clean_space_in_data(self):
        self.string = " ".join([x for x in self.string.split(' ') if len(x) > 0])

def clean_files(folder_name):
    parser = MyHTMLParser()
    files = os.listdir(folder_name)
    for file_name in files:
        parser.string = ""
        with open(os.path.join(folder_name, file_name), "r") as f:
            lines = f.readlines()
            lines = "".join(lines)
            parser.feed(lines)
            # print(parser.string)
        parser.clean_space_in_data()
        with open(os.path.join(folder_name, file_name), "w") as f:
            print(parser.string, file=f)

if __name__ == "__main__":
    # parser.feed('adflkj <br/><p>This is a <strong>akdjf</strong></p>')
    # print parser.string
    clean_files("nivetha/done_files1")
