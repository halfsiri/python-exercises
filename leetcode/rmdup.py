from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def deleteDuplicates(self, head: Optional['ListNode']) -> Optional['ListNode']:
        start = head
        while head is not None:
            if head.next is None: # Check if this is the last node
                break
            if head.val == head.next.val:
                if head.next.next is None: # Check if the next node is the last node
                    head.next = None
                else:
                    head.next = head.next.next
            else:
                head = head.next
        return start

# Create a linked list: 1 -> 1 -> 2
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)

# Test the deleteDuplicates method
test = ListNode()
test2 = test.deleteDuplicates(head)

# Print the result
while test2 is not None:
    print(test2.val, end=" -> ")
    test2 = test2.next

# Output: 1 -> 2 ->
