# Programmers 완전탐색 - 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840
# a,b,c의 범위를 answer와 비교해봤으나 테스트케이스 전부 통과 못함.
# 제한사항까지 출력하게 하고 비교하게 했더니 통과함.
# 완전탐색이나 응답속도는 빠르게 짜봤음
# 개선 여지  있음.

def solution(answers):
    a = [1,2,3,4,5] * 2000 
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    count1 = 0
    count2 = 0
    count3 = 0
    stack = []
    answer = []
    for i in range(len(answers)):
        if a[i] == answers[i]:
            count1 += 1
        if b[i] == answers[i]:
            count2 += 1
        if c[i] == answers[i]:
            count3 += 1
        else:
            continue
    stack.append(count1)
    stack.append(count2)
    stack.append(count3)
    max_of_stack = max(stack)
    for i in range(len(stack)):
        if stack[i] == max_of_stack:
            answer.append(i+1)
    
    return answer

#----------------------------------------------
# 짜고보니 불필요한 부분 있어서 생략하고 고친 부분.

def solution2(answers):
    a = [1,2,3,4,5] * 2000 
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    stack = [0,0,0]
    answer = []
    for i in range(len(answers)):
        if a[i] == answers[i]:
            stack[0] += 1
        if b[i] == answers[i]:
            stack[1] += 1
        if c[i] == answers[i]:
            stack[2] += 1
        else:
            continue

    max_of_stack = max(stack)
    for i in range(len(stack)):
        if stack[i] == max_of_stack:
            answer.append(i+1)
    
    return answer