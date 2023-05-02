from hsk_levels import *


# This function iterates through a txt file of sentences and adds them to the
# appropriate txt files based on their level. About 15% of sentences meet criteria.
def add_hsk_sentences():
    sentence_file = "hsk_sentences.txt"

    with open(sentence_file, 'r', encoding='utf-8') as f:
        # Reads all the lines in the file into a list
        lines = f.readlines()

        for sentence in lines:
            if determine_hsk_level(sentence) == 1:
                with open('hsk_sentences/hsk1_sentences.txt', 'a') as w:  # Opens in append mode
                    w.write(sentence)
            elif determine_hsk_level(sentence) == 2:
                with open('hsk_sentences/hsk2_sentences.txt', 'a') as w:
                    w.write(sentence)
            elif determine_hsk_level(sentence) == 3:
                with open('hsk_sentences/hsk3_sentences.txt', 'a') as w:
                    w.write(sentence)
            elif determine_hsk_level(sentence) == 4:
                with open('hsk_sentences/hsk4_sentences.txt', 'a') as w:
                    w.write(sentence)
            elif determine_hsk_level(sentence) == 5:
                with open('hsk_sentences/hsk5_sentences.txt', 'a') as w:
                    w.write(sentence)
            elif determine_hsk_level(sentence) == 6:
                with open('hsk_sentences/hsk6_sentences.txt', 'a') as w:
                    w.write(sentence)
            elif determine_hsk_level(sentence) == 9:
                with open('hsk_sentences/hsk9_sentences.txt', 'a') as w:
                    w.write(sentence)
            else:
                continue


# This function counts how many sentences are currently in each hsk*_sentences txt file
def sentence_inventory_by_level():
    hsk_1 = "hsk_sentences/hsk1_sentences.txt"
    hsk_2 = "hsk_sentences/hsk2_sentences.txt"
    hsk_3 = "hsk_sentences/hsk3_sentences.txt"
    hsk_4 = "hsk_sentences/hsk4_sentences.txt"
    hsk_5 = "hsk_sentences/hsk5_sentences.txt"
    hsk_6 = "hsk_sentences/hsk6_sentences.txt"
    hsk_9 = "hsk_sentences/hsk9_sentences.txt"

    with open(hsk_1, 'r', encoding='utf-8') as hsk1:
        hsk1_num_sent = 0
        # Reads all the lines in the file into a list
        lines = hsk1.readlines()
        for sentence in lines:
            hsk1_num_sent += 1
    print(f"HSK 1 Sentences: {hsk1_num_sent}")

    with open(hsk_2, 'r', encoding='utf-8') as hsk2:
        hsk2_num_sent = 0
        # Reads all the lines in the file into a list
        lines = hsk2.readlines()
        for sentence in lines:
            hsk2_num_sent += 1
    print(f"HSK 2 Sentences: {hsk2_num_sent}")

    with open(hsk_3, 'r', encoding='utf-8') as hsk3:
        hsk3_num_sent = 0
        # Reads all the lines in the file into a list
        lines = hsk3.readlines()
        for sentence in lines:
            hsk3_num_sent += 1
    print(f"HSK 3 Sentences: {hsk3_num_sent}")

    with open(hsk_4, 'r', encoding='utf-8') as hsk4:
        hsk4_num_sent = 0
        # Reads all the lines in the file into a list
        lines = hsk4.readlines()
        for sentence in lines:
            hsk4_num_sent += 1
    print(f"HSK 4 Sentences: {hsk4_num_sent}")

    with open(hsk_5, 'r', encoding='utf-8') as hsk5:
        hsk5_num_sent = 0
        # Reads all the lines in the file into a list
        lines = hsk5.readlines()
        for sentence in lines:
            hsk5_num_sent += 1
    print(f"HSK 5 Sentences: {hsk5_num_sent}")

    with open(hsk_6, 'r', encoding='utf-8') as hsk6:
        hsk6_num_sent = 0
        # Reads all the lines in the file into a list
        lines = hsk6.readlines()
        for sentence in lines:
            hsk6_num_sent += 1
    print(f"HSK 6 Sentences: {hsk6_num_sent}")

    with open(hsk_9, 'r', encoding='utf-8') as hsk9:
        hsk9_num_sent = 0
        # Reads all the lines in the file into a list
        lines = hsk9.readlines()
        for sentence in lines:
            hsk9_num_sent += 1
    print(f"HSK 7-9 Sentences: {hsk9_num_sent}")

    print(f"Total Sentences: {hsk1_num_sent + hsk2_num_sent + hsk3_num_sent + hsk4_num_sent + hsk5_num_sent + hsk6_num_sent + hsk9_num_sent}")


# add_hsk_sentences()
sentence_inventory_by_level()