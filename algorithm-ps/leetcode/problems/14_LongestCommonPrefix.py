"""https://leetcode.com/problems/longest-common-prefix/description/
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # 1. 정렬을 하면 사전 순으로 가장 앞의 것과 가장 뒤의 것이 배치됨
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        ans = ""
        # 2. 가장 첫 번째 단어와 가장 마지막 단어만 비교하면 됨
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                ans += first[i]
            else:
                break
                
        return ans