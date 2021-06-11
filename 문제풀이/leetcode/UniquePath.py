# LeetCode 62. UniquePaths 알고리즘
# https://leetcode.com/problems/unique-paths/
# 무조건 오른쪽 or 아래로만 이동가능.
# 우측은 무조건 1. 아래쪽으로 이동도 1. 그 사이는 우측이동+아래이동칸의 값.
# 출력하는 맨마지막은 m x n 인덱스면 m-1 x n -1

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for _ in range(n)] for _ in range(m)]
        print(paths)
        for i in range(m):
            paths[i][0] = 1
        for i in range(n):
            paths[0][i] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

        return paths[m-1][n-1]
    
Solution().uniquePaths(3,7)