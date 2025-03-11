def ips_between(start, end):
    result = []
    between = 0
    startV = list(map(int,start.split('.')))
    endV = list(map(int,end.split('.')))
    for i in range(len(startV)):
        result.append(endV[i] - startV[i])
    for i in range(len(result)):   
        between += (256**(len(result)-i-1))*result[i]
    return between


