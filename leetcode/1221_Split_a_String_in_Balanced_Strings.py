class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_counter = l_counter = 0
        result = 0
        for i in s:
            if i == "R":
                r_counter += 1
            else:
                l_counter += 1
                
            if r_counter == l_counter:
                result += 1
        return result  
