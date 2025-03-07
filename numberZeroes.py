def zeros(n):
    result = 0
    i = 5
    while n//i >0:
        result += n//i
        i=i*5
    return result 

print(zeros(1000))