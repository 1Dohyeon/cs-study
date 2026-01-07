# Graph DFS

## DFS (Depth-First Search) 개요
DFS는 '깊이 우선 탐색'으로, 그래프나 트리에서 한 경로를 선택해 갈 수 있는 가장 깊은 곳까지 탐색한 뒤, 더 이상 갈 곳이 없으면 마지막 갈림길로 돌아와 다른 경로를 탐색하는 알고리즘입니다. 미로 찾기에서 일단 한 길로 끝까지 가본 뒤 막히면 돌아오는 방식과 같으며, 주로 재귀 함수나 스택(Stack) 자료구조를 사용하여 구현합니다.

## Python으로 DFS 구현

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

### 1. DFS 함수 구현

```python
def dfs(graph, start_node):
    visited = set()
    result = []

    def _dfs(node):
        visited.add(node)
        result.append(node)

        for neighbor in graph.get(node, []): # .get()을 통해 node가 graph에 없더라도 빈배열 반환 --> keyError 방지
            if neighbor not in visited:
                # 방문하지 않은 노드가 있다면 깊게 탐색 (Recursive Call)
                _dfs(neighbor)
    
    _dfs(start_node)
    return result
```

- 현재 노드를 방문 처리함과 동시에 결과 배열에 기록하고, 연결된 인접 노드들을 차례대로 확인합니다.
- `.get()` 메서드로 안전하게 인접 노드 리스트를 가져오며, 방문하지 않은 노드를 발견하면 재귀 호출을 통해 즉시 더 깊은 단계로 진입합니다.

### 2. 실행

```python
# 함수를 호출하여 리스트 타입의 결과를 변수에 할당
result = dfs(graph, 1)  # 1부터 시작한다고 가정
print(result)
# 출력 결과 (방문 순서): [1, 3, 4, 5, 2] (그래프 삽입 순서에 따라 달라질 수 있음)
```

- `result = dfs(graph, 1)`과 같이 시작 노드를 전달하여 호출하면 탐색된 순서가 리스트로 반환됩니다.

