class FeatureExtractorForCompany:
    occurences_so_far = 0
    def __init__(self):
        self.company = None

    def cleanup(self):
        self.occurences_so_far = 0

    # Checks if the company contains indicators
    # like inc, corp, etc
    def contains_relevant_indicators(self, name):
        indicators = ['inc', 'corp', 'corporation', 'capital']
        if name.endswith('.') or name.endswith('\''):
            name = name[:-1]
        for indicator in indicators:
            if name.endswith(indicator):
                return True
        return False

    # Count the number of times company indicators
    # had occured previously
    def count_previous_relevant_indicators(self):
        data = self.occurences_so_far
        self.occurences_so_far += 1
        return data

    # Eliminate indices like NASDAQ, DOW,
    def contains_index_indicators(self, name):
        return name.find('nasdaq') != -1 or name.find('dow') != -1 or name.find('s') != -1 and name.find('p') != -1 and name.find('500') != -1

    # Check if all first letters are capital
    def check_first_letters_capital(self, name):
        for word in name.split(' '):
            if len(word.strip()) != 0 and word[0].isalpha() and not word[0].isupper():
                return False
        return True

    # Check if digit is present in name
    def digit_present_in_name(self, name):
        for letter in name:
            if letter.isdigit():
                return True
        return False

    # Check if word contains symbols
    def contains_special_symbols(self, name):
        for letter in name:
            if not letter.isspace() and not letter.isalnum():
                return True
        return False

    def word_count(self, name):
        words = [x for x in name.split(' ') if len(x) > 0]
        return len(words)

    def get_dictionary(self, name):
        name = name.strip()
        name_lower = name.lower()
        self.company = dict()
        # self.company['company_name'] = name
        self.company['indicators_present'] = 1 if self.contains_relevant_indicators(name_lower) else 0
        # self.company['previous_indicator_occurence'] = self.count_previous_relevant_indicators()
        self.company['index_present'] = 1 if self.contains_index_indicators(name_lower) else 0
        self.company['capitalized_words'] = 1 if self.check_first_letters_capital(name) else 0
        self.company['digits_present'] = 1 if self.digit_present_in_name(name_lower) else 0
        self.company['special_symbols_present'] = 1 if self.contains_special_symbols(name_lower) else 0
        self.company['name_length'] = self.word_count(name_lower)
        return self.company

if __name__ == "__main__":
    feature_extractor = FeatureExtractorForCompany()
    print feature_extractor.get_dictionary("Microsoft")
