import jieba


# This function finds the least frequently used word in a sentence
def find_lowest_freq_word(sentence):
    freq_file = "hsk_vocab_lists/hsk9.txt"
    # Load the frequency data from the file into a dictionary
    freq_dict = {}
    with open(freq_file, "r", encoding="utf-8") as f:
        for line in f:
            word, freq = line.strip().split()
            freq_dict[word] = int(freq)

    # Find the word in the sentence with the lowest frequency
    lowest_freq_word = None
    lowest_freq = float("inf")
    for word in jieba.cut(sentence):
        if word in freq_dict and freq_dict[word] < lowest_freq:
            lowest_freq_word = word
            lowest_freq = freq_dict[word]

    return lowest_freq_word


# This function replaces the least frequent word in a sentence with an underscore
def replace_least_frequent_word(sentence):
    least_frequent_word = find_lowest_freq_word(sentence)
    return sentence.replace(least_frequent_word, "___")


