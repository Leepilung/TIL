# leetcode Generate Parentheses 알고리즘 문제
# https://leetcode.com/problems/generate-parentheses/
# n이라는 정수값이 주어지면 그 정수값으로 나올 수 있는 괄호의 모든 패턴을 출력하도록 알고리즘 구성.
# 재귀함수 사용.
# n = 3이면 Output = ["((()))","(()())","(())()","()(())","()()()"]
# n = 1이면 Output = ["()"]
# 여러번 복습 필요.
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.traverse(0, 0, '', ans, n)
        return ans
    def traverse(self, opened: int, closed: int, current: str, ans: List[str], maxCount: int):
        if opened == maxCount:
            current += ')' * (opened - closed)
            ans.append(current)
            return
        self.traverse(opened + 1, closed, current + '(', ans, maxCount)
        if opened > closed:
            self.traverse(opened, closed + 1, current + ')', ans, maxCount)


