# 백준 알고리즘 - 문자열 - 1316. 그룹 단어 체커
# https://www.acmicpc.net/problem/1316
# 한번에 통과를 못했음. 기존에 check = []로 확인하던 부분이 dic = {}으로 되어있었는데
# 딕셔너리에 -> 리스트로 바꾸니까 통과함. 기존엔 오히려 딕셔너리로 통과했는데 의아함.

import sys
N = int(sys.stdin.readline().strip())
n = 1
check = []
ans = 0

while n <= N:
    text = list(str(sys.stdin.readline().strip()))
    count = 0
    n += 1

    for i in range(len(text)): # happy
        if text[i] not in check:
            check.append(text[i])
            count +=1
            continue
        if text[i] in check and text[i-1] == text[i]:
            count +=1

    if count == len(text):
        ans += 1
    check = []

print(ans)