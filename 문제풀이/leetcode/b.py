# 테스트케이스 1통과
# 2 index 에러. 디버깅 -> x, y 반대로. -> x, y 좌표말고 그냥 변수로 생각.

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        x = len(grid[0])
        print('x = ',x)
        y = len(grid)
        print('y =',y)
        # 둘다 y = 2 x =3
        for i in range(1,x): #1~2까지 출력.
            grid[0][i] += grid[0][i-1]
        print('x축',grid)
        for i in range(1,y):
            grid[i][0] += grid[i-1][0]
        print('y축',grid)

        for i in range(1,y):    # y = 2 -> 1만 출력
            for j in range(1,x):    # x =3 -> 1, 2 출력. 
                grid[i][j] += min(grid[i][j-1],grid[i-1][j])
        print('xy축',grid)

        return grid[y-1][x-1]

Solution().minPathSum([[1,2,3],[4,5,6]])