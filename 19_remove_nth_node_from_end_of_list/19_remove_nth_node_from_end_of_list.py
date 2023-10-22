# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # 步驟2：計算要移除的節點的位置
        target_index = length - n
        
        # 如果要移除的是頭節點
        if target_index == 0:
            return head.next
        
        # 步驟3：第二次遍歷鏈表，找到目標節點的前一個節點
        current = head
        for i in range(target_index - 1):
            current = current.next
        
        # 步驟4：移除節點
        current.next = current.next.next
        
        # 步驟5：返回修改後的鏈表的頭節點
        return head