# Programmers 오픈채팅방 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
# 다른 풀이법 by.범준

msg = {
    "Enter": '님이 들어왔습니다.',
    "Leave": '님이 나갔습니다.'
}
def printLog(logs, user):
    arr = []                        # arr라는 빈배열 생성
    for log in logs:                # log라는 변수는 logs의 값을 나열
        (id, action) = log          # (id, action) = log
        arr.append(user[id] + msg[action])  
    return arr
def solution(records):
    log = []
    user = {}
    for record in records:
        values = record.split(' ')  # values는 record 입력값을 리스트로 쪼갠거
        action = values[0]          # Enter, Leave, Change 해당
        id = values[1]              # id = values에서 userid에 해당하는 부분 별도 변수 설정
        if action == "Enter":       
            user[id] = values[-1]   # enter일때 user 딕셔너리[id]에 values[-1]값(닉네임 부분) 넣음
            log.append((id, action))# log에 append 시킨다. id, action값을.
        elif action == "Leave":
            log.append((id, action))
        elif action == "Change":
            user[id] = values[-1]
    return printLog(log, user)

## 다른 풀이법
# 심플한 풀이법

def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer