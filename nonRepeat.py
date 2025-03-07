def first_non_repeating_letter(s):
    for char in s:
          if s.lower().count(char.lower())<2:
               return char
    return ''
print(first_non_repeating_letter('sTreSS'))