"""https://leetcode.com/problems/valid-parentheses/
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in s:
            if i in mapping:
                # 닫는 괄호라면, 스택 꼭대기와 비
                top_element = stack.pop() if stack else '#'
                if mapping[i] != top_element:
                    return False
            else:
                # 여는 괄호라면 스택에 추가
                stack.append(i)

        return not stack