# 백준 알고리즘 - if문 - 2753. 윤년
# https://www.acmicpc.net/problem/2753
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

# 아주 간단한 문제. 바로 통과못했던 간과한점 ->  조건문을 2중으로 썼으나 else문을 oddYear % 4 == 0:일때만 넣었음.
# if문에 else문 여러번 사용하도록 하는것 주의하기.
# 입력부분을 굳이 범위 제한 루프문써서 구현 안해도 통과됨. -> 문제있지않나 ㅋㅋ


while True:
    oddYear = int(input())
    if 4000 >= oddYear >= 1:
        break
    else:
        continue
    
if oddYear % 4 == 0:
    if oddYear % 100 != 0 or oddYear % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)
# --------------------------------------------------------
# 다른 풀이
## 복기 사항
## 기존에 풀었던 풀이가 훨씬 깔끔함.. 조건문의 or문 사용 기억하기.
## 구문 단축 가능함 + 변수명 통일화 같은 단순한 실수 줄이기.
import sys
while True:
    oddYear = int(sys.stdin.readline())
    
    if 0 < oddYear < 4001:
        break
    else:
        continue

if oddYear % 4 == 0:
    if oddYear % 100 != 0:
        print(1)
    else:
        if oddYear % 400 == 0:
            print(1)
        else:
            print(0)
else:
    print(0)
