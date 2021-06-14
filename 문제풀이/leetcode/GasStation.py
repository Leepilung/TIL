# LeetCode 134. Gas station
# https://leetcode.com/problems/gas-station/
# 순회 가능한 경우에 어디서 시작해야 일주가 되는지 해당 인덱스값을 찾는 문제.
# 온갖 시행착오 b.py에 다적어놨는데 지웠다 썼다하면서 거진 다 날라감.
# 처음에 단순조건 gas[i] > cost[i+1] 으로 시작. -> 조건 부합안됨. 실패
# Description 에 있는 조건 나열해서 조건 파악해보기 -> gas[i] - cost[i]로 시작됨.
# 시작 인덱스값 구해야므로 starti = 0으로 두고 totalcost는 그냥 가스 - 코스트 변수로 놓고 시작. gas[i] - cost[i] 음수가 되는순간 시작 인덱스가 아니게됨.
# i가 그대로 진행되면 그게 시작인덱스가되고 totalcost가 음수가 나오는 시점이 생기면 i+1시키고 total코스트 초기화시킴.
# 1차시도에서 wrong answer 나온값까지 테스트케이스 추가 -> 통과

from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        starti = 0
        totalcost = 0
        for i in range(len(gas)):
            totalcost += gas[i] - cost[i]
            if totalcost < 0:
                starti = i + 1
                totalcost = 0
        return starti