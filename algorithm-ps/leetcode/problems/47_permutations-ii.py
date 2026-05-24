"""https://leetcode.com/problems/permutations-ii/description/
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False] * n
        nums.sort()

        def backtrack(path):
            if len(path) == n:
                # list로 감싸지 않으면 빈 배열이 담김.
                # 파이썬 리스트는 참조(Reference) 방식이라, 
                # 복사본을 만들지 않으면 원본 path가 변할 때 res에 담긴 값도 같이 변하기 때문.
                res.append(list(path))
                return

            for i in range(n):
                if visited[i]:
                    continue

                # nums가 정렬 되었을 경우
                # 이전 숫자와 현재 숫자가 같고(nums[i] == nums[i-1])
                # 이전 숫자가 지금 사용 중이 아니라면(not visited[i-1]) 
                #   -> 이미 한 번 써먹고 돌아온 녀석은 다시 시작점으로 잡지 않겠다
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    # 이전에 이미 그 숫자로 시작하는 모든 경우의 수를 다 훑었다는 뜻
                    continue
                
                path.append(nums[i])
                visited[i] = True
                backtrack(path)

                path.pop()
                visited[i] = False

        backtrack([])
        # # 리스트 안의 리스트들을 튜플로 바꿔서 set에 넣기
        # unique_res = set(tuple(x) for x in res)
        # # 다시 리스트 형태로 변환 -> (Permutations) * N 만큼 더 걸림
        # res = [list(x) for x in unique_res]

        return res