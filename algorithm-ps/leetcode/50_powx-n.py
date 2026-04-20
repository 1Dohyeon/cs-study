"""https://leetcode.com/problems/powx-n/description/
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 1. 지수가 0이면 항상 1
        if n == 0:
            return 1
        
        # 2. 음수 지수 처리: x를 역수로 만들고 n을 양수로 바꿈
        if n < 0:
            x = 1 / x
            n = -n
        
        # 3. 분할 정복(재귀)
        def fast_pow(base, power):
            if power == 0:
                return 1
            
            # 절반을 먼저 구함 (n/2)
            half = fast_pow(base, power // 2)
            
            # 지수가 짝수면: (x^(n/2))^2
            if power % 2 == 0:
                return half * half
            # 지수가 홀수면: x * (x^(n/2))^2
            else:
                return half * half * base
                
        return fast_pow(x, n)