def is_pangram(sentence):
    sentence= sentence.replace(' ','')
    splittedChar =  list(sentence)
    uniqueChar = set(splittedChar)
    return len(uniqueChar) >=  35
