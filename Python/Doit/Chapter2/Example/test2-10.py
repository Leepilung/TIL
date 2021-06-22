# 1000이하의 소수 나열하기 알고리즘 개선 2
# 여기서 소수의 조건은 '정수 n은 제곱근 이하의 어떤 소수로도 나눠 떨어지지 않는다' 이다.
# 그러나 실제 식에서 써먹기엔 제곱근을 사용하기보단 제곱을 사용하는편이 더 간단하기 때문에 제곱 사용

count = 0               # 곱셈, 나눗셈등을 계산한 횟수
index = 0               # 소수의 index.(찾은 소수의 갯수를 의미하기도 함)
prime = [None] * 500

prime[index] = 2    #prime[0] = 2
index += 1          #index = 1

prime[index] = 3    #prime[1] = 3
index += 1          #index = 2

for n in range(5, 1001, 2): # 홀수만 출력
    i = 1
    while prime[i] * prime[i] <= n:
        count += 2
        if n % prime[i] == 0:   #홀수 n 이 prime[i] 즉 소수로 나눠 떨어질 경우
            break               # 반복 중단 (n보다 작은 소수로 나눠떨어지면 소수가 아니므로)
        i += 1
    else:
        prime[index] = n    # prime[index] = n값으로 배열 [None]값 갱신
        index += 1          # 다음 index 처리하기위해 +=1
        count += 1  

for i in range(index):
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 총 횟수 :{count} ')
