#배열의 원소값을 난수로 결정
#배열의 원소 수, 최댓값, 최솟값은 입력받고, 최댓값과 최솟값 안에서 배열을 구성하는 원소값은 난수로 결정하는 프로그램

import random
from max import max_of

print('난수의 최대값을 구합니다.')
num = int(input('난수의 개수를 입력하세요. : '))
low = int(input('난수의 최솟값을 입력하세요 : '))
high = int(input('난수의 최댓값을 입력하세요 : '))
x = [None] * num        #원소수가 num인 리스트 생성

for i in range(num):
    x[i] = random.randint(low,high) #low 이상 high 이하의 정수를 난수로 반환

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')

