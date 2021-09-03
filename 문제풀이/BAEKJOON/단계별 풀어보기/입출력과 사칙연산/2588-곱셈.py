# 백준 알고리즘 - 입출력과 사칙연산- 2588. 곱셈
# https://www.acmicpc.net/problem/2588
# 세자리수 x 세자리수 의 곱셈 과정에서 각 자리에 출력되어야 하는 숫자를 출력하도록 해야함.
# https://www.acmicpc.net/upload/images/f5NhGHVLM4Ix74DtJrwfC97KepPl27s%20(1).png 
# 과정 (3)부터는 첫 세자리수와 두번째 세자리수의 첫째자리, (4)는 둘째자리 (5)는 셋째자리의 숫자와 계산한 값이고 마지막에는 A*B이 들어가야 한다.
# *복기 부분*
# 쉬운 문제이나 너무 성급하게 풀어서 단번에 제출하는데 실패하였다.
# 우선 입력을 따로따로 받기 때문에 input을 따로 써도 됨. 그리고 각 자리수와 곱을 따로해야 하기 때문에 두번째 3자리수를 리스트로 바꿔야한다.
# int형으로 입력 받은경우 list로 분배하려면 str형으로 형태를 바꿔줘야 한다.
# 각 자리수와 곱(*)하려면 int형 * int형의 형태가 되야 하므로 리스트 B1의 값(str)을 int형으로 다시 형변환 시켜야함.

A = int(input())
B = int(input())
B1 = list(str(B))
print(A*int(B1[2]))
print(A*int(B1[1]))
print(A*int(B1[0]))
print(A*B)

# ---------------------------------------
# 다른 풀이

# 복기해야할 부분
## 문자형 전환(str)만 사용하면 되는 간단한 문제.
## 기존보다 나은 풀이라고 생각됨(list로 만들필요가 없음) 그러나 한번에 풀지 못했음.

import sys
num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())

num2 = str(num2)

print(num1*int(num2[2]))
print(num1*int(num2[1]))
print(num1*int(num2[0]))
print(num1*int(num2))
