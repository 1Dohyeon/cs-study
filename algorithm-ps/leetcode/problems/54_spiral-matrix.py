class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        # 1. 사방의 경계선(벽) 인덱스 설정
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        result = []
        
        # 벽들이 서로 엇갈리기 전까지 계속 반복
        # 인덱스이기 때문에 bottom이 top보다 큰게 정상
        while top <= bottom and left <= right:
            
            # 방향 1: 왼쪽에서 오른쪽으로 이동 (맨 위 행 훑기)
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1 # 맨 위 행을 다 읽었으므로 top 벽을 아래로 한 칸 내림
            
            # 방향 2: 위에서 아래로 이동 (맨 오른쪽 열 훑기)
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1 # 맨 오른쪽 열을 다 읽었으므로 right 벽을 왼쪽으로 한 칸 당김
            
            # 방향 3 & 4를 하기 전, 앞선 조작으로 인해 벽이 이미 엇갈리지 않았는지 확인
            if top <= bottom and left <= right:
                
                # 방향 3: 오른쪽에서 왼쪽으로 이동 (맨 아래 행 훑기)
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1 # 맨 아래 행을 다 읽었으므로 bottom 벽을 위로 한 칸 올림
                
                # 방향 4: 아래에서 위로 이동 (맨 왼쪽 열 훑기)
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1 # 맨 왼쪽 열을 다 읽었으므로 left 벽을 오른쪽으로 한 칸 당김
                
        return result