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
	    # print("Word: ", words)
	    # print("Length: ", len(words))
	    if len(words) == 0:
		continue
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
    data = "XPS 13, and so on. Really honking laptops, like the 15-inch MacBook Pro, expect more wattage (85). This charger will work on those machinesjust not as fast. How do I love this thing? Let us count the ways. I keep one laptop charger my laptop bag, and one plugged in by the couch. So Ive been through the mill, trying to find just the right charging cord to be my spare. Since USB-C means that Im no longer locked into Apples proprietary chargers, Ive experimented with a Dell ($27, 30 watts) and a Udoli ($35, 45 watts), shown below. I knew both would take longer to charge than my MacBook Pros original charger (61 watts), but that didnt really matter for hotel-room purposes; theyd have overnight to charge. What I found, though, was that the Dell makes my laptop chime every few seconds, as though the cord is being unplugged and replugged. (Its probably not to spec, a buddy of mine guessesa hazard of the new, open USB-C world.) The Udoli works fine as long as the laptop is open  but when closed, it occasionally does that same chime. (I asked Anthony Sagneri, chief technology officer of FINsix, the Darts maker, about this chiming business. His suspicion: The Intel chipsets inside most laptops can draw large peak currents for short periods. But if the charger isnt designed for those surges, they can trip its overcurrent mode, cutting power; at that point, the charger re-negotiates its connection. In other wordsding!) But the Dart? No problems. Its small, gorgeous, lightweight (3 ounces!), fast, and chime-free. There are some footnotes. First, the prongs dont fold up, as they do on some chargers. And the Dart-C is back-ordered; the company says it has begun shipping, but new orders wont ship until next month. (Its worth noting that the actual Dart-Cthe brick itselfis identical to the original Dart charger, as first seen on Kickstarter. All thats new is the USB-C cable that plugs into it, which contains all the USB-C electronics and smarts. In fact, if you bought the original Dartthe one that comes with plug tips for a wide range of laptop modelsyou can get just the USB-C cable for it for $35.) Second, this charger costs $100, which is even more than Apples chargers ($70 and $80). Thats a drag. Im confident that in the new, open world of USB-C chargers, well have more compact, attractive, well-engineered options. For now, though, since this will be my one and only charger for all my gadgets, and since I travel a lot, and since space and weight are valued commodities in my laptop bag, Im going to bite the bullet. I have no problem saying it: The smallest laptop charger in the world is also one of the best. If youre a rabid USB-C nut like me, youll be in heaven. David Pogue, tech columnist for"
    print NegativeExampleExtractor.get_negative_markers(data, 0, 0)
