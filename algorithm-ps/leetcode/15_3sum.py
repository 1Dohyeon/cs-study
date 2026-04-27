"""https://leetcode.com/problems/3sum/description/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # 투 포인터를 쓰기 위해 반드시 정렬!
        
        n = len(nums)
        
        # 1. 조기 종료 (Early Exit)
        if n < 3 or nums[0] > 0 or nums[-1] < 0:
            return []

        for i in range(n - 2):
            # 2. 고정값(nums[i]) 중복 제거
            # 이전 값과 같다면 이미 그 숫자로 만들 수 있는 조합은 다 찾은 상태임
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 고정값 이후의 숫자들 중에서 두 합을 찾기 위한 투 포인터 설정
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # 합이 작으면 왼쪽 포인터를 오른쪽으로 (값 증가)
                elif total > 0:
                    right -= 1 # 합이 크면 오른쪽 포인터를 왼쪽으로 (값 감소)
                else:
                    # 합이 0인 경우 정답 리스트에 추가
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 3. 포인터 이동 및 중복 제거
                    # 정답을 찾은 후에도 left나 right가 가리키는 값이 다음 값과 같다면 건너뜀
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 다음 새로운 숫자를 보기 위해 포인터 한 칸 더 이동
                    left += 1
                    right -= 1
                    
        return res
    
    # set을 이용한 풀이 
    # 중복 제거가 간편하지만, 정답 리스트의 순서가 보장되지 않고, 메모리 효율이 상대적으로 떨어질 수 있음
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)

        if n < 3 or nums[0] > 0 or nums[-1] < 0:
            return []

        for i in range(n-2):
            # 예외처리: i가 이전값과 같으면 해당 숫자 조합은 이미 다 찾음
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

        return [list(x) for x in res]
