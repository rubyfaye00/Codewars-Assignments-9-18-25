#Pull Your Words Together Man!
#https://www.codewars.com/kata/59ad7d2e07157af687000070
#This code turns a list of words into a sentence.
#It capitalizes the first word, joins all the words, and adds a period at the end.
def sentencify(words):
    if not words:
        return ""
    
    words[0] = words[0].capitalize()

    sentence = ' '.join(words)

    sentence += '.'

    return sentence 

print(sentencify(["this", "is", "a", "sentence"]))
print(sentencify(["please", "help", "me"]))

print(sentencify(["dont", "look", "in", "the", "basement"]))
