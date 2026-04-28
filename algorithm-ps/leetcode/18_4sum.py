"""https://leetcode.com/problems/4sum/description/
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 3):
            # 첫 번째 숫자 중복 제거
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                # 두 번째 숫자(Center) 중복 제거
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # 투 포인터 중복 제거
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
        return res
    
    # set을 이용한 풀이
    # 중복 제거가 간편하지만, 정답 리스트의 순서가 보장되지 않고, 메모리 효율이 상대적으로 떨어질 수 있음
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)

        for i in range(n-3):
            # 고정값(nums[i]) 중복 방지
            # 이전 값과 같다면 이미 그 숫자로 만들 수 있는 조합은 다 찾은 상태임
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            for j in range(i+1, n-2):
                # 고정값(nums[j]) 중복 방지
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        res.add((nums[i], nums[j], nums[left],nums[right]))
                        left += 1
                        right -= 1


        return [list(x) for x in res]


