""" https://leetcode.com/problems/longest-palindromic-substring/description/?envType=problem-list-v2&envId=dynamic-programming
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""
class Solution:
    # Expand Around Center
    def longestPalindrome(self, s: str) -> str:
        start, max_length = 0, 1
        n = len(s)

        if n < 2:
            return s

        # 중앙에서 확장하는 방법
        for i in range(n):
            # 홀수 길이 팰린드롬
            left, right = i - 1, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                # 왼쪽 및 오른쪽 포인터가 유효하고, 문자가 동일한 동안 확장
                current_length = right - left + 1
                if current_length > max_length:
                    max_length = current_length
                    start = left
                left -= 1
                right += 1

            # 짝수 길이 팰린드롬
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                # 왼쪽 및 오른쪽 포인터가 유효하고, 문자가 동일한 동안 확장
                current_length = right - left + 1
                if current_length > max_length:
                    max_length = current_length
                    start = left
                left -= 1
                right += 1

        return s[start:start + max_length]
    
    # brute force
    # def longestPalindrome(self, s: str) -> str:
    #     ans=s[0]
    #     maxLen=1
    #     for i in range(0,len(s)-1):
    #         currString=s[i]
    #         currLen=1
    #         for j in range(i+1,len(s)):
    #             currString+=s[j]
    #             currLen+=1
    #             if(currString==currString[::-1] and currLen>maxLen):
    #                 maxLen=currLen
    #                 ans=currString

    #     return ans


    # dynamic programming
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        start, max_length = 0, 1

        for i in range(n):
            dp[i][i] = True  # 길이 1인 팰린드롬

        for length in range(2, n + 1):  # 팰린드롬의 길이
            for i in range(n - length + 1):
                j = i + length - 1  # 끝 인덱스
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True  # 길이 2인 팰린드롬
                    else:
                        # 내부가 팰린드롬이면 현재도 팰린드롬
                        dp[i][j] = dp[i + 1][j - 1]

                    # 최대 길이 갱신    
                    if dp[i][j] and length > max_length:
                        max_length = length
                        start = i

        return s[start:start + max_length]