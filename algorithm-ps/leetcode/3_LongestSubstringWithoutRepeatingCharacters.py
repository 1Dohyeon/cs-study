""" https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        q = deque([])
        max_size = 1

        for i in range(len(s)):
            if s[i] in q:
                while True:
                    v = q.popleft()
                    if v == s[i]:
                        break

            q.append(s[i])
            cur_size = len(q) 
            max_size = max(max_size, cur_size) 

            
        return max_size


            

