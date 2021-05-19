# 1000이하의 소수 나열하기

counter = 0
#나눗셈 연산의 횟수 카운트

for n in range(1,501):
    for i in range (2,n):
        counter += 1
        if n % i == 0: 
            break 
    else:
        print(n)    
print(f'나눗셈을 실행한 횟수: {counter}')