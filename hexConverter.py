def rgb(r, g, b): 
    form = lambda x: min(255, max(x,0)) 
    return "{:02X}{:02X}{:02X}".format(form(r),form(g),form(b))

