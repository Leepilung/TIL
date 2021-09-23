# LeetCode Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# 들어가는거 ( )비교, 딕셔너리 활용.
# 일단 여는 괄호이면 추가. 닫는괄호가 시작이면 자동으로 false 출력
# return 구문에서 결국 판단해야되는 부분은 len(stack). 왜냐하면 True False값 출력해야되므로

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'(':')','[':']','{':'}'}
        open = dict.keys()
        for i in s:
            if i in open:
                stack.append(i)
            else:
                if len(stack) > 0 and stack[-1] == dict[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0