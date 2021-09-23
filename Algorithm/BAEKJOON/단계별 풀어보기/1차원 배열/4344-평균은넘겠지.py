# 백준 알고리즘 - 1차원 배열 4344. 평균은 넘겠지
# https://www.acmicpc.net/problem/4344
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 복기할 부분
# 우선 가장 중요한 부분. 출력을 40.000% 와 같이 소수점 표현을 해야하는데 
# 이때 사용해야 하는게 format 함수를 이용한 표현법이다. 
# "{:.3F}%" 이렇게 하면 highscore의 3자리수까지 float형으로 표시해준다.
# 그리고 가장 크게 실수한 부분이 nums[0]와 C값을 혼동해서 사용한 부분이다.

C = int(input())
n = 1
while n < C+1:
    nums = list(map(int,input().split()))
    equal = sum(nums[1:])/nums[0]
    highscore = 0
    for i in range(1,nums[0]+1):
        if nums[i] > equal:
            highscore += 1
    highscore = highscore / nums[0] * 100 
    n += 1
    print("{:.3F}%".format(highscore))


# 다른 풀이 ---------------
# 자잘구레한 컴파일 에러만 아녔으면 바로통과했을 문제.
# 천천히 봐야하지만 풀어야할 양이 많다보니 그렇게 안되는것같음. 최대한 신중히 풀면 한방에 패스될듯.

import sys

C = int(sys.stdin.readline())
n = 1
while n <= C: 
    N = list(map(int, sys.stdin.readline().split()))
    number = N.pop(0)
    equal = sum(N) / number
    topTier = 0

    for i in N:
        if i > equal:
            topTier += 1
            
    ratio = topTier/number*100
    print('%.3f'%ratio+'%')
    n +=1