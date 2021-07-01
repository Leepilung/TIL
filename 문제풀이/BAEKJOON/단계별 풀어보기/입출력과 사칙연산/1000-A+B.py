# 백준 알고리즘 - 입출력과 사칙연산 - 1000. A+B 알고리즘
# https://www.acmicpc.net/problem/1000
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어지면 A+B를 출력시켜야함ㄷ
# * 주의할 점
# 입력이 1 2인데 1따로 2따로가 아니다. 한줄에 1 2를 입력해서 A+B를 출력시켜야 함.
# 입력의 형태를 신경써야하는 문제

C=input().split()
A=int(C[0])
B=int(C[1])
print(A+B)

# C = input().split()
# -> 입력값만큼 ex) 1 2 3 공백을 기준으로 split해서 리스트로 만들어줌. -> [1,2,3]으로 출력됨
# 이 풀이가 좀 더 유연하게 이용 가능.(인수가 늘어도 대처가 더 쉬움)

# 또 다른 풀이
# -> 입력값을오 2개의 변수 a, b를 입력받음.
# ex) 1 2 입력할 시 공백을 기준으로 [1, 2]로 나뉘고 a, b 두개의 변수만을 지정하였으므로 1 2 3 처럼 입력시 에러발생.
a,b = input().split()
a = int(a)
b = int(b)
print(a+b)