"""https://leetcode.com/problems/multiply-strings/
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        # 결과의 최대 길이는 두 숫자의 길이를 합친 것
        res = [0] * (len(num1) + len(num2))
        
        # 뒤에서부터 한 자리씩 곱함
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # 문자를 숫자로 변환 (ord 활용)
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # 곱한 결과와 현재 자리에 있던 값을 더함
                mul = digit1 * digit2
                p1, p2 = i + j, i + j + 1 
                total = mul + res[p2] # 이전 계산에서 넘어온 올림수를 더해서 현재 칸의 진짜 합계를 구함(10이 넘어갔을 때를 방지)
                
                # 올림 처리
                res[p2] = total % 10   # 현재 곱셈 자리
                res[p1] += total // 10 # 현재 곱셈의 앞자리(올림 당하는 자리)
                
        # 배열 앞의 0들을 제거하고 문자열로 합침
        ans = "".join(map(str, res))
        return ans.lstrip("0")