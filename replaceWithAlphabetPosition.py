def alphabet_position(text):
    change = list(text)
    result = ''.join( [str(ord(word.lower()) - 96) + " " if word.isalpha() else "" for word in change])
    return result[0:len(result)-1]