# LeetCode 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/
# m x n 배열이 주어지면 좌측 상단에서부터 우측하단 끝까지 이동하면서 주어진 숫자의 합계가 가장 작은 path를 찾야아함.
# 아래쪽 or 오른쪽으로만 이동이 가능하다.
# 배열의 규칙성 찾기. Unique Path와 형태는 유사하나 규칙성은다름.
# 우측진행, 아래 진행은 바로 앞의 인덱스 가산하는 방식이면 끝.
# 1,1 1,2, 2,1, 2,2와 같은 부분의 규칙성 찾아야함. 뭐지?
# 기존값 + 기존값 위치의 왼쪽 or 위쪽 인덱스 둘중 작은값 더하면 됨.
# 테스트케이스 2번 실패 인덱스에러 -> x y 반전시켜야함. 
# return 부분 인덱스 에러 -> grid y x 순으로 똑같이 반전해야함
# 통과.

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        x = len(grid[0])
        y = len(grid)
     
        for i in range(1,x): 
            grid[0][i] += grid[0][i-1]
        for i in range(1,y):
            grid[i][0] += grid[i-1][0]

        for i in range(1,y):    
            for j in range(1,x):   
                grid[i][j] += min(grid[i][j-1],grid[i-1][j])

        return grid[y-1][x-1]