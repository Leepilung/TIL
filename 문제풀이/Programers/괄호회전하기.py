# Programmers 괄호 회전하기 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/76502#
# 스택 활용해서 풀었음. 배열 s = "[](){}" 가 주어지면 이 배열을 왼쪽으로 회전시키면서 올바른 문자열만 출력 될때 그 결과값 가산.
# 배열을 문자열 길이만큼 왼쪽으로 회전시킴. 주어진 문자열 s를 회전 -> 내부문법 통해 array_s 만듦
# 회전 배열을 리스트로 만들고 거기서 시작값이 열리는 괄호가 아니면 완전한 문자열이 될 수 없으므로 나머지 경우의 수는 전부 예외처리
# if 문법 사용시 or and 조건 확실하게.
def solution(s):
    stack = []
    answer = 0
    for i in range(len(s)):
        array_s = list(s[i:]+s[:i])

        while array_s:
            if array_s[0] == '(' or array_s[0] ==  '[' or array_s[0] ==  '{':
                stack.append(array_s[0])
                array_s.pop(0)
            else:
                if len(stack) == 0:
                    break
                else:
                    stack.append(array_s[0])
                    array_s.pop(0)
                    if stack[-2] + stack[-1] == '[]' or stack[-2] + stack[-1] == '()' or stack[-2] + stack[-1] == '{}':
                        stack.pop(-1)
                        stack.pop(-1)
                        continue

        if len(array_s) == 0 and len(stack) == 0:
            answer +=1
    return answer