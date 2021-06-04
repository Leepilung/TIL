# Programmers 완전탐색 -> 카펫 알고리즘 문제
# https://programmers.co.kr/learn/courses/30/lessons/42842#
# yellow의 너비와 높이를 찾아서 갈색의 개수를 세는 알고리즘
# 너비 = 노랑의 크기 / 높이 (크기 = 너비x높이)
# 이 경우 카펫 자체의 크기는 yellow의 너비 +2, 높이 +2.

def solution(brown, yellow):
    for height in range(1, yellow + 1):
        if yellow % height == 0:
            width = yellow / height
            boxHeight = height + 2
            boxWidth = width + 2
            brownCount = boxHeight * 2 + width * 2
            if brownCount == brown:
                return [boxWidth, boxHeight]