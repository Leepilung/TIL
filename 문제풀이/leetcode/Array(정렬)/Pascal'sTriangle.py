# LeetCode 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
# 정수 numRows이 주어지면 그 정수의 크기만큼 2중배열 생성
# 그리고 그 안의 수는 파스칼의 삼각형(가운데는 그위의 2개의 합) 규칙성으로 채워야 함
# 0, 1일때는 [1], [1,1] 고정이고 스택형태로 쌓아야 하기때문에 for문 사용+ 2중 for문으로
# index가 0일때랑 끝일때 1, 나머지는 규칙성에 따라 기입하도록 짰음
# 쉬운 문제였으나 이중배열 부분에서 살짝 해맸던 문제.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i = 0
        tri = [[] for i in range(numRows)]
        # ex 기준 tri = [[],[],[],[],[]]
        # [1] [1,1] [1,2,1] [1,3,3,1] [1,4,6,4,1]
        if numRows == 1:
            tri[0] = [1]
        if numRows == 2:
            tri[0] = [1]
            tri[1] = [1,1]
        if numRows > 2:
            tri[0] = [1]
            tri[1] = [1,1]
            for i in range(2,numRows):
                for j in range(i+1):
                    if j == 0:
                        tri[i].append(1)             
                        
                    if j != 0 and j != i:
                        tri[i].append(tri[i-1][j-1]+tri[i-1][j])
                    
                    if j == i:
                        tri[i].append(1)
                
        return tri