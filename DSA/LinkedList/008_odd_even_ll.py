# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class of solution
class Solution:
    # method to sort odd - even wise
	def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # check linked list is empty
		if head == None:
			return None

        # initialize
        # head will always be 1st odd node
        # head will always point to 1st even node
		odd_node = head
		even_node = head.next
		evenhead = head.next

        # check if there exist next even node
		while even_node != None and even_node.next != None:
            # to find next odd node, skip 1 node after last found odd node
			odd_node.next = odd_node.next.next
            # to find next even node, skip 1 node after last found even node
			even_node.next = even_node.next.next

			odd_node = odd_node.next
			even_node = even_node.next

        # if there was no existence of next even node
        # then next node is last node and it is odd
		odd_node.next = evenhead

		return head