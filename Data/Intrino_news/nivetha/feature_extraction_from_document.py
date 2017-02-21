from __future__ import print_function
from HTMLParser import HTMLParser
import os
from markup_feature_extraction import FeatureExtractorForCompany

class DocumentFeatureExtractor(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.comapanies_occurred = 0
        self.company_name_started = False
        self.feature_extractor = FeatureExtractorForCompany()
        self.company_col = dict()
        self.document = ""
        self.company_occurence = dict()

    def handle_starttag(self, tag, attrs):
        # print("Tag: ", tag)
        if tag == "strong":
            self.company_name_started = True

    def handle_endtag(self, tag):
        # print("End tag: ", tag)
        if tag == "strong":
            self.company_name_started = False

    def check_first_word(self):
        if len(self.document.strip()) == 0:
            return True
        if not self.document.strip()[-1].isalnum:
            return True
        return False

    def handle_data(self, data):
        print("Data: ", data)
        if self.company_name_started:
            data = data.strip()
            self.comapanies_occurred += 1
            company = self.feature_extractor.get_dictionary(data)
            company['first_word'] = 1 if self.check_first_word() else 0
            self.company_occurence[data] = self.company_occurence[data] + 1 if self.company_occurence.has_key(data) else 0
            self.company_col[len(self.document)] = (data, company)
            # self.document += data
        self.document += data

    def final_wraps(self):
        print(type(self.company_col))
        for key,value in self.company_col.items():
            company_name, company = value
            company['occured_multiple_times'] = 1 if self.company_occurence[company_name] > 1 else 0
            print(company_name)
            print(company)
        print(self.document)

def get_dictionary_in_all_documents(source, destination):
    if not os.path.exits(source) or not os.path.isdir(source):
        print("The source folder doesn't exists!!!")
        return
    if not os.path.exists(destination):
        os.makedirs(destination)
    files = [x for x in os.listdir(source) if os.path.isfile(os.path.join(source,x))]
    # for file_name in files:


if __name__ == "__main__":
    parser = DocumentFeatureExtractor()
    parser.feed("This is a <strong>Microsoft</strong> document. <strong>Apple</strong> is also in this document.")
    parser.final_wraps()
