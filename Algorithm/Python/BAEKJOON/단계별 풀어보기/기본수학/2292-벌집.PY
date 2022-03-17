# 백준 알고리즘 - 기본수학 - 2292.벌집
# https://www.acmicpc.net/problem/2292
# 이 문제는 바로 풀었으나 TIL 업로드겸 수학 수식활용하는 문제파트인지라 정리해본다.
# 문제 링크에서와 같이 육각형으로 이뤄진 벌집이 있다.중앙의 방 부터 1씩 증가해서 번호를 매긴다.
# 숫자 N이 주어졌을 때 벌집 중앙 1 번에서 n번방 까지 최소 몇개의 방을 거쳐 지나가는지 계산하는 프로그램을 짜라.


# 규칙성(등차수열) 1 -> 7(6) -> 19(12) -> 37(18) -> 61(24)
Nums = int(input())
A = 1
B = 7
N = 0
n = 1
while True:
    if Nums == 1:
        print(1)
        break
    if A < Nums <= B:
        n +=1
        print(n)
        break
    else:
        n +=1
        N = 6*n
        A = B
        B = B + N