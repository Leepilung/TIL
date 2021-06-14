# LeetCode 1277. Count Square Submatrices with All Ones
# m x n 꼴로 0과 1로된 행렬이 주어지면 모든 행렬을 포함하는 하위 제곱 행렬의 수를 구해야 함.
#Input: matrix = 일때 Output은 15.
#[[0,1,1,1],    1로된 길이가 1인 square의 수는 10
# [1,1,1,1],    1로된 길이가 2인 square의 수는 4
# [0,1,1,1]]    1로된 길이가 3인 square의 수는 1  도합 15.
# 카운트하는 별도의 함수명 사용해보기. -> 길이가 3이상인 변 카운트하는 함수를 전부 개별로 해야되서 삭제.
# Unique Path or Minimum path sum이랑 비슷하게 생각해보기
# 각각 0열은 고정. 2x2에서 1111이면 길이가 2인 변이 되므로 카운트. 3도 3x3에 전부 1이면 카운트.
# 규칙성 발견. example 1에서 길이 2인부분 3인부분을 체크했을때 배열을 다음과 같이 바꿀 수 있음.
# 0111  
# 1122  -> 2x2 형태의 맨끝변 (1,2) (1,3)을 2로 표시 가능.
# 0123  -> 3x3이 되는 맨끝변의 값을 3으로 해도 개수 세는데 동일. 1이상인 값 + 2 이상인 값+ 3이상인 값 -> 15
# 그냥 안에 숫자 다 더해도 15. (1,1)은 (0,0), (0,1), (1,1)중에 가장 작은 값+ 원래(1,1)의 값 -> 가장 최근에 풀었던 문제랑 동일(Set matrix Zeros)


from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] ==  1:
                    if i == 0 or j == 0:
                        count +=1
                    else:
                        matrix[i][j] = min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1]) + matrix[i][j]
                        count += matrix[i][j]
        return count