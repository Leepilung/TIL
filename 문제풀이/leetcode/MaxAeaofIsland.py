# LeetCode Max Area of Island 알고리즘
# https://leetcode.com/problems/max-area-of-island/
# 섬은 1로 되어있고, 섬중에서 가장 큰 섬의 크기를 구하라.
# 섬을 돌면서 1을 전부 끄고 1을 끌때마다 섬의 크기를 스택에다가 넣는 방식으로
# 스택 가산하는 방식 채용. 선언된 함수에서 설정된 변수를 다른 함수에서 사용하고 싶을경우 self. 구문 붙여줘야함.
# NumberofIsland와 거의 유사한 템플릿.

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.stack = []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    self.count = 0
                    self.islandCount(y,x,grid)
        if len(self.stack) == 0:
            return 0
        return max(self.stack)
    
    def islandCount(self, y, x ,grid): #상 하 좌
        if y >= len(grid):
            return
        if y < 0:
            return
        if x >= len(grid[0]):
            return
        if x < 0:
            return
        if grid[y][x] != 1:
            return
        self.count += 1
        grid[y][x] = 'x'
        self.islandCount(y+1,x,grid)
        self.islandCount(y-1,x,grid)
        self.islandCount(y,x-1,grid)
        self.islandCount(y,x+1,grid)
        self.stack.append(int(self.count))