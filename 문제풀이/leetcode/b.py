gas = [5,1,2,3,4]
cost =[4,4,1,5,1]
# totalcost += gas[i] - cost[i] >0 -> 이걸 i까지 반복?
# 우선 sum(gas) == sum(cost) -> 이조건 아녔음. 가스가 더많으면 노 상관.
# i에서 시작. 일주가 가능하다면 시작위치를 반환함. 총합은 15로 같으나. index 3에서 시작한다고 가정할 경우
# 4충전 -> 1소모 + 5충전 = 8 -> 2소모 + 1충전 = 7 -> 3소모 2충전 = 6 -> 4소모 3충전 = 5 -> 5소모 일주 성공.
# [5,1,2,3,4] // [4,4,1,5,1]
# gas[3] - cost[3] + gas[4] - cost[4] + gas[0] - cost[0] + gas[1] - cost[1] + gas[2] - cost[2] 
# 4      - 1        +  5    - 2       + 1      - 3       + 2      - 4       + 3      - 5
#[5,1,2,3,4] // [4,4,1,5,1]
# gas[4] - cost[4] + gas[0] - cost[0] + gas[1] - cost[1] + gas[2] - cost[2]   gas[3] - cost[3] 
#     4  -  1      
if sum(gas) < sum(cost):
    print(-1)

starti = 0
totalcost = 0
for i in range(len(gas)):
    totalcost += gas[i] - cost[i]
    if totalcost < 0:
        starti = i + 1
        totalcost = 0
print(starti)