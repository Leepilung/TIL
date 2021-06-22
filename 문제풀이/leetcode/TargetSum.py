# LeetCode 494. Target Sum
# https://leetcode.com/problems/target-sum/
# 정수배열 nums와 정수 target이 주어짐.
# nums에 +와 -를 붙여서 target이 되는 식의 개수를 구해야함.
# target이 3이면 -1 +1 +1 +1 +1, +1 -1 +1 +1 +1이 다름.
# 복습 필요함.
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ans = 0
        self.memo = [{}.copy() for _ in range(len(nums))]
        return self.visit(0, 0, nums, target)

    def visit(self, i, curr, nums, target):
        if i == len(nums):
            if curr == target:
                return 1
            return 0
        if curr in self.memo[i]:
            return self.memo[i][curr]
        add = self.visit(i + 1, curr + nums[i], nums, target)
        sub = self.visit(i + 1, curr - nums[i], nums, target)
        self.memo[i][curr] = add + sub
        print(self.memo)
        return add + sub
        
Solution().findTargetSumWays([1,1,1,1,1],3)