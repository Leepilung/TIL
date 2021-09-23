# BaekJoon - 문자열 - 1157. 단어공부
# https://www.acmicpc.net/problem/1157

# 한번에 풀이 성공 했으나 풀이에 시간이 좀 걸렸음.
# 단축시킬 곳이 있나 확인해서 줄여보기.

import sys

N = list(str(sys.stdin.readline().rstrip()).upper())
num = {}

for i in N:
    if i not in num:
        num[i] = 1
    else:
        num[i] += 1

max = max(num.values())
max_count = 0

for i in num:
    if num[i] == max:
        max_count += 1

list_of_key = list(num.keys())
list_of_value = list(num.values())
answer = list_of_value.index(max)

if max_count != 1:
    print('?')
else: print(list_of_key[answer])