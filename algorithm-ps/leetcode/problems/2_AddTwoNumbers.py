""" https://leetcode.com/problems/add-two-numbers/description/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def toNum(node):
            res = 0
            multiplier = 1
            while node:
                res += node.val * multiplier
                multiplier *= 10
                node = node.next
            return res

        num1 = toNum(l1)
        num2 = toNum(l2)

        total = num1 + num2

        if total == 0:
            return ListNode(0)

        # 실제 데이터는 dummy 다음부터 시작
        dummy = ListNode(0)
        curr = dummy
        
        while total > 0:
            digit = total % 10  # 가장 뒷자리 숫자 추출 (예: 807 -> 7)
            curr.next = ListNode(digit)  # 새 노드 생성 및 연결
    
            curr = curr.next  # 다음 칸으로 이동
            total //= 10  # 사용한 자릿수 제거 (예: 807 -> 80)

        return dummy.next