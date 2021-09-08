# 백준 알고리즘 - 문자열 - 11654.아스키코드
# https://www.acmicpc.net/problem/11654

# 틀린점

# 아주 간단한 문제였는데 풀이에 유의해야할 부분이 있다.
# input과 다르게 import sys -> sys.stdin.readline으로 하면 끝에 개행문자가 같이 삽입된다.
# rstrip()으로 개행문자를 없애줘야 ord 메소드가 정상작동함.
# (안하면 매개변수로 길이2이상의 스트링이 입력됐다고 뜸)
import sys
N = str(sys.stdin.readline().rstrip())

print(ord(N))