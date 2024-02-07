# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmpr=head
        while tmpr and tmpr.next:
            if tmpr.val==tmpr.next.val:
                tmpr.next=tmpr.next.next
            else:
                tmpr=tmpr.next
        return head
