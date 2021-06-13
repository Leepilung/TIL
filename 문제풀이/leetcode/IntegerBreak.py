# LeetCode 343. Integer Break 알고리즘
# https://leetcode.com/problems/integer-break/
# n = 2 -> 1+1 , 1x1 =1 // n = 3 -> 1+2, 1x2 = 2 // n = 4 -> 2+2, 2x2 =4 // n = 5 -> 2+3 , 2x3 = 6 // n =6 -> 3+3, 3x3 = 9 
# n = 7 -> 4+3, 4x3 = 12 // n =8 -> 3+3+2, 3x3x2 = 18, n = 9 -> 3+3+3, 3x3x3 = 27 // n = 10 -> 3+3+4 , 3x3x4 = 36
# n = 11 -> 3+3+3+2 , 3x3x3x2 = 54 // n = 12 -> 3+3+3+3 , 3x3x3x3 = 81
# n이 2,3일때 제외하면 규칙성존재. n을 3으로 나눴을때 나머지가 1인경우 3 x a x 4의 형태
# n을 3으로 나눴을때 나머지가 2인경우 3x
# Wrong Answer -> 3일때 2 // 4일때 4 까진 정답. 5일때 2 오답 // 6일때 3 오답 // 7일때 12 오답
# 5일때 6이 나와야함. 5일때 3일떄 3의 0승 x 2. 6일때 3의 2승.
# 테스트케이스 통과. submit 통과. DP로도 풀어봐야하는데.
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return n -1
        if n == 3:
            return n -1
        if n % 3 == 0:
            return 3**(n//3)
        if n % 3 == 1:
            return 3**(n//3-1)*4
        if n % 3 == 2:
            return 3**(n//3)*2