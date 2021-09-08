# 백준 알고리즘 - 문자열 - 2675.문자열 반복
# https://www.acmicpc.net/problem/2675
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 
# 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# * 복기해야할 부분
# 입력 조건을 제대로 안보고 대충풀었음 그래서 N을 따로 구현안했음<- 문제를 제대로 꼼꼼히 읽자.
# while문 조건식 제대로 파악하기. n = 0으로 잡아두고 n에 1씩 가산했을떄 종료조건 n<2로 해두면
# n이 0, 1일때까지만 반복. 매번 테스트 별도로 해야되므로 기억해두자.


N = int(input())
n = 0
while n < N:
    word = input().split()
    word[0] = int(word[0])
    result = ''
    if len(word) != 1:
        for i in word[1]:
            result += i * word[0]
    n += 1
    print(result)

## 다른 풀이
# 바로 통과했음. 기존풀이보다 시간자체는 빨라졋는데 input대신인가 모르겠음.

import sys
T = int(sys.stdin.readline())
n = 1

while n <= T: 
    R,S = sys.stdin.readline().rstrip().split(" ")
    S = list(S)
    sum = ''
    for i in range(len(S)):
        sum += S[i]*int(R)
    print(sum)
    n +=1