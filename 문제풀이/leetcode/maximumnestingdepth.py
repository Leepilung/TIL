#괄호안에 문자열의 깊이 구하기
#(1) = 1 ((1)) = 2 (((3))) = 3 과 같은 형태
#stack 사용해서 풀기. 
#스택 지정하고 최대 깊이는 숫자형태로 나와야함. int설정.

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []          #빈 스택 설정
        depth = int()       #숫자형태로 나와야함
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop()
            if len(stack) > depth:
                depth = len(stack)
        
        return depth