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