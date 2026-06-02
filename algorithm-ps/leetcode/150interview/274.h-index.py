"""https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

 

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 

Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        # 앞에서부터 확인하며 조건(인용수 >= 논문 수)을 비교
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                continue
            else:
                return i # 그 전까지 성공한 개수인 i를 리턴

        # 모두 잘 인용되었으면 배열의 총 길이
        return len(citations)