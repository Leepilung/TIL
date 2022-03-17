# LeetCode Number of Islands 알고리즘 문제
# https://leetcode.com/problems/number-of-islands/
# m x n의 2중 배열 grid가 주어지면 1로 되있는 부분은 섬, 0으로 되있는 부분은 물이다.
# 이때 섬(1)의 개수를 구해야 하는 알고리즘 문제. 8퀸 문제를 사용해서 풀어야한다.
# ex) Input: grid = [               Input: grid = [
#  ["1","1","1","1","0"],             ["1","1","0","0","0"],
#  ["1","1","0","1","0"],             ["1","1","0","0","0"],
#  ["1","1","0","0","0"],             ["0","0","1","0","0"],
#  ["0","0","0","0","0"]              ["0","0","0","1","1"]
# ]    Output: 1                      ]     Output : 3
# 1인 부분을 만났을때 재귀함수로 대각선을 제외한 상하좌우가 1인 부분을 싹다 지우고 Answer에 +1 가산되도록 해야한다.

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        for y in range(len(grid)):              # len(grid) -> grid의 원소 갯수 4 출력  0~3
            for x in range(len(grid[0])):       # 여기서 len(grid[0])면 5가 출력 0~4
                if grid[y][x] == '1':           # grid[y][x]의 값이 1일 경우 answer 1씩 가산 
                    answer +=1
                    self.count(y,x,grid)        # 그 후 상하좌우 1값지우는 재귀함수
        return answer
    
    def count(self, y, x, grid):
        if x > len(grid):       # x 3이상일 경우 재귀 종료
            return
        if x < 0:               # x 0이하일 경우 재귀 종료
            return       
        if y > len(grid[0]):    # y 4이상일 경우 재귀 종료
            return
        if y < 0:               # y 0이하일 경우 재귀 종료
            return
        if grid[y][x] == '0':
            return
        self.count(y+1,x,grid)  # 상
        self.count(y-1,x,grid)  # 하
        self.count(y,x-1,grid)  # 좌
        self.count(y,x+1,grid)  # 우
