def likes(names):
    result = ""
    if(len(names) == 0):
        return("no one likes this")
    elif(len(names) == 1):
        return(names[0] + " likes this")
    elif(len(names)<4):
        result+=names[0]
        for i in range(1, len(names)-1):
            result+=", "
            result+=names[i]
        result+= " and "
        result+= names[len(names)-1]
        result+= " like this"
        return result       
    else:
        return(names[0] + ", " + names[1] + " and " + str(len(names)-2) + " others like this")    