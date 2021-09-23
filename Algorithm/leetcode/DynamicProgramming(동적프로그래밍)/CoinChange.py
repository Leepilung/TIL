# LeetCode 322. Coin Change
# https://leetcode.com/problems/coin-change/
# 종류를 나타내는 동전 배열과 총금액 amount가 주어진다.
# amount를 동전배열로 조합해서 이때 필요한 동전의 가작 적은 수의 값을 반환. 불가능할 경우 -1 반환
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            dp = [0] + [float('inf') for i in range(amount)]
            for i in range(1, amount+1):
                for coin in coins:
                    if i - coin >= 0:
                        dp[i] = min(dp[i], dp[i-coin] + 1)
            if dp[-1] == float('inf'):
                return -1
            return dp[-1]
        