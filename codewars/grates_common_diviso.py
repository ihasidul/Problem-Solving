def mygcd(x, y):
    mod = x%y
    while(mod):
        x = y
        y = mod
        mod = x%y
    return y
