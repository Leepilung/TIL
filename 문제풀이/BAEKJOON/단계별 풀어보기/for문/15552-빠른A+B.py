# 백준 알고리즘 - for문 - 15552.빠른 A+B
# https://www.acmicpc.net/problem/15552
# 8393.합 문제와 비슷해보이나 주어지는 조건때문에 풀이가 아예 달라지는 문제.
# * 복기 사항 *

# 우선 합문제와 유사해 보이나 아예 다름. 문제에 주어지는 제한사항에서 주어지는 양식을 사용하지 않으면 시간초과 발생
# sys사용하기 때문에 import sys 필수. 그리고 입력의 형태가 20 30 과같이 이어지는 형태이므로 map함수 사용하여
# split(' ')으로 A,B 값을 각각 지정해준다. map 함수는 map(형태, 함수) -> 함수로 입력받은 값을 '형태'에 맞춰서 변환시키는 함수
# 문제는 map이 내장함수라는 점인데


import sys
T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split(" "))
    print(A+B)