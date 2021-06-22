# LeetCode 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/
# 정수 n 이 주어지면 

class Solution:
    def numTrees(self, n: int) -> int:
        node = 0
        
        if n == 0:
            return 1

        for i in range(1, n+1):
            node += self.numTrees(i-1)*self.numTrees(n-i)
        
        return node