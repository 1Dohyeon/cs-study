from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
           return None
       
        old_to_new = {}
        old_to_new[node] = Node(node.val)
        q = deque([node])
    
        while q:
            curr = q.popleft()
            
            # 현재 노드(curr)의 이웃들을 확인
            for neighbor in curr.neighbors:
                # 1. 이웃 노드가 처음 발견된 것이라면 복제본 생성
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                
                # 2. 현재 노드의 복제본에 이웃의 복제본을 연결
                # (이미 생성되었든 방금 생성했든 딕셔너리에서 꺼내서 연결 - 선(Edge)은 아직 긋지 않았기 때문)
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
                
        return old_to_new[node]

        # def dfs(node):
        #        # 이미 복제된 노드라면 기존 복제본 반환
        #        if node in visited:
        #            return visited[node]

        #        # 새로운 노드 생성 (값만 복사)
        #        clone = Node(node.val)
        #        visited[node] = clone

        #        # 이웃들을 재귀적으로 복제하여 연결
        #        for neighbor in node.neighbors:
        #            clone.neighbors.append(dfs(neighbor))

        #        return clone

