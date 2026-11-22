class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head

        for _ in range(k - 1):
            first = first.next

        node1 = first
        second = head
        fast = first.next

        while fast:
            fast = fast.next
            second = second.next

        node1.val, second.val = second.val, node1.val

        return head