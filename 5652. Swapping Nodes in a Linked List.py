# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        temp = head
        
        slow = head
        fast = head
        initial = head
        
        for _ in range(k-1):
            fast = fast.next
            
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        for _ in range(k-1):
            initial = initial.next
            
        print(slow.val)
        print(initial.val)
        
        slow.val, initial.val = initial.val, slow.val
        
        return head
    
            
        
        
