#기능개발 알고리즘 다른 풀이 by.범준

def work(progresses, speeds):
    remain = 100 - progresses[0]
    speed = speeds[0]
    left = 1 if remain % speed != 0 else 0
    days = remain // speed  + left
    for index, task in enumerate(progresses):
        progresses[index] = task + speeds[index] * days
def solution(progresses, speeds):
    answer = []
    while len(progresses):
        work(progresses, speeds)
        count = 0
        while len(progresses) and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        answer.append(count)
    return answer