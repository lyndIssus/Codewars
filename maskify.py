def maskify(cc):
    mask = "#" * (len(cc)-4)
    if(len(cc)<4):
        start = 0
    else:
        start = len(cc)-4
    return (mask[0:len(cc)-4] + cc[start:])
print(maskify("SF$SDfgsd2eA"))