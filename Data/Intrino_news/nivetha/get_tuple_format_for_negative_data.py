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
        for words in sentence_parts:
            if words[0].isupper():
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
    print NegativeExampleExtractor.get_negative_markers("A B C D and N I V E T H A", 0, 0)
