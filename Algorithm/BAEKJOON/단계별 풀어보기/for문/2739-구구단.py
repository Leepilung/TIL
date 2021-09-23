# 백준 알고리즘 for문 - 구구단
# https://www.acmicpc.net/problem/2739
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

# 복기할 부분------
# f 문자열 포매팅 활용하여 푸는 문제.
# 파이썬 f 문자열 포매팅을 기억못하고 format함수 사용법만 어설프게 기억하는 바람에 틀린 문제.
# 틀린김에 문자열 포매팅 복습 별도로 진행함.
# format 함수 사용한 식으론 곱셉연산 처리가 불가능했음 

import sys
while True:
    N = int(sys.stdin.readline())
    if 0 < N < 10:
        break
    else: continue

for i in range(1,10):
    print(f'{N} * {i} = {N*i}')