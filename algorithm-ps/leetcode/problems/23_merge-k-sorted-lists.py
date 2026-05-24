"""https://leetcode.com/problems/merge-k-sorted-lists/description/
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 
"""

from typing import List, Optional
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. 더미 노드와 힙 초기화
        dummy = ListNode(0)
        curr = dummy
        heap = []
        
        # 2. 각 리스트의 첫 번째 노드를 힙에 추가
        # (노드.val, 리스트의 인덱스, 노드 객체) 순서로 저장하여 값이 같을 때 인덱스로 비교하게 함
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        # 3. 힙에서 하나씩 꺼내며 연결
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # 꺼낸 노드의 다음 노드가 있다면 힙에 추가
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
        