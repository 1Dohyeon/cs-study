"""https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in dict_strs:
                dict_strs[key] = [s]
            else:
                dict_strs[key].append(s)

        return list(dict_strs.values())
    
    from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 초기값을 list로 가지는 딕셔너리 생성
        dict_strs = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            # key가 없으면 알아서 []를 만들고 append 해줍니다.
            dict_strs[key].append(s)

        return list(dict_strs.values())