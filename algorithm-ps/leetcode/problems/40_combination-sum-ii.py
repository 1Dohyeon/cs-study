"""https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(remain, start, path):
            if remain == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # 같은 레벨(형제 노드)에서 이미 사용한 숫자와 같다면 건너뜀
                # # i > start 조건은 "현재 선택하려는 칸"에서 첫 번째 숫자가 아닐 때를 의미함
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                # 가지치기: 정렬되어 있으므로 이미 넘치면 뒤는 볼 필요 없음
                if remain - candidates[i] < 0:
                    break # or return

                path.append(candidates[i])
                # # i+1을 넘겨서 현재 숫자를 중복해서 쓰지 않도록 함
                backtrack(remain - candidates[i], i+1, path)
                path.pop()

        backtrack(target, 0, [])
        return res


"""
i > start 조건이 왜 필요한지 예시로 설명:

[ 1(A), 1(B), 2 ]

Level 0: [ 1(A) ]를 뽑음 (첫 후보 면제)
   │
   └── Level 1: [ 1(B) ]를 뽑음 (이 층의 첫 후보(i == start)이므로 면제!) -> [1, 1] (OK)

Level 0: [ 1(B) ]를 뽑으려 함 (i=1, start=0 이므로 i > start)
   │   그런데 1(B) == 1(A) 이네? 
   └── [ 1(B) ]는 SKIP! (이미 1(A)가 모든 경우의 수를 다 확인했음)
"""