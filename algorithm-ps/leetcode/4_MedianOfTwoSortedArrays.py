""" https://leetcode.com/problems/median-of-two-sorted-arrays/description/
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import List

class Solution:
    # O((m+n)log(m+n)) time
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mid = (m + n) // 2
        
        merged = nums1 + nums2
        merged.sort()
        
        if (m + n) % 2 == 1:
            return merged[mid]
        else:
            return (merged[mid] + merged[mid - 1]) / 2
        
    # O(m+n) time
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mid = (m + n) // 2
        
        i = j = 0
        merged = []
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        while i < m:
            merged.append(nums1[i])
            i += 1
        
        while j < n:
            merged.append(nums2[j])
            j += 1
        
        if (m + n) % 2 == 1:
            return merged[mid]
        else:
            return (merged[mid] + merged[mid - 1]) / 2
        
    # O(log(m+n)) time
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        # 1. 항상 더 짧은 배열(nums1)을 기준으로 이진 탐색을 수행
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        low, high = 0, m
        
        while low <= high:
            # 2. nums1을 자를 위치(partitionX)를 이진 탐색으로 결정
            partitionX = (low + high) // 2
            # 3. 전체의 절반이 왼쪽으로 가도록 nums2의 자를 위치(partitionY)를 계산
            # (m + n + 1) // 2는 전체 개수가 홀수일 때 왼쪽 부분이 하나 더 많게 설정
            partitionY = (m + n + 1) // 2 - partitionX
        
            # 4. 각 파티션의 경계에 있는 4개의 값을 가져옴
            # 인덱스가 범위를 벗어나는 경우(자른 위치가 맨 앞이나 맨 뒤일 때)를 위해 무한대(inf)를 사용
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            # 5. 지그재그(교차) 비교를 통해 올바른 절반으로 나뉘었는지 확인
            # 왼쪽 그룹의 모든 값은 오른쪽 그룹의 모든 값보다 작거나 같아야 함
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
                
            # 7. 만약 nums1의 왼쪽 값이 너무 크다면, 경계선을 왼쪽으로 옮김
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # 8. 만약 nums2의 왼쪽 값이 너무 크다면, 경계선을 오른쪽으로 옮김
            else:
                low = partitionX + 1