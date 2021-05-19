# 1000 이하의 소수들 나열하기

counter = 0             #나눗셈 횟수 카운트
ptr = 0                 # 찾은 소수의 갯수
prime = [None] * 500    #소수 저장하는 배열

prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2):     # 홀수만 대상으로 설정
    for i in range(1,ptr):      # 이미 찾은 소수로 나누기
        counter += 1            
        if n % prime[i] == 0:   # 나누어 떨어질 경우 소수가 아님
            break               # break문으로 반복 중단
    else:
        prime[ptr] = n          #소수로 배열에 등록
        ptr += 1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수 : {counter}')