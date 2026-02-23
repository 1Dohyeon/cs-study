""" https://leetcode.com/problems/zigzag-conversion/description/
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        s_list = ["" for _ in range(numRows)]
        d = 1
        cur_idx = 0

        for i in s:
            s_list[cur_idx] += i

            if cur_idx == 0:
                d = 1
            elif cur_idx == numRows - 1:
                d = -1

            if d == 1:
                cur_idx += 1
            elif d == -1:
                cur_idx -= 1

        result = ""
        for i in s_list:
            result += i

        return result

    def convert(self, s: str, numRows: int) -> str:
        # 1. 예외 처리: 행이 1개거나 문자열보다 행이 많으면 변환이 필요 없음
        if numRows == 1 or numRows >= len(s):
            return s
        
        # 2. 각 행을 담을 리스트 (문자열 대신 리스트에 담아 join하는게 효율적)
        rows = [''] * numRows
        cur_idx = 0
        step = 1  # 1이면 아래로, -1이면 위로 이동
        
        for char in s:
            rows[cur_idx] += char
            
            # 3. 양 끝(0번 행 또는 마지막 행)에 도달하면 방향 전환
            if cur_idx == 0:
                step = 1
            elif cur_idx == numRows - 1:
                step = -1
                
            cur_idx += step
            
        # 4. 모든 행을 하나로 합침
        return "".join(rows)