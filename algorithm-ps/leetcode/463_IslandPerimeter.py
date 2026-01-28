""" https://leetcode.com/problems/island-perimeter/description/?envType=problem-list-v2&envId=depth-first-search
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
"""
from typing import List

class Solution:
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     # 물과 닿는 면적 개수는 4 - edge
        
    #     # 반복문으로 구현
    #     perimeter = 0
    #     rows, cols = len(grid), len(grid[0])

    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 1:
    #                 edges = 4
                    
    #                 # grid 범위 내에서 인접한 땅이 있는지 확인
    #                 # 상
    #                 if r > 0 and grid[r - 1][c] == 1:
    #                     edges -= 1
    #                 # 하
    #                 if r < rows - 1 and grid[r + 1][c] == 1:
    #                     edges -= 1
    #                 # 좌
    #                 if c > 0 and grid[r][c - 1] == 1:
    #                     edges -= 1
    #                 # 우
    #                 if c < cols - 1 and grid[r][c + 1] == 1:
    #                     edges -= 1
                    
    #                 perimeter += edges
    #     return perimeter

        # DFS로 구현
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 1 # 물이나 경계를 만나면 둘레 +1
            if grid[r][c] == -1:
                return 0 # 이미 방문한 땅은 둘레에 영향 없음
            
            grid[r][c] = -1 # 방문 처리
            return dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # 섬이 하나이므로, 여기서 반환되는 값이 곧 전체 둘레
                    return dfs(r, c)