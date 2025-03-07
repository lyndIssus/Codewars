def spin_words(sentence):
    change = sentence.split(" ")
    return ' '.join( [word[::-1] if len(word)>4 else word for word in change])