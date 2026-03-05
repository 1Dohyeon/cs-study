"""https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # list의 전체 길이 계산
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1

        dummy = ListNode(0, head)
        curr = dummy
        
        # 삭제할 노드의 직전 노드까지 이동 (length - n 번 이동)
        for _ in range(length - n):
            curr = curr.next

        curr.next = curr.next.next
        return dummy.next    
            

        

        