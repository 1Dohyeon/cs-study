""" https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
"""

# Definition for singly-linked list.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 이전 노드를 저장하는 포인터. 초기값은 None
        prev = None
        # 현재 노드를 가리키는 포인터. 초기값은 head
        current = head

        # 현재 노드가 None이 될 때까지 반복
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        return prev


print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))