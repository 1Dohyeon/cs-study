"""https://leetcode.com/problems/divide-two-integers/description/
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 1. 32비트 정수 오버플로우 예외 처리
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # 2. 부호 결정
        negative = (dividend < 0) != (divisor < 0)
        
        # 3. 절대값으로 계산
        m, n = abs(dividend), abs(divisor)
        res = 0
        
        # 4. 핵심 로직: 지수적 감산
        while m >= n:
            temp_divisor, count = n, 1
            # divisor를 2배씩 키우며 뭉텅이로 뺄 수 있는지 확인
            while m >= (temp_divisor << 1):
                #  temp_divisor는 3,6,12,24, ... 로 업데이트되고, count 역시 1,2,4,8,... 로 동시에 업데이트
                temp_divisor <<= 1
                count <<= 1
            
            # 찾은 큰 덩어리를 빼고 결과 누적
            m -= temp_divisor
            res += count
            
        # 5. 부호 적용 및 범위 제한
        if negative:
            res = -res
            
        return max(MIN_INT, min(MAX_INT, res))