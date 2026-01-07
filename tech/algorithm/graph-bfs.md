# Graph BFS

## BFS (Breadth-First Search) 개요

BFS는 **'너비 우선 탐색'** 으로, 시작 노드에서 가까운 노드부터 차례대로 그래프의 모든 정점을 탐색하는 알고리즘입니다. 마치 물에 돌을 던졌을 때 파동이 사방으로 퍼져나가는 것과 같은 방식으로, 현재 노드와 인접한 노드(1촌)를 모두 방문한 뒤 그다음 거리의 노드(2촌)들로 넘어갑니다. 주로 두 노드 사이의 최단 경로를 찾을 때 유리하며, 선입선출(FIFO) 방식의 큐(Queue) 자료구조를 사용하여 구현합니다.

## Python으로 BFS 구현

### 0. dictionary로 그래프 표현

```python
graph = {}

# 아래와 같이 입력을 받았다고 가정
# v = [[1, 3], [2, 5], [1, 5], [3, 4], [1, 4]]

for e in v:
    if e[0] not in graph:
        graph[e[0]] = []
    if e[1] not in graph:
        graph[e[1]] = []
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])
    
print(graph)
# 출력 결과: {1: [3, 5, 4], 3: [1, 4], 2: [5], 5: [2, 1], 4: [3, 1]}

```

- 딕셔너리의 키를 노드로, 리스트를 연결된 인접 노드로 활용하여 그래프의 인접 리스트 구조를 생성합니다.
- `if`문을 통해 노드 존재 여부를 확인하고 초기화하며, 양방향 간선 정보를 모두 추가하여 무방향 그래프를 완성합니다.

### 1. BFS 함수 구현

```python
def bfs(graph, start):
    # 필요 변수 선언
    visited = set()
    result = []
    queue = deque([start])

    # 방문 및 결과에 시작 노드 삽입
    visited.add(start)

    # 큐(Queue)가 비워질 때까지 반복: 
    # 현재 노드의 방문하지 않은 모든 이웃을 큐에 넣어 '다음 단계' 탐색 후보로 예약
    # 이 과정을 통해 시작점에서 가까운 노드부터 층별로 탐색하여 너비를 우선적으로 확장
    while queue:
        # 1. 큐에서 가장 오래된 노드를 꺼냄 (FIFO)
        node = queue.popleft()
        # 2. 실제로 방문한 시점에 결과 리스트에 기록
        result.append(node)

        # 3. 현재 노드와 연결된 이웃들 확인
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                # 4. 방문하지 않은 노드라면 방문 처리 후 큐에 삽입 (방문 예약)
                queue.append(neighbor)
                visited.add(neighbor)

    return result
```

### 2. 실행

```python
# 함수를 호출하여 리스트 타입의 결과를 변수에 할당
result = bfs(graph, 1) # 1부터 시작한다고 가정
print(result)
# 출력 결과 (방문 순서): [1, 3, 5, 4, 2] (그래프 삽입 순서에 따라 달라질 수 있음)
```

> 0번에서 생성된 그래프를 사용합니다.