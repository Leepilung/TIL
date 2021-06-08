# Programmers 탐욕법(Greedy) - 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885
# 몸무게의 합이 구명보트보다 작거나 같으면 한대로 가능.
# 초과할경우 불가능. 그럴경우 구명보트 개수 추가로 필요함.

def solution(people, limit):
    boat = 0
    heap = []
    people.sort()
    
    li = 0
    ri = len(people) -1
    
    while li <= ri:
        boat += 1
        if people[li] + people[ri] <= limit:
            li += 1
        ri -=1

    return boat