class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        s = 0
        for i in range(len(endTime)):
            if (startTime[i] <= queryTime and endTime[i] >= queryTime):
                s = s + 1
            else:
                continue
        return s
                
