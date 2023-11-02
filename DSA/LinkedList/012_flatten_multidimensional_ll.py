# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Node) -> Node:
        if not head:
            return head
        current_node = head
        while current_node != None:
            if current_node.child == None:
                current_node = current_node.next
            else:
                tail_child = current_node.child
                while tail_child.next != None:
                    tail_child = tail_child.next
                tail_child.next = current_node.next
                if tail_child.next != None:
                    tail_child.next.prev = tail_child
                current_node.next = current_node.child
                current_node.next.prev = current_node
                current_node.child = None
        return head