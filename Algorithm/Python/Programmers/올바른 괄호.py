# Programmers 올바른 괄호 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/12909
# 문자열 s의 길이는 100,000이하 이며 s는 오로지 '('와 ')'로 이루어져 있다.
# 올바른 괄호이면 True, 아니면 False를 출력하도록 짜시오.
# 스택으로 짜도 되나 복잡도를 줄여보고자 스택 원리 활용해서 변수 활용함.
# ')'로 시작하는 경우는 전부다 False 출력 -> Count 가 음수일때가 전부 해당됨.
def solution(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
