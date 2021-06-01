def string_challenge(s):
    lst = s.split(".")
    print(lst)
    left = int(lst[0])
    right = int(lst[1])
    templeft = int(lst[0])
    
    while( left >= 0):
        print("full ",end = "")
        left -= 1
    for i in range(5 - templeft):

        if ( right > 0 ):
            print("half", end= "")
        else:
            print("empty", end = "")
        


string_challenge("4.5")

