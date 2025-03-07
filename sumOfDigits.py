def digital_root(n):
    change = [int(d) for d in str(n)]
    return  sum(change) if len(change)<2 else digital_root(sum(change))

