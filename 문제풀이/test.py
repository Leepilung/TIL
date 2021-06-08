# 몸무게의 합이 구명보트보다 작거나 같으면 한대로 가능.
# 초과할경우 불가능. 그럴경우 구명보트 개수 추가로 필요함.
import heapq
people = [70, 50, 80, 50]
limit = 100
boat = 0

heap = []
for i in people:
    heapq.heappush(heap,i)
ri = 0
li = 1
while ri != len(people):
    if heap[ri] + heap[li] <= limit:
        li += 1
        boat +=1
    ri -=1
    
print(boat)