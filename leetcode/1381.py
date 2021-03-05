class CustomStack:

    def __init__(self, maxSize: int):
        self.lst = [] 
        self.size = maxSize

    def push(self, x: int) -> None:
        if(len(self.lst) < self.size):
            self.lst.append(x)

    def pop(self) -> int:
        if len(self.lst) >= 1:
            return self.lst.pop()
        else:
            return -1 
        

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < len(self.lst):
                self.lst[i] += val
                
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
