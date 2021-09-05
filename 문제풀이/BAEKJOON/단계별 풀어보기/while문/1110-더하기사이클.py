# 백준 알고리즘 - while문 - 1110. 더하기사이클 
# https://www.acmicpc.net/problem/1110
# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 

# *복기해야할 부분
# 시간초과가 계속 떠서 애먹은 문제. 원인은 int->str ->int등으로 형변환 자체가 시간을 너무잡아먹었기 때문.
# 10의자리 + 1의자리 한것과 1의자리를 합쳐서 새로운 숫자를 만들고 이걸 반복했을때 나오는 값이 원래 기존값과 같으면 종료
# 반복문 종료조건, 사이클 재는등은 거진 다똑같았으나 //10, %10을 활용하는 것을 간과했음.
N = int(input())
check = N
new_N = 0
temp = 0
cycle = 0
while True:
    temp = N//10 + N%10
    new_N = (N%10)*10 + temp%10
    cycle += 1
    N = new_N
    if new_N == check:
        break
print(cycle)

#-----
# 새로 푼 풀이
# 기존풀이를 보니 새로운 풀이가 굉장히 더럽다. 굳이 str-> int형 형변환 메소드를 안써도 될듯.
# 단순히 10자리와 1의자리를 몫과 나머지를 구하는기호로 간략화 가능함 
# 시도 횟수 자체는 줄었으나 코드 간략화가 가능하다는 점에서 반성할 필요가 많은듯.

import sys
N = int(sys.stdin.readline())
cycle = 0
Ori_N = N
while True:
    if 0 <= N <= 99:
        if N < 10:      # N = 5 
            N = '0' + str(N)     # 05
            A = int(N[-2])+int(N[-1]) # A = 5
            N = int(N[-1] + str(A)[-1])  # N = 55
            cycle += 1
        else:
            N = str(N) # 50
            A = int(N[-2])+int(N[-1]) #  5+0 = 5
            N = int(N[-1] + str(A)[-1])  # 5
            cycle += 1

    if N == Ori_N:
        print(cycle)
        break

