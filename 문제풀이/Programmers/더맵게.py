# Programmers 힙(Heap) - 더 맵게 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/42626
# scoville = [1,2,3,9,10,12] k =7 return = 2
# 모든 음식의 스코빌 지수를 k이상으로 만들어야함
# ex 1 + 2*2 = 5 -> scvoille = [5,3,9,10,12] 그러나 5와 3이 여전히 k이하이므로
# 3 + 5*2 = 13 -> scoville = [13,9,10,12]
# 초안1. 그냥 스택활용해서 풀기 -> 대부분 테스트 케이스 통과이나, 제한사항에 따라 값이 커지는 경우 런타임 에러로 통과 실패.
# 카테고리에 나와있는대로 heap 써야함. heap 개념 공부 사이트 https://www.daleseo.com/python-heapq/ 참조.
# 풀이시간 사이트 참조 공부시간 전부 포함 대략 53분.

import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)

    while heap[0] <= K:
        bucket = heapq.heappop(heap) + (heapq.heappop(heap)*2)
        heapq.heappush(heap,bucket)
        answer +=1

        if heap[0] <= K and len(heap) <= 1:
            answer = -1
            break
        if heap[0] >= K:
            break
    
    return answer