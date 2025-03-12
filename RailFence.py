def encode_rail_fence_cipher(string, n):
    rail=[]
    for i in range(n):
        rail.append([])
    
    i = 0
    currently = 1
    for letter in string:
        rail[i].append(letter)
        i+= currently
        
        if i == len(rail):
            currently = -1
            i = len(rail)-2
        elif i<0:
            currently = 1
            i = 1
    result = ''
    for i in rail:
        result+= ''.join(map(str,i))
    return result


def decode_rail_fence_cipher(string, n):
    rail=[]
    for i in range(n):
        rail.append([])
    
    i = 0
    currently = 1
    for letter in string:
        rail[i].append('*')
        i+= currently
        
        if i == len(rail):
            currently = -1
            i = len(rail)-2
        elif i<0:
            currently = 1
            i = 1
    result = ''
    index = 0
    for i in range(len(rail)):
        for j in range(len(rail[i])):
            rail[i][j] = string[index]
            index+=1
    print(rail)
    i = 0
    currently = 1
    railIndex = [0]*len(rail)
    for letter in string:
        result+=rail[i][railIndex[i]]
        railIndex[i]+=1   
        i+= currently
        
        if i >= len(rail):
            currently = -1
            i = len(rail)-2
            
        elif i<0:
            currently = 1
            i = 1
        
        
    return result
    
    


        




    

    
    