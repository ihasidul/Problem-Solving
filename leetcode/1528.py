class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        slst = list(s)
        res = dict(zip(indices, slst))
        sorted_res = sorted(res)
        st = ""
        for i in sorted_res:
            st += res[i]
        return st
