# LeetCode Combination Sum 알고리즘 문제
# https://leetcode.com/problems/combination-sum/
# 개별 정수로된 배열 candidates가 주어지면 이를 조합한 합이 target에 있는 숫자의 값이 되도록 해야함.
# test case 1
# Input: candidates = [2,3,6,7], target = 7
# Output : [[2,2,3].[7]]

# test case 2
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# 기존 재귀 문제랑 접근 비슷하게. 배열 사용. 수식 자세한건 공책위주로 계산하기.
# 종료 조건 세워야함. sum[current] == target. 만약 current의 합이 target보다 크거나 작으면 무효. 
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        self.Countfuntion(candidates, [], answer, target)
        return answer

    def Countfuntion(self, candidates, current, answer, target):
        if target < 0:
            return
        if target == 0:
            answer.append(current)
            return
        for i in range(len(candidates)): # 0~3까지
            self.Countfuntion(candidates[i:], current + [candidates[i]], answer, target - candidates[i])        
