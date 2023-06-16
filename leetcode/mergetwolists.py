"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
# Definition of the ListNode class

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition of the Solution class
class Solution(object):
    def sortLists(self, head):
        if not head or not head.next:
            return head

        # Split the list into two halves
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None

        # Recursively sort the two halves
        left = self.sortLists(head)
        right = self.sortLists(second_head)

        # Merge the sorted halves
        return self.mergeLists(left, right)

    def mergeLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            result = list1
            result.next = self.mergeLists(list1.next, list2)
        else:
            result = list2
            result.next = self.mergeLists(list1, list2.next)

