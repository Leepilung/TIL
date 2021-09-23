# 백준 알고리즘 - 기초수학 - 1193. 분수찾기
# https://www.acmicpc.net/problem/1193
# 링크 내의 이미지, 설명 참조. 

# 사선을 찾는 규칙성을 찾아야함. 이에 따라 계산하는 방식이 달라짐.
# 추가로 다시 무조건 풀어봐야 할 문제.

num = int(input())

line = 0
maximum = 0
while num > maximum:
    line +=1
    maximum += line

gap = maximum - num
if line % 2 == 0:
    son = line - gap
    mom = gap + 1
else:
    son = gap + 1
    mom = line - gap
print(f'{son}/{mom}')