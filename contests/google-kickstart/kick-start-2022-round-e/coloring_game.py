# Not working
import math
T = int(input())

for i in range(T):
    N = int(input())
    output = math.ceil(N/4)
    print("Case #"+ str(i+1) + ": {}".format(output))
