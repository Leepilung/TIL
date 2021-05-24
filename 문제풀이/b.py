p = [93, 30 , 55]
s = [1, 30, 5]
answer = []
timegab = []
count = 1
import math
for i,j in zip(p,s):    
    timegab.append(math.ceil((100 - i) / j))
    if timegab[0] > timegab[1]:
        timegab.pop(1)
        count +=1
    elif timegab[0] < timegab[1]:
        timegab.pop(0)
        answer.append(count)
    else:
        timegab.pop(0)
        timegab.pop(1)
        count+=2

print(timegab) -> [7,3,9]
print(timegab[0]) -> 7
print(timegab[1]) -> 3
timegab.pop(0) -> 7 pop으로 삭제
print(timegab) -> [3,9]
# 7, 3, 9 출력 -> return [2,1]
# 7 계산,출력하고 count에 1가산, 3계산하고 count에 또 1가산. 여기서 조건문 들어가야함
# answer[0] > answer[1] 일때만 반복. 만약 answer[0] < answer[1]이면 별도로
#배포가 진행된다. answer[0]
print('----------------')

p2 = [95, 90, 99, 99, 80, 99]
s2 = [1, 1, 1, 1, 1, 1]
for i,j in zip(p2,s2):    
    done2 = math.ceil((100 - i) / j)
    print(done2)
    
# 5, 10, 1, 1, 20, 1 출력 -> return[1,3,2]

# 1, 1, 3 , 1, 2, 10, 5 -> return[2,3,2]