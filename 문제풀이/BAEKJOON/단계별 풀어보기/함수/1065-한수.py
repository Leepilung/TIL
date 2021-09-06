# 백준 알고리즘 - 함수 - 1065. 한수
# https://www.acmicpc.net/problem/1065
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
# 입력 - 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

# * 복기할 부분 *
# 함수 파트로 와서 한번에 통과하는 경우가 대폭줄었다.
# 실제로 def을 사용한 함수 선언 문제는 아닌게 좀 웃기지만 이번 풀이는 어려운것도 아니고 연상도 어렵지 않았으나
# 바로 통과하지 못한 이유는 else 구문에 hansoo값에 99를 더하는걸 까먹은점 + for문 범위를 N+1로 해야되는데 N으로 한점
# 때문에 바로 통과하지 못했다. 좀 더 꼼꼼히 푸는 연습을 하도록 하자.
N = int(input())
hansoo = 0
if N <= 99:
    hansoo = N
else:
    hansoo += 99
    for i in range(100,N+1):
        first = int(str(i)[0])-int(str(i)[1])
        second = int(str(i)[1])-int(str(i)[2])
        if first == second:
            hansoo +=1
        else: continue
print(hansoo)


# 다른 풀이
# 위의 풀이는 함수문제인데 함수형태를 아예안사용하고 푼걸보니 어떻게 풀었는지 끔찍하다.
# 문제에서 주어진 한수의 정의가 해깔려서 별도로 검색하고 풀었음..
# 한방에 패스하긴 했으나 기존 풀이가 너무 맘에안들어서 별도로 풀이 기입.

import sys
N = int(sys.stdin.readline())

def Hansoo (N):
    num = 0
    if N >= 100:
        num += 99
        for i in range(100,N+1):
            N = list(str(i))
            a = int(N[0])-int(N[1])
            b = int(N[1])-int(N[2])
            if a == b:
                num +=1
    else: # N < 100
        num = N
    print(num)

Hansoo(N)