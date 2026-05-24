"""https://leetcode.com/problems/combination-sum/description/
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(remain, start, path):
            # 1. 목표값에 도달한 경우
            if remain == 0:
                res.append(list(path)) # 현재 경로의 복사본을 결과에 추가
                return
            
            # 2. 목표값을 초과한 경우 (더 이상 계산할 필요 없음)
            if remain < 0:
                return

            # 3. 숫자 선택하기
            for i in range(start, len(candidates)):
                # 숫자 하나를 선택해서 경로에 추가
                path.append(candidates[i])
                
                # 재귀 호출: 숫자를 중복해서 쓸 수 있으므로 인덱스 i를 그대로 넘김
                # 남은 금액(remain)에서 선택한 숫자를 뺌
                backtrack(remain - candidates[i], i, path)
                
                # 4. 백트래킹: 마지막에 넣었던 숫자를 빼고 다음 숫자로 넘어감
                path.pop()

        backtrack(target, 0, [])
        return res
    

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 1. 먼저 정렬 => 가지치기(Pruning)할 때 유용 => 굳이 끝까지 탐색할 필요 없음
        candidates.sort()
        n = len(candidates)

        def backtrack(remain, start, path):
            if remain == 0:
                res.append(list(path))
                return

            for i in range(start, n):
                # 2. 가지치기 (Pruning)
                # 현재 숫자를 뺐는데 이미 음수라면, 뒤에 있는 더 큰 숫자들은 볼 필요도 없음
                if remain - candidates[i] < 0:
                    break 
                
                path.append(candidates[i])
                backtrack(remain - candidates[i], i, path)
                path.pop()

        backtrack(target, 0, [])
        return res