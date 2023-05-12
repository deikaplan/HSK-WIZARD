# HSK-WIZARD
HSK WIZARD is a web app (in progress) that allows a user to choose their Chinese proficiency level (HSK level 1-9) to be quizzed on. The HSK WIZARD will then generate a Chinese sentence in that level, removing the least frequently used word. Four multiple choice answers will be generated below the sentence, prompting the user to select the word that best completes the sentence. This app utilizes the New HSK 3.0 vocabulary.

The **HSK_sentences** folder contains the lists of sentences sorted by their difficulty levels. 

The **HSK_vocab_lists** folder contains the vocabulary lists of the New HSK 3.0 exams, sorted by level.

**frequency.py** contains a function to find the word in a sentence with the lowest frequency use (based on Jieba library). It also contains a function that will replace the lowest frequency word in a sentence with a blank underscore.

**generate_sentence_by_level.py** contains functions that will generate a sentence by HSK level, remove the lowest frequency word, give multiple choice options, and ask the user to select the word that best fits the sentence. 

**hsk_levels.py** contains functions that take a Chinese sentence as input, breaks the sentence down into individual words (using Jieba library), and matches those words against individual HSK vocabulary lists to determine what percentage of the words are a match. If there is at least an 85% match, the function will check if the words match the next HSK level and by this method, the sentence is categorized into its appropriate HSK level.

**sentence_adder.py** takes a txt file of Chinese sentences as input, it will iterate through the sentences line by line and determine the HSK level of each sentence, writing the sentence to its appropriate file within the HSK_sentences folder.
