# LeetCode 73. Set Matrix Zeroes 알고리즘
# https://leetcode.com/problems/set-matrix-zeroes/
# Do not return anything, modify matrix in-place instead. 주의하기.
# matrix = [[1,1,1], 일경우     [[1,0,1], 와 같이 바꿔야함.
#           [1,0,1],            [0,0,0],
#           [1,1,1]]            [1,0,1]]
# b.py에서 실험 끝.
# 그러나 속도가 너무 느림. 개선필요. 이중 for문에 while문써서 그럼.
# 다른 풀이 고안.
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    index.append((i,j))

        while len(index) != 0:
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    matrix[i][index[0][1]] = 0
                    matrix[index[0][0]][j] = 0
            index.pop(0)

#-------------------------------------------------------------------------------------------------------
class Solution2:
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        column = set()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    column.add(j)

        for i in list(rows):
            for j in range(n):
                matrix[i][j] = 0
        
        for i in range(m):
            for j in list(column):
                matrix[i][j] = 0