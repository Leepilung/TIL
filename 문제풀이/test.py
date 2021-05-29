# bin(int(n)) -> 입력값 정수형 n을 2진수로 변환하는 내장함수. 
# 안에 1이 몇개있는지 확인하는건 count
a = 2
b = []

for i in range(a+1):
    b.append(bin(i).count('1'))

print(b)