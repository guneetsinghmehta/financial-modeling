class NegativeExampleExtractor():
    @staticmethod
    def get_negative_markers(sentence, word_length, words_processed):
        if sentence == None or len(sentence) == 0:
            return None
        sentence_parts = sentence.split(' ')
        # print("Sentence parts:")
        # print(sentence_parts)
        word_lens = word_length
        continuous_word_list = []
        word_list_to_process = False
        negative_markers = []
        no_of_words_processed = words_processed
        filter_list = NegativeExampleExtractor.get_filter_word_list()
        for words in sentence_parts:
	    # print("Word: ", words)
	    # print("Length: ", len(words))
            if len(words) == 0:
                continue
            if words[0].isupper() and not NegativeExampleExtractor.should_filter(words, filter_list):
                continuous_word_list.append(words)
                word_list_to_process = True
            else:
                if word_list_to_process:
                    negative_markers.extend(NegativeExampleExtractor.process_word_list(continuous_word_list, word_lens, no_of_words_processed))
                    word_list_to_process = False
                    no_of_words_processed += len(continuous_word_list)
                    word_lens += sum([len(x) for x in continuous_word_list])
                    continuous_word_list = []
                word_lens += len(words)
                no_of_words_processed += 1
        if word_list_to_process:
            negative_markers.extend(NegativeExampleExtractor.process_word_list(continuous_word_list, word_lens, no_of_words_processed))
        return negative_markers

    @staticmethod
    def should_filter(words, filter_list):
        filter_list = set(['the', 'editors', 'capital', 'trump', 'ajo,', 'lp', 'alzheimers', 'university'])
        # return False
        # should filter the words present in the filter list
        if words.lower().strip() in filter_list:
            return True
        return False
        # remove if the word length is less than 3
        if len(words.strip()) < 3:
            return True
        # return False
        # # remove if the words are all caps
        for letter in words:
            if letter.isalpha() and letter.islower():
                return False
        return True

    @staticmethod
    def get_filter_word_list():
        filter_list = None
        with open("filter_list.txt", "r") as f:
            lines = f.readlines()
            lines = ",".join(lines)
            filter_list = [ x.strip().lower() for x in lines.split(',') if len(x.strip()) > 0 ]
        filter_list = set(filter_list)
        # print filter_list
        return filter_list

    @staticmethod
    def process_word_list(word_list, word_lens, no_of_words_processed):
        if len(word_list) <= 4 :
            combinations = NegativeExampleExtractor.get_combinations_end(word_list, word_lens, no_of_words_processed)
            return combinations
        negative_markers = []
        for i in range(len(word_list)-4+1):
            curr_word_group = []
            for j in range(4):
                curr_word_group.append(word_list[i+j])
            combinations = None
            # print(curr_word_group, word_lens, no_of_words_processed)
            if i+4 != len(word_list):
                combinations = NegativeExampleExtractor.get_combinations(curr_word_group, word_lens, no_of_words_processed)
            else:
                combinations = NegativeExampleExtractor.get_combinations_end(curr_word_group, word_lens, no_of_words_processed)
            negative_markers.extend(combinations)
            word_lens += len(word_list[i])
            no_of_words_processed += 1
        return negative_markers

    @staticmethod
    def get_combinations(word_group, word_len, no_of_words_processed):
        combinations = []
        curr_list = []
        for i in range(len(word_group)):
            curr_list.append(word_group[i])
            # print curr_list
            combinations.append({
            'curr_list': list(curr_list),
            'starting_position': word_len + no_of_words_processed,
            'ending_position': word_len + no_of_words_processed + NegativeExampleExtractor.get_words_len(curr_list) + len(curr_list) - 1
            })
        return combinations

    @staticmethod
    def get_combinations_end(word_group, word_len, no_of_words_processed):
        combinations = []
        for i in range(len(word_group)):
            curr_list = []
            for j in range(i,len(word_group)):
                curr_list.append(word_group[j])
            # print("curr_list", curr_list)
            combinations.extend(NegativeExampleExtractor.get_combinations(curr_list, word_len, no_of_words_processed))
            word_len += len(word_group[i])
            no_of_words_processed += 1
        return combinations

    @staticmethod
    def get_words_len(curr_list):
        return sum([len(x) for x in curr_list])

if __name__ == "__main__":
    words = ['A', 'B', 'C', 'D', 'E']
    # print NegativeExampleExtractor.get_combinations(words, 0, 0)
    # print NegativeExampleExtractor.get_combinations_end(words, 0, 0)
    # print NegativeExampleExtractor.process_word_list(words, 0, 0)
    data = "This is a Nivetha example. The example should work."
    print NegativeExampleExtractor.get_negative_markers(data, 0, 0)
