#https://leetcode.com/problems/merge-nodes-in-between-zeros/submissions/1308876164/?envType=daily-question&envId=2024-07-04
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        current = head.next  # Skip the initial zero
        merged_head = ListNode(0)  # Dummy node for the result list
        merged_current = merged_head
        current_sum = 0
        
        while current:
            if current.val != 0:
                current_sum += current.val
            else:
                if current_sum > 0:  # Only add a new node if there is a sum
                    merged_current.next = ListNode(current_sum)
                    merged_current = merged_current.next
                    current_sum = 0
            current = current.next
        
        return merged_head.next

# Helper function to create linked list from list
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
