"""https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-interview-150
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        # 매핑 정보 구성
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []

        def _backtrack(index, path):
            if len(path) == len(digits):
                res.append("".join(path)) # 리스트를 str로 join 후 배열에 삽입
                return

            # 현재 숫자가 가리키는 문자들을 하나씩 순회
            possible_letters = phone[digits[index]]
            for letter in possible_letters:
                path.append(letter)          # 선택
                _backtrack(index + 1, path)   # 다음 숫자로 이동
                path.pop()        

        _backtrack(0, [])
        return res