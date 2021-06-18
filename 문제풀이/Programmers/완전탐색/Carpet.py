# Programmers 완전탐색 -> 카펫 알고리즘 문제
# https://programmers.co.kr/learn/courses/30/lessons/42842#
# 카펫에서 brown은 테두리, yellow는 내부에 있는 각각의 색을 지닌 격자의 개수
# brown 8~ 5000이하, yellow 1~2000000이하. x >= y(가로는 세로보다 같거나 길다.)
# brown 갯수 구하는 공식 구하고 yellow도 구함.
# 가로축 x 세로축 y라고 할때 x*y = brown + yellow
# brown 구하는 공식 brown = (x-2)*2+(y-2)*2+4(모서리1시,5시,7시,11시) 제외하면 중앙 제외 x축 y축남고 
# x-2 y-2는 각 축에서 모서리 부분 제외한 값. x,y축 각각 가상의 원점기준으로 대칭이므로 *2(대칭값) 둘이 항등식 세우면
# brown 식 정리하면 x+y = (brown+4)/2 나옴. x*y = brown + yellow 두 식을
# 항등식 세워서 정리하면 y^2 -(brown+4)/2*y+brown+yellow = 0 -> y^2 -ay +b의 형태. 근의공식 사용
# y값기준으로 근이 2개나옴 그런대 y1 y2가 자체만으로도 해답이 나오는데 -> 이부분 해결 필요함.
# x로 구하려고 했기때문에 y값중 작은값으로 나눠줌.

def solution(brown, yellow):
    answer = []
    y = (brown+4)/4 - (((brown+4)/2)**2 -4*(brown+yellow))**0.5 /2
    x = (brown+yellow) / y
    answer = [x,y]
    return answer
    