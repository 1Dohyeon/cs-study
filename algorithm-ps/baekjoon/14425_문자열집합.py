""" https://www.acmicpc.net/problem/14425
문제
총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.

다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.

다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink

출력
첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.

4
"""

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# s = []
# inputs = []
# count = 0

# for _ in range(n):
#     s.append(input().rstrip())

# for _ in range(m):
#     inputs.append(input().rstrip())

# for word in inputs:
#     if word in s:
#         count += 1

# print(count)

import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    
    # 딕셔너리로 트라이 구현
    trie = {}
    
    # 집합 S 삽입
    for _ in range(n):
        word = input().rstrip()
        current_node = trie
        for char in word:
            # 해당 문자가 없으면 새 딕셔너리 생성
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]
        # 단어의 끝을 표시 (문자열에 나올 수 없는 특수값 사용)
        current_node['*'] = True

    # 검사 및 카운트
    count = 0
    for _ in range(m):
        word = input().rstrip()
        current_node = trie
        found = True
        for char in word:
            if char not in current_node:
                found = False
                break
            current_node = current_node[char]
        
        # 마지막 노드에 '*'가 있어야 완전한 단어 일치
        if found and '*' in current_node:
            count += 1
            
    print(count)

solve()