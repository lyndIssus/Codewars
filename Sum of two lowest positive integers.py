def sum_two_smallest_numbers(numbers):
    min1 = numbers[0]
    min2 = numbers[0]
    for i in numbers:
        if i < min1:
            min2 = min1
            min1 = i
        elif i < min2 and i!= min1:
            min2 = i
    return min1 + min2        