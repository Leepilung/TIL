record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

for i in range(len(record)):
    a = record[i].split()
    if a[0] == 'Enter':
        print(f"{a[2]}님 이 들어왔습니다.")
    if a[0] == 'Leave':
        print(f"{a[1]}님이 나갔습니다.")
    print(a)
    