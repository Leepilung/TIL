# 백준 알고리즘 - 기본 수학 1단계 - 손익분기점
# https://www.acmicpc.net/problem/1712
# A는 고정비용, B는 가변비용 이라고 할 때 노트북 판매 가격이 C이면
# 총 수입이 총 비용보다 많아지는 지점을 손익분기점이라고 할 때 손익분기점을 출력해야함.

# A -> 고정비용 B -> 가변비용 A+B -> 노트북 생산 비용
# C -> 노트북 가격
# 손익분기점 BP(Break Point) A+B*n > C*n.
# 틀린부분 -> 0을 포함안시켜서 Zero division Error 발생했음.
# 잘한 부분 -> while문으로 단순계산하면 21억까지 n번출력해야되서 무조건 시간초과 나는걸 생각하고 수학식을 생각하고 계산했음.

A,B,C = map(int,input().split())
BP = 0
if C-B <= 0:
    BP = -1
else:
    BP = (A // (C-B)) + 1 
    
print(BP)

# 다른 풀이
# 오히려 과거가 더 간단하게 풀었음. 너무 급하게 풀었던 문제.
# 접근도 이상했다. while문 사용하는 방법으로 복잡하게 생각했음.
import sys

A, B, C = map(int,sys.stdin.readline().rstrip().split(" "))
BP = 0
if B > C or B-C == 0:
    print(-1)
else:
    BP = A//(C - B)
    n = BP + 1
    print(n)