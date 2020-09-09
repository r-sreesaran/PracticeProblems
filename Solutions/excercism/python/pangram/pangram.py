import re

def is_pangram(sentence):
    sentence = re.sub('[^A-Za-z]+', '', sentence)
    sentence= sentence.replace(' ','').lower()
    splittedChar =  list(sentence)
    uniqueChar = set(splittedChar)
    return len(uniqueChar) >=  26


def is_pangram(sentence):
    sent = sentence.lower()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabets:
        if letter not in sent:
            return False
    return True