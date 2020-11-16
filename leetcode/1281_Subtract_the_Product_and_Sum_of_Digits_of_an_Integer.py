class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        s = 0
        for _ in range(len(str(n))): 
            x = n%10
            s += x
            product = product * x
            n = n //10
        """  print("s",s )
            print("p",product )
            print("n",n ) """
        return product - s