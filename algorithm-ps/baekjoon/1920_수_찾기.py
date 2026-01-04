""" https://www.acmicpc.net/problem/1920
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
"""

import sys

# n = int(sys.stdin.readline())
# # set을 써도 되는 이유: 존재 여부만 확인하면 되기 때문
# a = set(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# b = list(map(int, sys.stdin.readline().split()))

# for x in b:
#     if x in a:
#         print(1)
#     else:
#         print(0)

n = int(sys.stdin.readline())
# 이진 탐색을 위해 반드시 정렬(Sort)을 수행해야 함: O(N log N)
a = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

# 이진 탐색 함수 정의 (반복문 방식)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        # 찾았으면 1 반환
        if array[mid] == target:
            return 1
        # 중간값보다 작으면 왼쪽 탐색
        elif array[mid] > target:
            end = mid - 1
        # 중간값보다 크면 오른쪽 탐색
        else:
            start = mid + 1
            
    return 0

# 각 타겟에 대해 이진 탐색 수행: O(M log N)
for x in targets:
    print(binary_search(a, x, 0, n - 1))