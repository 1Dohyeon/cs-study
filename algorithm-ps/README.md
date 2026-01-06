# Problem Solving (PS)

알고리즘 문제 풀이 과정을 기록한 폴더

## 💻 Environment
- **Language:** Python 3
- **Platform:** 
    - [Baekjoon](./baekjoon/README.md)
    - [LeetCode](./leetcode/README.md)

## 📑 유형별 대표 문제 (개념 상기용)

복잡한 응용보다는 기본 메커니즘을 명확히 이해하고 다시 상기시키기 좋은 대표 문항 리스트

### 1. 자료구조 (Data Structure)
- **Stack (List 활용):** [백준 10828 - 스택](https://www.acmicpc.net/problem/10828)
    - `append()`, `pop()` 메서드 사용법 및 LIFO 구조 이해
- **Queue (deque 활용):** [백준 2164 - 카드2](https://www.acmicpc.net/problem/2164)
    - `collections.deque`의 `popleft()`를 활용한 효율적인 큐 구현 학습
    - `collections.deque`: [deque란?](../tech/data-structure/deque.md)
- **Linked List:** [LeetCode 206 - Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
    - 노드 포인터 조작을 통한 리스트 뒤집기 및 연결 리스트 구조 숙지
- **Hash / Map:** [LeetCode 380 - Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/description/)
    - 해시 테이블의 시간 복잡도($O(1)$) 및 인덱스 관리 원리
- **Heap / Priority Queue:** [백준 1927 - 최소 힙](https://www.acmicpc.net/problem/1927)
    - `heapq` 모듈을 이용한 우선순위 큐 처리 및 완전 이진 트리 이해
    - [Python heapq는 어떻게 작동할까?](../tech/data-structure/heapq.md)
- **Tree / BST:** [백준 1991 - 트리 순회](https://www.acmicpc.net/problem/1991)
    - 재귀를 이용한 전위·중위·후위 순회 메커니즘 학습
    - [Binary Tree란?](../tech/data-structure/binary-tree.md)
    - [Binary Search Tree란?](../tech/data-structure/binary-search-tree.md)
- **Trie:** [백준 14425 - 문자열 집합](https://www.acmicpc.net/problem/14425)
    - 문자열 탐색 최적화를 위한 접두사 트리 구현

### 2. 알고리즘 (Algorithm)
- **Sorting:** [백준 18870 - 좌표 압축](https://www.acmicpc.net/problem/18870)
    - 정렬과 해시를 결합한 데이터 전처리 및 중복 제거 응용
- **Binary Search:** [백준 1920 - 수 찾기](https://www.acmicpc.net/problem/1920)
    - 정렬된 데이터에서 $O(\log N)$ 탐색 원리 및 이분 탐색 기본형
- **DFS / BFS:** [백준 1260 - DFS와 BFS](https://www.acmicpc.net/problem/1260)
    - 그래프 완전 탐색을 위한 스택/재귀(DFS)와 큐(BFS)의 활용 차이
- **Backtracking:** [백준 15649 - N과 M (1)](https://www.acmicpc.net/problem/15649)
    - 조건에 따른 상태 복구 및 가지치기(Pruning)를 이용한 탐색 최적화
- **Greedy:** [백준 11047 - 동전 0](https://www.acmicpc.net/problem/11047)
    - 매 순간 최적의 선택을 하는 탐욕법의 조건과 정당성 확인
- **DP:** [백준 1463 - 1로 만들기](https://www.acmicpc.net/problem/1463)
    - 작은 문제의 답을 저장(Memoization)하여 큰 문제를 해결하는 상향식/하향식 접근
- **Shortest Path:** [백준 1753 - 최단경로](https://www.acmicpc.net/problem/1753)
    - 다익스트라(Dijkstra) 알고리즘을 이용한 가중치 그래프 내 최단 거리 산출
- **MST:** [백준 1197 - 최소 스패닝 트리](https://www.acmicpc.net/problem/1197)
    - Kruskal / Prim 알고리즘 및 Union-Find를 활용한 최소 비용 간선 연결
- **Two Pointers:** [백준 2003 - 수들의 합 2](https://www.acmicpc.net/problem/2003) / [백준 2559 - 수열](https://www.acmicpc.net/problem/2559)
    - 구간 포인터 이동 및 슬라이딩 윈도우를 이용한 $O(N)$ 연산 효율화