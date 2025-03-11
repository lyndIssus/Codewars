def solution(args):
    result = ""
    i = 0
    while i < len(args)-2:
        if(abs(args[i]-args[i+1]) == 1 and abs(args[i]-args[i+2])==2):
            current = i
            while current < len(args) - 1 and abs(args[current] - args[current + 1]) == 1:
                current+=1
            result+= (str(args[i])+ "-" + str(args[current])+ ",")
            i = current + 1
            
        else:
            result+=(str(args[i])) + ","
            i+=1
    while i < len(args):
        result+=(str(args[i])) + ","
        i+=1
    return result[0:len(result)-1] if result[len(result)-1:] ==", " else result

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))