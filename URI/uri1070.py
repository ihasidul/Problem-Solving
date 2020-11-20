x = int(input())
count = 0
for _ in range(12):
    if(x%2 == 0):
        x  += 1
        continue
    else:
        print(x)
        if(count == 6):
            break
        count += 1
        x += 1