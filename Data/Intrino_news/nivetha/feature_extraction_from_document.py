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
        self.document_with_tags = ""
        self.company_occurence = dict()

    def handle_starttag(self, tag, attrs):
        if tag == "strong":
            self.company_name_started = True
            self.document_with_tags += "<strong>"

    def handle_endtag(self, tag):
        if tag == "strong":
            self.company_name_started = False
            self.document_with_tags += "</strong>"

    def check_first_word(self):
        if len(self.document.strip()) == 0:
            return True
        if not self.document.strip()[-1].isalnum():
            return True
        return False

    def previous_indicators_occurred(self):
        if len(self.document_with_tags) > 100:
            str_of_interest = self.document_with_tags[-100:]
        else:
            str_of_interest = self.document_with_tags
        return str_of_interest.find("</strong>") != -1

    def handle_data(self, data):
        if self.company_name_started:
            data = data.strip()
            self.comapanies_occurred += 1
            company = self.feature_extractor.get_dictionary(data)
            company['first_word'] = 1 if self.check_first_word() else 0
            company['previous_indicator_occurence'] = 1 if self.previous_indicators_occurred() else 0
            company['starting_position'] = len(self.document)
            company['ending_position'] = len(self.document) + len(data)
            if not self.company_occurence.has_key(data.lower()):
                self.company_occurence[data.lower()] = 1
            else:
                self.company_occurence[data.lower()] += 1
            # self.company_occurence[data] = self.company_occurence[data] + 1 if not self.company_occurence.has_key(data) else 1
            self.company_col[len(self.document)] = (data, company)
            # self.document += data
        self.document += data
        self.document_with_tags += data

    def final_wraps(self, file_obj, file_name):
        for key,value in self.company_col.items():
            company_name, company = value
            company['occurence_count'] = self.company_occurence[company_name.lower()]
            company['document'] = file_name
            print(company, file=file_obj)

def get_dictionary_in_all_documents(source, destination):
    if not os.path.exists(source) or not os.path.isdir(source):
        print("The source folder doesn't exists!!!")
        return
    if not os.path.exists(destination):
        os.makedirs(destination)
    files = [x for x in os.listdir(source) if os.path.isfile(os.path.join(source,x))]
    for file_name in files:
        try:
            source_file = open(os.path.join(source, file_name), "r")
            dest_file = open(os.path.join(destination, file_name), "w")
            parser = DocumentFeatureExtractor()
            parser.feed("".join(source_file.readlines()))
            parser.final_wraps(dest_file, file_name)
            source_file.close()
            dest_file.close()
        except:
            print("Exception occurred while trying to parse: " + file_name)
        break



if __name__ == "__main__":
    get_dictionary_in_all_documents("done_files1", "dictionary_files")
