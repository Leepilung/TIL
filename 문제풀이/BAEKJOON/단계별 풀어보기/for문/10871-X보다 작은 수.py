# 백준 알고리즘 - for문 - X보다 작은 수
# https://www.acmicpc.net/problem/10871
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

## 복기할 부분 ----------------
# 문제에서 입력값은 N, X 는 10 5, A는 1 10 4 9 2 3 8 5 7 6의 형태였다.
# A에 대해 처리하는법 연상이 안되서 예전 풀이 참고했음.. 
# 그냥 하나의 입력으로 받고 split()함수로 공백부분을 리스트로 만들

# 숫자 입력이 1 2 3 4 5 6 7 8 9 인경우
# 그냥 A = sys.stdin.readline().split()만 쓰면 각 숫자가 str형태로 list에 담긴다.
# ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 이런형태
# 반대로 A = map(int, sys.stdin.readline().split())으로 사용하면
# 1 2 3 4 5 6 7 8 9의 형태로 저장된다.
# 여기서 A = list(A)하면 int형태의 숫자가 [1,2,3,4,5,6,7,8,9]로 저장된다.
# 맨 마지막에 공백인 " "이 저장되므로 [:-1]까지 해야 공백부분 제외하고 들어감.

import sys
N, X = map(int,sys.stdin.readline().split(" "))
A = map(int, sys.stdin.readline().split())
A = list(A)
answer = ""


for i in range(N):
    if A[i] < X:
        answer += str(A[i])+ " "

print(answer[:-1])