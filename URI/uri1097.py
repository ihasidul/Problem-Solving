x = 7
for _ in range(1,10,2):
    for j in range(3):
        print("I=%d J=%d" % (_,x))
        x -= 1
        if(j == 2):
            x  = x + 5