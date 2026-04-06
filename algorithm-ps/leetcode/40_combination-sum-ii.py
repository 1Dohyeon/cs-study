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
        # 정렬 순으로 선택을 위해 미리 정렬
        candidates.sort()

        def backtrack(remain, start, path):
            if remain == 0:
                res.append(list(path))
                return
            
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                # 현재 결정(for문 안)에서 같은 숫자가 연속되면 건너뜀
                # 단, i > start 조건이 중요: 현재 깊이에서의 첫 번째 선택은 허용
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(remain - candidates[i], i+1, path)
                path.pop()

        backtrack(target, 0, [])
        return res