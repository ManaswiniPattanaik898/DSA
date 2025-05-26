class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class Solution:
    def sortedInsert(self, head, data):
        #code here
        new_node = Node(data)

    # If the list is empty
        if not head:
            new_node.next = new_node
            return new_node

        curr = head

        while True:
        # Case 1: Insert between two nodes
            if curr.data <= data <= curr.next.data:
                break

        # Case 2: Insert at turning point (from max to min)
            if curr.data > curr.next.data:
                if data >= curr.data or data <= curr.next.data:
                    break

            curr = curr.next

        # Case 3: Full loop done; insert anywhere
            if curr == head:
                break

    # Insert new node
        new_node.next = curr.next
        curr.next = new_node

    # If inserted node is new minimum, return it as new head
        return new_node if data < head.data else head