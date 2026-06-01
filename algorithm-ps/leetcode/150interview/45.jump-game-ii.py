"""https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150
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
    # nums는 무조건 도달할 수 있는 배열로 주어짐
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        jumps = 0 # 실제 점프 횟수
        max_reach = 0 # 여태까지 발견한 가장 먼 사정거리
        current_end = 0 # 현재 점프 횟수로 도달 가능한 한계선

        for i in range(len(nums)-1):
            # 현재 칸에서 갈 수 있는 가장 먼 거리를 계속 업데이트
            max_reach = max(max_reach, i + nums[i])

            # 현재 점프로 올 수 있는 한계선(current_end)에 도달했다면
            if i == current_end:
                jumps += 1 # 점프 횟수를 1회 추가하고,
                current_end = max_reach # 다음 한계선을 여태까지 구한 최전방 선으로 갱신
                
                # 만약 새로 갱신한 한계선이 이미 마지막 칸을 넘어섰다면 더 볼 필요도 없이 종료
                if current_end >= len(nums) - 1:
                    break
        
        return jumps