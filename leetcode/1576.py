class Solution:
    def modifyString(self, s: str) -> str:
        res = list(s)
        
        for i in range(len(res)):
            if res[i] == '?':
                left = res[i-1] if i > 0 else ''
                right = res[i+1] if i < len(s) - 1 else ''
                
                for _ in 'abc':
                    if _ != left and _ != right:
                        res[i] = _
                        break
        
        return ''.join(res) 