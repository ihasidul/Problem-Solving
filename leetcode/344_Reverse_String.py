class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for item in range(len(s)//2):
            temp = s[item]
            s[item] = s[len(s) - (1 + item)]
            s[len(s) - (1 + item)] = temp
            #print(s)