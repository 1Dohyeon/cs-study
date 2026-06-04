"""https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # 1. 왼쪽부터 누적 곱 채우기
        lp = 1
        for i in range(n):
            res[i] = lp      # i번째 요소를 곱하기 전의 누적곱을 먼저 저장
            lp *= nums[i]    # 다음 인덱스(i+1)의 연산을 위해 현재 요소를 곱해서 누적

        # 2. 오른쪽부터 누적 곱을 기존 값에 곱하기
        rp = 1
        for i in range(n - 1, -1, -1):
            res[i] *= rp     # 현재 저장된 왼쪽 곱에 오른쪽 누적곱을 곱함 (i 제외)
            rp *= nums[i]    # 다음 인덱스(i-1)의 연산을 위해 현재 요소를 곱해서 누적

        return res