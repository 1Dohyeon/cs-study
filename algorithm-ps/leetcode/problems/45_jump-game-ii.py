"""https://leetcode.com/problems/jump-game-ii/description/
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
        
        jumps = 0      # 점프 횟수
        curr_end = 0   # 현재 점프로 갈 수 있는 최대 범위의 끝
        max_reach = 0  # 다음 점프까지 고려했을 때 갈 수 있는 가장 먼 곳
        
        # 마지막 칸에 도달하면 멈추므로 n-1 전까지만 확인
        for i in range(n - 1):
            # 1. 어디까지 멀리 갈 수 있는지 계속 업데이트
            max_reach = max(max_reach, i + nums[i])
            
            # 2. 현재 내가 갈 수 있는 범위(curr_end)의 끝에 도달하면
            if i == curr_end:
                jumps += 1      # 점프 한 번 추가
                curr_end = max_reach # 다음 점프의 사거리를 업데이트
                
                # 만약 이미 끝에 도달 가능하다면 바로 종료
                if curr_end >= n - 1:
                    break
                    
        return jumps