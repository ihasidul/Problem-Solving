class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        st = ""
        while head is not None:
            st += str(head.val)
            head = head.next
        return int(st,2)