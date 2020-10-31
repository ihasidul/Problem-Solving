class Solution:
    def reverse(self, x: int) -> int:
        r = int(str(abs(x))[::-1])
        #print(int(str(abs(x))[::-1]))
        rn = r * -1
        #print(rn)
        if x < 0:
            return rn if rn > -2**31 else 0        
        return r if r < 2**31 else 0