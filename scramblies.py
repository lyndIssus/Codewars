def scramble(s1, s2):
    return all(s1.count(letter) >= s2.count(letter) for letter in list(set(s2)))
print(scramble('rkqodlw', 'world'))
