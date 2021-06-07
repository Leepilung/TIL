# 스택 사용 -> 대부분 통과하나 일부 런타임 에러 실패. + 효율성 통과 실패.
# heap 사용. heapqpop -> 작은값을 알아서 빼줌. 
# heappush -> 인수로 받은값 알아서 최소로 정렬하고 넣음.
# 

import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7
answer = 0
heap = []
for i in scoville:
    heapq.heappush(heap,i)
print('heap =',heap)

while heap[0] <= K:
    bucket = heapq.heappop(heap) + (heapq.heappop(heap)*2)
    heapq.heappush(heap,bucket)
    answer +=1
    print(bucket)
    print(heap)
    if heap[0] <= K and len(heap) <= 1:
        answer = -1
        break
    if heap[0] >= K:
        break
print(heap)
print(answer)