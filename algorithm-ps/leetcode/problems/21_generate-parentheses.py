"""https://leetcode.com/problems/generate-parentheses/description/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # "(" 는 최대 n개
        # ")" 는 현재까지 쓴 '('의 개수보다 적을 때만 사용 가능

        def backtrack(open_count, close_count, path):
            # 1. 베이스 케이스: 괄호를 다 썼다면 결과에 추가
            if len(path) == 2 * n:
                res.append(path)
                return
            
            # 2. 열린 괄호를 더 쓸 수 있다면 추가
            if open_count < n:
                backtrack(open_count + 1, close_count, path + "(")
                
            # 3. 닫힌 괄호를 쓸 수 있다면(열린 게 더 많다면) 추가
            if close_count < open_count:
                backtrack(open_count, close_count + 1, path + ")")
        
        backtrack(0, 0, "")
        return res