"""https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

from typing import List

# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums:
#             return [-1, -1]

#         if target not in nums:
#             return [-1, -1]

#         res = []
#         left = 0
#         right = len(nums)-1

#         while True:
#             if nums[left] < target:
#                 left += 1
#             if nums[right] > target:
#                 right -=1
#             if nums[left] == target and nums[right] == target:
#                 res.append(left)
#                 res.append(right)
#                 break

#         return res

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid # 일단 찾았으니 기록
                    if isFirst:
                        right = mid - 1 # 왼쪽 끝을 찾기 위해 더 왼쪽으로
                    else:
                        left = mid + 1  # 오른쪽 끝을 찾기 위해 더 오른쪽으로
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        return [findBound(True), findBound(False)]