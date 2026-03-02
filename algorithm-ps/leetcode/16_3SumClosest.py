"""https://leetcode.com/problems/3sum-closest/description/
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            # 중복된 고정값 건너뛰기 (최적화)
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total
                
                if abs(target - total) < abs(target - res):
                    res = total

                if total < target:
                    left += 1
                else:
                    right -= 1
                    
        return res