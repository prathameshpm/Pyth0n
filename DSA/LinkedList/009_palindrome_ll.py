# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # method to check palindrome
    def isPalindrome(self, head: ListNode) -> bool:

        # initialize slow, fast and reverse pointing pointer
        slow, fast, prev = head, head, None

        # check if linked list is not ended
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # with slow at middle and fast at the end of linked list, 
        # we can reverse 
        prev, slow, prev.next = slow, slow.next, None

        # check back half is properly reversed
        while slow:
            # start back over again at head
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            # check if slow and fast disagree, 
            # then it means it is not a palindrome, so return false
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True