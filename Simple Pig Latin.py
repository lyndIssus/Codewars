def pig_it(text):
    textlist = text.split(" ")
    result = ""
    for item in textlist:
        alpha = list(map(chr, range(ord('a'), ord('z')+1)))
        if any(letter in item.lower() for letter in alpha):
            item = item[1:len(item)] + item[0:1] + "ay"
            result+= " " + item
        else:
            result += " " + item    
    return result[1:]

print(pig_it('Pig latin is cool'))

