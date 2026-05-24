"""https://leetcode.com/problems/swap-nodes-in-pairs/description/
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev = dummy # 바꿀 두 노드의 '바로 앞' 노드

        while prev.next and prev.next.next:
            # 바꿀 두 노드 지정
            first = prev.next
            second = prev.next.next
            
            # 포인터 재조립 (Swap)
            # [prev] -> [first] -> [second] -> [next_pair]
            # 아래 3단계를 거치면 순서가 바뀝니다.
            
            prev.next = second        # prev가 second를 가리키게 함
            first.next = second.next  # first가 그 다음 쌍을 가리키게 함
            second.next = first       # second가 first를 가리키게 함
            
            # [prev] -> [second] -> [first] -> [next_pair]
            
            # 3. 다음 쌍으로 이동
            # 이제 first가 뒤로 갔으므로, 다음 쌍의 '앞 노드'는 first가 됩니다.
            prev = first
            
        return dummy.next