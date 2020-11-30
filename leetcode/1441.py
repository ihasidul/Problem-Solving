class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l = []
        s = set(target)#this is to boost lookup performance
        for i in range(1, target[-1] + 1):
            l.append("Push")
            if i not in s:
                l.append("Pop")
        return l 