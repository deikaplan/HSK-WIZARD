import jieba
from frequency import *

hsk1 = "hsk_vocab_lists/hsk1.txt"
hsk2 = "hsk_vocab_lists/hsk2.txt"
hsk3 = "hsk_vocab_lists/hsk3.txt"
hsk4 = "hsk_vocab_lists/hsk4.txt"
hsk5 = "hsk_vocab_lists/hsk5.txt"
hsk6 = "hsk_vocab_lists/hsk6.txt"
hsk9 = "hsk_vocab_lists/hsk9.txt"


# Calculates the % of the input sentence that can be found in the vocab list (filename)
def calculate_word_match_percentage(input_sentence, filename):

    # Open the text file and read its contents into a list of lines
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Sets the hsk9.txt file as the jieba dictionary
    jieba.set_dictionary("hsk_vocab_lists/hsk9.txt")

    # Tokenizes the input sentence into a list of words using the jieba library
    input_words = jieba.cut(input_sentence, cut_all=False)

    # Calculate the number of words in the input sentence that appear in the text file
    unique_words_in_input = set()
    matched_words = set()

    # Count the number of unique words in the input and add them to the set
    for word in input_words:
        # Skip "," or "." symbols that are being counted as words
        if word == "，" or word == "," or word == "。" or word == ".":
            continue
        unique_words_in_input.add(word)

    # Count the number of input words matched in the dictionary
    for line in lines:
        for word in unique_words_in_input:
            if word in line:
                matched_words.add(word)
                break

    # Calculate the percentage of words in the input sentence that appear in the text file
    percentage_matched = round(((len(matched_words))/(len(unique_words_in_input)) * 100), 2)
    return percentage_matched


# At least 85% of the words in the sentence must be found in the corresponding hsk vocab list
def determine_hsk_level(sentence):
    if calculate_word_match_percentage(sentence, hsk1) >= 85:
        return 1
    elif calculate_word_match_percentage(sentence, hsk2) >= 85:
        return 2
    elif calculate_word_match_percentage(sentence, hsk3) >= 85:
        return 3
    elif calculate_word_match_percentage(sentence, hsk4) >= 85:
        return 4
    elif calculate_word_match_percentage(sentence, hsk5) >= 85:
        return 5
    elif calculate_word_match_percentage(sentence, hsk6) >= 85:
        return 6
    elif calculate_word_match_percentage(sentence, hsk9) >= 85:
        return 9
    else:
        return None
