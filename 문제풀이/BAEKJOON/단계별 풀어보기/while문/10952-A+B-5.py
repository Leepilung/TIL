# 백준 알고리즘 - while문 - 10952.A+B - 5 알고리즘
# https://www.acmicpc.net/problem/10952
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력에는 여러 테스트케이스가 한줄로 이뤄져있으며 각줄에 A, B가 각각 주어진다.
# 마지막에 0 0이 입력된다.
# *복기 할 부분*
# 굉장히 쉬운문제이나 한번에 통과 못한점 -> while문 자체를 미사용. + A,B 입력부분을 while문 바깥에서 사용한 점.
# 별거 없으니 신중하게 생각해서 문제 풀기.

while True:
    A, B = map(int,input().split())
    if 0 < A and B < 10:
        print(A+B)
    else:
        break
