# Programmers 오픈채팅방 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
# ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
# 첫 단어는 Enter, Leave, Change중 하나.
# 튜플 사용해서 처음 for문으로 반복돌면서 튜플 키, 벨류값 설정해서 입력
# 그다음 for문 사용해서 키 벨류 조합해서 나타내기.
# 처음에 print문으로 사용했던건 완전 오류 answer값에 대입해야함.
# answer 리스트에 문장형태로 입력되야 하므로, ~님이 들어왔습니다, ~님이 나갔습니다 부분도 키,벨류값 설정해서 합쳐야함.



record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    answer = []
    userid = {}
    announce = {'enter' : '님이 들어왔습니다.', 'leave' : '님이 나갔습니다.'}
    for i in range(len(record)):
        recordlist = record[i].split()
        if recordlist[0] == 'Enter':
            userid[recordlist[1]] = recordlist[2]
        if recordlist[0] == 'Change':
            userid[recordlist[1]] = recordlist[2]

    for text in range(len(record)):
        recordlist = record[text].split()
        if recordlist[0] == 'Enter':
            answer.append(userid.get(recordlist[1])+announce.get('enter'))
        if recordlist[0] == 'Leave':
            answer.append(userid.get(recordlist[1])+announce.get('leave'))


    return answer