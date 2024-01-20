class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow = head
        # fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         return True
        # return False

        res = {}
        current = head
        while current:
            if current in res:
                return True
            else: res[current] = True
            current = current.next
        return False