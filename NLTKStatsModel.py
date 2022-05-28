# Imports
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk import trigrams
from collections import defaultdict
import random


# Creating model and opening file
model = defaultdict(lambda: defaultdict(lambda: 0))
file = open("EAPStories.txt", 'r')


# Creating and cleaning up model
for line in file:
    for w1, w2, w3 in trigrams(line.lower().split(), pad_right=True, pad_left=True):
        model[(w1, w2)][w3] += 1

total_occurence = 0
for occurence in model['the', 'day'].values():
    total_occurence += occurence

for w1w2 in model:
    for w3 in model[w1w2]:
        model[w1w2][w3] = model[w1w2][w3] / total_occurence

# Will print model => dict(model['and', 'then'])


# Will create a sentence with the model
def create_sentence(word1, word2):
    sentence = [word1, word2]
    sentence_complete = False
    total_words = 0
    num_words = 2

    while not sentence_complete:
        min_words = random.random()

        for word in model[tuple(sentence[num_words - 2:])].keys():

            total_words += model[tuple(sentence[num_words - 2:])][word]

            if total_words >= min_words:
                sentence.append(word)
                num_words += 1
                break

        if sentence[num_words - 2:] == [None, None]:
            sentence_complete = True

    sentence_str = ""
    for word in sentence:
        if word != None:
            sentence_str = sentence_str + word + " "
    
    #print("create_sentence:", sentence_str)
    
    return sentence


# Will check how many syllables there are in a word
def syllable_checker(word):
    num_syllables = 0
    for index in range(0, len(word)):
        if word[index] in 'aeiouy':
            num_syllables += 1
            if index + 1 < len(word) and word[index + 1] in 'aeiouy':
                if index + 3 == len(word)-1 and word[-3:] == 'ing':
                    num_syllables += 1
                num_syllables -= 1
    if (word[-1:] in 'e' and num_syllables > 1) or word[-2:] == 'ed':
        num_syllables -= 1
    return num_syllables


# Will build the sentence in a string format
def build_sentence(sentence):
    sentence_str = ""
    for word in sentence:
        sentence_str = sentence_str + word + " "
    return sentence_str


# Used for debugging syllable output
def debug_print(syllables, sentence_str):
    syllable_debug = str(sum(syllables)) + " " + str(syllables)
    #print(f'{str(syllables):<18}', sum(syllables), "|", sentence_str)


# Creating the haiku
haiku_created = False

while not haiku_created:
    sentence = create_sentence("and", "how")
    sentence = sentence[0:len(sentence) - 2]
    #print("sentence:", sentence)

    syllables = []
    index = 0

    for word in sentence:
        syllables.append(syllable_checker(word))
        index += 1

    #print("sylables:", syllables)
    
    if sum(syllables) < 17:
        continue
    
    first_sentence = []
    second_sentence = []
    third_sentence = []
    
    index = 0
    num_syllables = 0
    for word in sentence:
        #print("sylable_num:", num_syllables)
        if num_syllables >= 5:
            break
        elif num_syllables < 5:
            first_sentence.append(word)
            num_syllables += syllables[index]
            index += 1
            
    if num_syllables > 5:
        continue
    
    
    num_syllables = 0
    for i in range (index, len(sentence)):
        if num_syllables >= 7:
            break
        elif num_syllables < 7:
            second_sentence.append(sentence[i])
            num_syllables += syllables[index]
            index += 1
    
    if num_syllables > 7:
        continue
            
    num_syllables = 0
    for i in range (index, len(sentence)):
        if num_syllables >= 5:
            haiku_created = True
            break
        elif num_syllables < 5:
            third_sentence.append(sentence[i])
            num_syllables += syllables[index]
            index += 1
            
    if num_syllables > 5:
        continue

    first_sentence_str, second_sentence_str, third_sentence_str = build_sentence(first_sentence), build_sentence(second_sentence), build_sentence(third_sentence)

    first_syllables = syllables[:len(first_sentence)]
    second_syllables = syllables[len(first_sentence):len(first_sentence + second_sentence)]
    third_syllables = syllables[len(first_sentence + second_sentence):len(first_sentence + second_sentence + third_sentence)]

    #debug_print(first_syllables, first_sentence_str)
    #debug_print(second_syllables, second_sentence_str)
    #debug_print(third_syllables, third_sentence_str)

    print(first_sentence_str)
    print(second_sentence_str)
    print(third_sentence_str)

