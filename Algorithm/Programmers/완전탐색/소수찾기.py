# Programmers 완전탐색 - 소수찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839
# 순열 사용해야 하는 문제. 경우의 수 탐색 해야함.
# 내장함수 사용하였으나 안하는 방법도 있음.(for문사용)
# numbers가 주어지면 ex = '017' -> [0,1,7]로 생각해서 이로 조합할 수있는 소수의 개수를 반환하는 문제.
# 복습필요한 문제.

from itertools import permutations
import math

def primeNumber(n):
    k = math.sqrt(n)
    if n < 2: 
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):
            if primeNumber(int(i)):
                answer.append(int(i))

    answer = len(set(answer))

    return answer

# ---------------------------------------------------------------------------
#
