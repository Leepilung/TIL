
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
userid = {}
announce = {'enter' : '님이 들어왔습니다.', 'leave' : '님이 나갔습니다.'}
answer = []

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

print(answer)
#print(userid)
#>{'uid1234': 'Prodo', 'uid4567': 'Ryan'} 출력
#print((userid.get'uid1234'))
#> Prodo 출력
#print(userid.get('uid4567'))
#> Ryan 출력