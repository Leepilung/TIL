# Programmers 스택/큐 파트 기능개발 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/42586
# 기존 풀이와 다르게 복습겸 다시 풀음.
# 작업에 걸리는 일수는 필요하지 않으므로 제외.

def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0
        for i in range(len(progresses)):
            if progresses[i] != 100:
                progresses[i] += speeds[i]
                print(progresses[i])
        while len(progresses) and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        if count != 0:
            answer.append(count)


    return answer
