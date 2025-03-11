import heapq
def hamming(n):
    arr = [1]
    factors = [2,3,5]
    smallest = 1
    for i in range(n):
        smallest = heapq.heappop(arr)
        for factor in factors:
            if(smallest * factor not in arr):
                heapq.heappush(arr,smallest*factor)
    return smallest
    




