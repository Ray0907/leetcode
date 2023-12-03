# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def mergeTwoLists(x, y):
            dummy = ListNode()
            current = dummy

            while x and y:
                if x.val < y.val:
                    current.next = x
                    x = x.next
                else:
                    current.next = y
                    y = y.next
                current = current.next
            if x:
                current.next = x
            if y:
                current.next = y
            return dummy.next
        
        def mergeKListHelper(lists, left, right):
            if left == right:
                return lists[left]
            mid = (left + right ) //2
            left_merged = mergeKListHelper(lists, left, mid)
            right_merged = mergeKListHelper(lists, mid + 1, right)
            return mergeTwoLists(left_merged, right_merged)
        return mergeKListHelper(lists, 0, len(lists) -1)