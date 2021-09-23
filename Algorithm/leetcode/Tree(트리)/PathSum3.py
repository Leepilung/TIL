# LeetCode 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/
# root 배열이 주어지고 targetsum이 주어지는데 root에서 경로를 따른 노드들의 합계가 targetsum과 같아지는 경로의 수를 구해야함.
# 경로는 리프나 루트에서 시작해도 무관하나 무조건 상위노드에서 하위노드로만 이동해야됨.(위에서 아래로)
# 복습하기.
# Definition for a binary tree node.
# 
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.cache = defaultdict(int)
        return self.dfs(root, 0, targetSum)
        
    def dfs(self, node, prev, target):
        if not node:
            return 0
        res = 0
        acc = prev + node.val
        if acc - target in self.cache:
            res += self.cache[acc - target]
        self.cache[acc] += 1
        res += self.dfs(node.left, acc, target)
        res += self.dfs(node.right, acc, target)
        self.cache[acc] -= 1
        return res