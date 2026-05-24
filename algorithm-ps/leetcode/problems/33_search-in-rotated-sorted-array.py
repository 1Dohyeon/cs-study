"""https://leetcode.com/problems/search-in-rotated-sorted-array/description/
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # 정답을 찾은 경우 즉시 인덱스 반환
            if nums[mid] == target:
                return mid
            
            # 1. 왼쪽 절반(left ~ mid)이 정렬된 구간인지 확인
            if nums[left] <= nums[mid]:
                # target이 이 정렬된 '왼쪽 구간' 안에 있는가
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # 왼쪽으로 좁히기
                else:
                    left = mid + 1  # 오른쪽으로 점프
            
            # 2. 위 조건이 아니면 오른쪽 절반(mid ~ right)이 정렬된 구간임
            else:
                # target이 이 정렬된 '오른쪽 구간' 안에 있는가
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # 오른쪽으로 좁히기
                else:
                    right = mid - 1 # 왼쪽으로 점프
                    
        return -1 # 끝까지 찾지 못한 경우