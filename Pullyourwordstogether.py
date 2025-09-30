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