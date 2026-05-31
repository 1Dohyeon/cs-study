"""https://leetcode.com/problems/jump-game/description/
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 내가 현재까지 도달할 수 있는 가장 먼 인덱스
        max_reach = 0
        
        for i in range(len(nums)):
            # 최대 이동 거리로 i까지 못 감
            if i > max_reach:
                return False
            
            # 최대 도달 거리를 계속 더 큰 값으로 갱신
            max_reach = max(max_reach, i + nums[i])
            
            # 만약 이미 배열의 마지막 인덱스 이상으로 갈 수 있게 되었다면 성공
            if max_reach >= len(nums) - 1:
                return True
                
        return True