#It needs to be optimized 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num/2)+1):
        if num%i ==0:
            return False
            break
    else:
        return True
num = int(input())
print(is_prime(num))
