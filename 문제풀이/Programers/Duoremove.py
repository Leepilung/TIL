#프로그래머스 2017 팁스다운 짝지어 제거하기
#문자열 2개가 이어지는 경우 제거하고 
# s = baabaa result = 1
# s = cdcd   result = 0
# for i in s -> b a a b a a
# stack = 0이면 b입력. -> stack [b] 그다음 i 는 a
# stack[-1] = b == a가 아니므로 stack.append(i) 
# 그다음 i도 a stack[-1] = a == i(=a). stack.pop() 하면 stack = [b]
# 그 다음 b  동일하므로 스택 지워짐.
# 처음 제출시 테스크 케이스 2번 통과안했음. 두번째 조건문이 if였음. if -> elif로 변경
# 효율성, 점수 테스트 전부 올체크.

def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    if len(stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer