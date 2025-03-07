def count_bits(n):
    transform = str(bin(n))
    count = transform.count("1",1)
    
    return count