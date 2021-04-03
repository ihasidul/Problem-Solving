class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        s = 0
        for i in A:
            if i % 2 == 0:
                s += i
        print(s)  
        for i  in range(len(queries)):
            val = queries[i][0]
            aPos = queries[i][1]
            tem = A[aPos]
            A[aPos] = A[aPos] + val
            if (tem % 2  == 0 and A[aPos] % 2 == 0 ):
                s += val
                result.append(s)
            elif (tem % 2  == 0 and A[aPos] % 2 != 0 ):
                s -= tem 
                result.append(s)
            elif (tem % 2  != 0 and A[aPos] % 2 == 0 ):
                s += A[aPos] 
                result.append(s)
            else:
                result.append(s)
                
            
        if result == []  : 
            return [0] 
        else:
            return result