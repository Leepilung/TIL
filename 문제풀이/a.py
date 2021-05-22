participant = ['jin','leo','faul','jin','dragnov']
loser = ['leo','faul','dragnov','jin']
group = {}

for member in participant:
    if member not in group:
        group[member] = 1
    else :
        group[member] = group.get(member) +1
print(group)