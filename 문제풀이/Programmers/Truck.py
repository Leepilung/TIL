#트럭은 1초에 1만큼 움직인다.트럭의 무게는 다리에 올라왔을 경우에만 고려
#모든 트럭이 다리를 건너는데 걸리는 시간은 몇초인지 구하라.
# ex) bridge_length = 2	weight = 10 truck_weights = [7,4,5,6] return = 8
#트럭무게의 0번이 다리를 지나는데 걸리는 시간 2초. but 1초단위로 1. 진입. 2.건넘 
#두대가 들어갈 수 있어도 매초마다 한대씩 진입된다.
weight = 10
bridge_lenth = 2
truck_weights = [7,4,5,6]

def solution(bridge_length, weight, truck_weights):
    bridge=[0]*bridge_length
    time=0
    totalweight = 0
    while truck_weights:
        time+=1
        temp1 = bridge.pop(0)
        if temp1 !=0:
            totalweight -= temp1
        if truck_weights:
            if totalweight + truck_weights[0]<=weight:
                temp2 = truck_weights.pop(0)
                totalweight += temp2
                bridge.append(temp2)
            else:
                bridge.append(0)

    return time + bridge_length