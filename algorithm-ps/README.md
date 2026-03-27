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

### 3. 추가 추천 문제 (대표 문제 보강)

- **Stack 심화:** [LeetCode 20 - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)
  - 스택으로 괄호 짝 검증 로직을 구현하며 조건 분기 정확도 강화
- **Queue/Graph Traversal:** [LeetCode 102 - Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)
  - 큐 기반 레벨 순회 패턴을 트리/그래프 탐색에 재사용 가능
- **Linked List 포인터 조작:** [LeetCode 24 - Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/)
  - 연결 리스트에서 포인터 재연결 순서의 중요성 학습
- **Hash + Sliding Window:** [LeetCode 3 - Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
  - 해시와 투 포인터 결합으로 중복 관리 및 윈도우 최적화
- **Binary Search 응용:** [LeetCode 33 - Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)
  - 정렬 조건이 부분적으로 깨진 배열에서의 분기 전략 연습
- **Backtracking 심화:** [LeetCode 79 - Word Search](https://leetcode.com/problems/word-search/description/)
  - 방문 처리/복구(백트래킹)의 핵심 패턴 정리
- **DP 트리 구조 응용:** [LeetCode 96 - Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/description/)
  - 카탈란 수 기반 점화식 설계 훈련
- **Shortest Path/Graph:** [LeetCode 133 - Clone Graph](https://leetcode.com/problems/clone-graph/description/)
  - 그래프 복제 과정에서 방문 체크와 노드 매핑 활용

## 📑 유형별 응용 문제

기본 유형을 익힌 뒤, 구현 복잡도와 사고 확장이 필요한 문제들 위주 추천 리스트

### 1. 자료구조 응용

- **Linked List Hard:** [LeetCode 25 - Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)
  - 구간 단위 역전과 포인터 연결을 동시에 처리하는 고난도 연결 리스트 문제
- **Advanced Hash Design:** [LeetCode 381 - Insert Delete GetRandom O(1) - Duplicates Allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/)
  - 중복 원소를 허용하는 자료구조 설계 및 인덱스 동기화
- **BST Validation/Recovery:** [LeetCode 98 - Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/) / [LeetCode 99 - Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/description/)
  - 트리 순회와 경계값 관리, 잘못된 노드 복구 사고 확장

### 2. 탐색/백트래킹 응용

- **Combination Search:** [LeetCode 17 - Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)
  - 재귀적으로 상태 공간을 확장하는 조합 탐색 기본기 강화
- **Constraint Backtracking:** [LeetCode 36 - Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)
  - 행/열/박스 조건을 동시 관리하는 검증형 탐색
- **Graph Flood Fill:** [LeetCode 733 - Flood Fill](https://leetcode.com/problems/flood-fill/description/)
  - DFS/BFS를 격자 문제에 적용하는 대표 패턴

### 3. 정렬/투포인터/구간 처리 응용

- **Two Pointers + Sorting:** [LeetCode 15 - 3Sum](https://leetcode.com/problems/3sum/description/) / [LeetCode 18 - 4Sum](https://leetcode.com/problems/4sum/description/)
  - 정렬 이후 포인터 이동 규칙으로 중복 제거와 해 탐색 최적화
- **Boundary Binary Search:** [LeetCode 34 - Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/)
  - lower/upper bound 분리 구현 연습
- **Permutation Logic:** [LeetCode 31 - Next Permutation](https://leetcode.com/problems/next-permutation/description/)
  - 사전순 다음 상태를 만드는 스왑 + 뒤집기 규칙 이해

### 4. 그래프/트리/경로 응용

- **Tree Construction:** [LeetCode 105 - Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)
  - 순회 결과를 이용한 분할 정복 트리 복원
- **Tree View Variants:** [LeetCode 103 - Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/) / [LeetCode 199 - Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/description/)
  - BFS 레벨 처리 변형을 통한 시야/순서 문제 대응
- **Graph Topology Insight:** [LeetCode 310 - Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/description/)
  - 리프 제거(Topological Trimming)로 트리 중심 찾기

### 5. 그리디/수학/문자열 응용

- **Greedy Decision:** [LeetCode 134 - Gas Station](https://leetcode.com/problems/gas-station/description/)
  - 누적 손익 관점으로 시작 지점을 찾는 그리디 증명형 문제
- **Math + Parsing:** [LeetCode 12 - Integer to Roman](https://leetcode.com/problems/integer-to-roman/description/)
  - 규칙 기반 변환 테이블 설계와 예외 케이스 처리
- **String Processing:** [LeetCode 28 - Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)
  - 문자열 탐색 기초 구현과 경계값 검증
