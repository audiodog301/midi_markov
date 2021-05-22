from random import choice, choices

#stores the text of a word/token and the quantities of the various words that occur after it in a given input.
class Word:
    def __init__(self, text):
        self.text = text
        self.after = {}

#counts those quantities properly
def train(text, separator):
    text = text.split(separator)
    words = {}
    
    for i in range(len(text)-1):
        #add the text of a word as a key and a new Word object as a value if the word isn't already in the dict
        if text[i] not in words.keys():
            words[text[i]] = Word(text[i])
        #for the word after the current word, if it isn't in the dictionary of possible after words, add it as occurring once so far
        if text[i+1] not in words[text[i]].after.keys():
            words[text[i]].after[text[i+1]] = 1
        #otherwise, just add to the already existing count of that word ocurring
        else:
            words[text[i]].after[text[i+1]] += 1
    
    return words

def find_chances(words):
    #this code is kind of a mess but it just does some math to replace quantity with likelihood (quantity of a given word divided by the quantity of all possible next words)
    for (text, obj) in words.items():
        num = 0
        for (word, count) in words[text].after.items():
            num += words[text].after[word]
        for (word, count) in words[text].after.items():
            words[text].after[word] /= num
    
    return words

def generate_out(words, amount):
    out = []
    #choose a random word to be first
    current = choice(list(words.values()))
    for i in range(amount):
        #add the current word to the output list
        out.append(current.text)
        #choose a new current word based on the probabilities of possible next words
        #i'm not actually sure that choosing based on probability works because i haven't tested properly, but i have no reason to assume it doesn't 
        current = words[choices(list(current.after.keys()), weights=current.after.values())[0]]
    return " ".join(out)

#this does the same as above except it saves state and only generates a new word when you ask for one
class Procedural:
    def __init__(self, words):
        self.words = words
        self.out = []
        self.current = choice(list(self.words.values()))
    def generate(self):
        self.out = self.current.text
        self.current = self.words[choices(list(self.current.after.keys()), weights=self.current.after.values())[0]]
        return self.out
        