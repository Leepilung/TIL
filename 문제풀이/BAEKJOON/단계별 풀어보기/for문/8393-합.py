# 백준 알고리즘 - for문 - 8393. 합 알고리즘
# https://www.acmicpc.net/problem/8393
# n이 주어졌을 때, 1부터 n까지의 합을 구하는 프로그램을 작성하시오.
# * 복기할 부분 *
# 아주 아주 아주 아주 쉬운 문제이나 바로 테스트에 통과하지 못한 이유는
# for문에서 별도로 sum같은 함수를 안만든채로 i += i 같은 말도 안되는 짓거릴 했기 때문이다.
# 변수 설정에 유의하자.


while True:
    n = int(input())
    if 1 <= n <= 10000:
        break
    else: continue

sum = 0
for i in range(1,n+1):
    sum += i
print(sum)