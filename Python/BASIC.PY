bucket = [4,3,1,1,3,2,4]
b = bucket
answer = 0


n = 0 

if bucket[n] == bucket[n+1]:
    answer += 2
    bucket.pop(n)
    bucket.pop(n)
else:
    n += 1

bucket = [4,3,3,2,4]