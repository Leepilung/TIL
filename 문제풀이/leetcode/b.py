nums = [2,2,3,2]

count = {}

for i in nums:
    if i not in count:
        count[i] = 1
    elif i in count:
        count[i] += 1
    print(count)

print('count =',count)

print('-------------------------')
for i in count:
    if count.get(i) == 1:
        print(i)
