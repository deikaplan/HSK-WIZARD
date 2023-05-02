import random
from hsk_levels import determine_hsk_level, calculate_word_match_percentage


# This function picks a random sentence from filename
def pick_random_sentence():
    filename = "hsk_sentences.txt"
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    random_line = random.choice(lines)
    sentence = random_line.split("\t")[0]
    return sentence


# This function checks how many sentences in the file fall into each HSK level
def check_sentences_per_hsk_level():
    hsk_1_sentences = 0
    hsk_2_sentences = 0
    hsk_3_sentences = 0
    hsk_4_sentences = 0
    hsk_5_sentences = 0
    hsk_6_sentences = 0
    hsk_9_sentences = 0

    sentence_file = "hsk_sentences.txt"
    with open(sentence_file, 'r', encoding='utf-8') as f:
        # Reads all the lines in the file into a list
        lines = f.readlines()
        # Chooses a random line from the list
        for line in lines:
            # Splits the line into its components (index, language code, sentence)
            sentence = line
            if determine_hsk_level(sentence) == 1:
                hsk_1_sentences += 1
            elif determine_hsk_level(sentence) == 2:
                hsk_2_sentences += 1
            elif determine_hsk_level(sentence) == 3:
                hsk_3_sentences += 1
            elif determine_hsk_level(sentence) == 4:
                hsk_4_sentences += 1
            elif determine_hsk_level(sentence) == 5:
                hsk_5_sentences += 1
            elif determine_hsk_level(sentence) == 6:
                hsk_6_sentences += 1
            elif determine_hsk_level(sentence) == 9:
                hsk_9_sentences += 1
            else:
                continue
    print(f"HSK 1 Sentences: {hsk_1_sentences} \n"
          f"HSK 2 Sentences: {hsk_2_sentences} \n"
          f"HSK 3 Sentences: {hsk_3_sentences} \n"
          f"HSK 4 Sentences: {hsk_4_sentences} \n"
          f"HSK 5 Sentences: {hsk_5_sentences} \n"
          f"HSK 6 Sentences: {hsk_6_sentences} \n"
          f"HSK 7-9 Sentences: {hsk_9_sentences} \n")


pick_random_sentence()
# check_sentences_per_hsk_level()