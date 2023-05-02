from frequency import *
import random


def generate_hsk_1_sentence():
    # Opens the file containing the sentences
    with open("hsk_sentences/hsk1_sentences.txt", "r", encoding="utf-8") as f:
        # Read all the lines of the file into a list
        sentences = f.readlines()

    # Chooses a random sentence from the list
    random_sentence = random.choice(sentences)

    with open("hsk_vocab_lists/hsk1.txt", "r", encoding="utf-8") as f:
        # Read all the lines of the file into a list
        words = f.readlines()

    # Choose the correct answer
    correct_answer = find_lowest_freq_word(random_sentence)

    # Choose three additional answer options without repeats
    answer_options = [word.strip() for word in words if word.strip() != correct_answer]
    mult_choice_answers = random.sample(answer_options, k=3)
    mult_choice_answers.append(correct_answer)

    # Shuffle the answer options and print the sentence with choices
    random.shuffle(mult_choice_answers)
    print(replace_least_frequent_word(random_sentence))
    print(f"A. {mult_choice_answers[0]}\n"
          f"B. {mult_choice_answers[1]}\n"
          f"C. {mult_choice_answers[2]}\n"
          f"D. {mult_choice_answers[3]}\n")

    # Prompt the user for input
    user_choice = input("Enter the letter of the correct answer (A, B, C, or D): ")

    # Check the user's answer and give feedback
    if user_choice.upper() == "A" and mult_choice_answers[0] == correct_answer:
        print("Correct!")
    elif user_choice.upper() == "B" and mult_choice_answers[1] == correct_answer:
        print("Correct!")
    elif user_choice.upper() == "C" and mult_choice_answers[2] == correct_answer:
        print("Correct!")
    elif user_choice.upper() == "D" and mult_choice_answers[3] == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer was {correct_answer}.")



generate_hsk_1_sentence()

def generate_hsk_2_sentence():
    # Opens the file containing the sentences
    with open("hsk_sentences/hsk2_sentences.txt", "r", encoding="utf-8") as f:
        # Read all the lines of the file into a list
        sentences = f.readlines()

    # Chooses a random sentence from the list
    random_sentence = random.choice(sentences)

    # Prints the chosen sentence
    print(random_sentence)


def generate_hsk_3_sentence():
    # Opens the file containing the sentences
    with open("hsk_sentences/hsk3_sentences.txt", "r", encoding="utf-8") as f:
        # Read all the lines of the file into a list
        sentences = f.readlines()

    # Chooses a random sentence from the list
    random_sentence = random.choice(sentences)

    # Prints the chosen sentence
    print(random_sentence)


def generate_hsk_4_sentence():
    # Opens the file containing the sentences
    with open("hsk_sentences/hsk4_sentences.txt", "r", encoding="utf-8") as f:
        # Read all the lines of the file into a list
        sentences = f.readlines()

    # Chooses a random sentence from the list
    random_sentence = random.choice(sentences)

    # Prints the chosen sentence
    print(random_sentence)


def generate_hsk_5_sentence():
    # Opens the file containing the sentences
    with open("hsk_sentences/hsk5_sentences.txt", "r", encoding="utf-8") as f:
        # Read all the lines of the file into a list
        sentences = f.readlines()

    # Chooses a random sentence from the list
    random_sentence = random.choice(sentences)

    # Prints the chosen sentence
    print(random_sentence)


def generate_hsk_6_sentence():
    # Opens the file containing the sentences
    with open("hsk_sentences/hsk6_sentences.txt", "r", encoding="utf-8") as f:
        # Read all the lines of the file into a list
        sentences = f.readlines()

    # Chooses a random sentence from the list
    random_sentence = random.choice(sentences)

    # Prints the chosen sentence
    print(random_sentence)


def generate_hsk_9_sentence():
    # Opens the file containing the sentences
    with open("hsk_sentences/hsk9_sentences.txt", "r", encoding="utf-8") as f:
        # Read all the lines of the file into a list
        sentences = f.readlines()

    # Chooses a random sentence from the list
    random_sentence = random.choice(sentences)

    # Prints the chosen sentence
    print(random_sentence)


