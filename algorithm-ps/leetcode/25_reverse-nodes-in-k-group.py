"""https://leetcode.com/problems/reverse-nodes-in-k-group/description/
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 내부 함수로 정의할 때는 self를 빼고 정의하는 것이 일반적입니다.
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr 

        dummy = ListNode(0, head)
        groupPrev = dummy # 0. 뒤집을 그룹 '직전'의 노드를 고정

        while True:
            # 1. 현재 groupPrev로부터 k번째 노드가 있는지 확인
            kth = getKth(groupPrev, k)
            if not kth: # k개가 안 되면 뒤집지 않고 종료
                break
            
            groupNext = kth.next # 2. 다음 그룹의 시작점을 미리 저장
            
            # 3. 그룹 뒤집기 시작
            # prev를 kth.next(다음 그룹 시작점)로 두면, 
            # 뒤집기가 끝났을 때 그룹의 꼬리가 자동으로 다음 그룹과 연결됨
            prev, curr = kth.next, groupPrev.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev # 방향 뒤집기
                prev = curr      # 포인터 이동
                curr = tmp       # 포인터 이동
            
            # 4. 뒤집힌 그룹을 앞쪽(groupPrev)과 연결
            # 뒤집기 전의 첫 번째 노드(groupPrev.next)를 미리 백업
            tmp = groupPrev.next 
            groupPrev.next = kth # groupPrev를 새로운 머리(kth)와 연결
            groupPrev = tmp      # groupPrev를 뒤집힌 그룹의 끝으로 이동시켜 다음 준비
            
        return dummy.next