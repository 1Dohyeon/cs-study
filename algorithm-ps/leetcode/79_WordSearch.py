""" https://leetcode.com/problems/word-search/description/?envType=problem-list-v2&envId=depth-first-search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""


from typing import Counter, List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [] # 방문한 노드의 인덱스를 (i, j) 형태로 담음

        m = len(board)
        n = len(board[0])

        # 글자 수가 보드판 칸 수보다 많으면 당연히 불가능 
        if m * n < len(word):
            return False
        
        # 단어에 있는 각 알파벳과 보드에 존재하는 각 알파벳 수를 비교
        # ex: 보드판에 있는 'A'가 2개뿐인데 단어엔 'A'가 3개 필요하다면, 불가능
        count = Counter(sum(board, []))
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
        
        def _dfs(i, j, k):
            # 단어의 모든 글자를 찾았을 때
            if k == len(word):
                return True
            # 인덱스가 보드판 범위를 벗어났을 때
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            # 이미 방문한 노드이거나, 글자가 일치하지 않을 때
            if (i, j) in visited:
                return False
            # 글자가 일치하지 않을 때
            if board[i][j] != word[k]:
                return False
            
            visited.append((i, j))
            res = _dfs(i+1, j, k+1) or _dfs(i-1, j, k+1) or _dfs(i, j+1, k+1) or _dfs(i, j-1, k+1)
            visited.pop() # False로 돌아왔을 때 방문 기록을 지워줘야 다른 경로에서 다시 방문 가능
            return res
        
        for i in range(m):
            for j in range(n):
                if _dfs(i, j, 0):
                    return True
                
        return False