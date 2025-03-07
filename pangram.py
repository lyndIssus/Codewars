import string


def is_pangram(st):
    
    alpha = list(map(chr, range(ord('a'), ord('z')+1)))
    if all(letter in st.lower() for letter in alpha):
        return True
    return False