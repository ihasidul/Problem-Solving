class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I' : 1,'V' : 5,'X' : 10,'L' : 50,'C' :100,'D' :500,'M' : 1000}
        val = 0 
        lastChar =""
        for i in s:
            val = val + romans[i]
            if lastChar != "" and (romans[lastChar] < romans[i]):
                val -= 2*romans[lastChar]
            lastChar = i

        return val    #for key, value in romans.items():

print(Solution().romanToInt('MCMXCIV'))