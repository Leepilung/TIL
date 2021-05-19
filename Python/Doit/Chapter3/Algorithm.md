# 검색 알고리즘

## 검색과 키

주소록을 검색한다고 가정해보자.

- 국적이 한국인 사람을 찾습니다.
- 나이가 21세 이상 27세 미만인 사람을 찾습니다.
- 이름에 '민'자가 들어간 사람을 찾습니다.

검색 조건들은 모두 어떠한 항목에 주목한다. 이렇게 주목하는 항목을 `키(key)`라고 한다.

국적으로 검색하는 경우 국적이 키. 나이로 검색하는 경우 나이가 키인 것이다.
대부분 `키`는 데이터의 일부이다. 데이터가 간단한 정숫값이나 문자열이면 데이터값이 그대로 키값이 될 수도 있다.

다시 말해 위의 주소록 검색 조건을 수행하려면 다음과 같이 키를 지정해야 한다.

- **국적** : 키값과 일치하도록 지정한다.
- **나이** : 키값의 구간을 지정한다.
- **문자** : 키값에 가깝도록 지정한다.

검색에서는 이러한 조건을 하나만 지정할 수도 있고 논리곱, 논리합 등을 사용해서 복합해서 지정할 수 있다.

---

# 선형 검색

`선형 검색(Linear search)`란 직선 모양(선형)으로 늘어선 배열에서 검색하는 경우 원하는 키값을 가진 원소를 찾을 때까지 맨 앞부터 스캔하여 순서대로 검색하는 알고리즘이다.

> 선형 검색의 종료 조건

1. 검색할 값을 찾지 못하고 배열의 맨 끝을 지나간 경우 -> 검색 실패
2. 검색할 값과 같은 원소를 찾는 경우 -> 검색 성공

배열의 원소 개수가 n이라면 이 조건을 판단하는 횟수는 평균 n / 2 번입니다.

배열 a에서 검색하는 프로그램은 다음과 같이 나타낼 수 있다.

```m
i = 0
while True:
    if i == len(a):
        # 검색 실패
    if a[i] == key:
        # 검색 성공(찾은 원소의 인덱스는 i)

        i +=1
```

배열을 스캔할 때 주목하는 원소의 인덱스를 카운터용 변수 i로 나타냈다. i를 0으로 초기화하고 원소를 하나씩 검사할 때마다 while 문의 끝에서 1씩 증가한다.

while문을 빠져나가는 것은 앞에서 설명한 선형 검색의 종료 조건1 , 2가운데 어느 하나가 성립되는 경우이며 각 if문과 대응한다.

- 선형 검색의 종료 조건 1. if i == len(a)이 성립하면 스캔 종료.
- 선형 검색의 종료 조건 2. if a[i] == key 가 성립하면 스캔 종료.

> While문으로 작성한 선형 검색 알고리즘

```m
from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 같이 같은 원소를 선형 검색(while문)"""
    i = 0

    while True:
        if i == len(a):
            return -1       # 검색 실패하여 -1 반환
        if a[i] == key:
            return i        # 검색에 성공하여 현재 검사한 배열의 인덱스 반환
        i += 1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요. : ')) # num값 입력받음
    x = [None] * num        # 원소 수가 num인 배열 생성

    for i in range(num):
        x[i] =int(input(f'x[{i}]: '))

    ky = int(input('검색할 값을 입력하세요.: ')) #검색할 키 ky를 입력받음

    idx = seq_search(x ,ky)        # ky와 같이 같은 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
```

`seq_search()`는 배열 a에서 값이 key인 원소를 선형 검색하는 함수이며, 찾은 원소의 인덱스를 반환한다. 값이 key인 원소가 여러개 존재 하는 경우에는 스캔 과정에서 맨처음 발견한 원소(배열에서 맨 앞의 원소)를 반환한다.

그러나 배열의 스캔을 for문으로 구현하면 코드가 더 짧고 간결해진다.
앞에서 작성한 while문을 for문으로 수정해보자

> for문으로 작성한 선형 검색 알고리즘

```mm

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """ 시퀀스 a에서 key와 같이 같은 원소를 선형 검색(for 문)"""
    for i in range(len(a)):
        if a[i] == key:
            return i        #검색 성공(인덱스를 반환)
    return -1               #검색 실패(-1을 반환)
```

> test.py파일의 seq_search()함수 사용하여 실수 검색하기

```mm
#seq_search() 함수를 사용하여 실수 검색하기
from test import seq_search

print('실수를 검색합니다')
print('주의 : "End"를 입력하면 종료합니다.')

number = 0
x = []

while True:
    s = input(f'x[{number}]')
    if s == 'End':
        break
    x.append(float(s))
    number += 1

ky = float(input('검색할 값을 입력하세요. : '))

idx = seq_search(x, ky)

if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else :
    print(f'검색값은 x[{idx}]에 있습니다.')

```

위에서 작업한 teset.py파일내의 함수를 import하여 사용한 프로그램이다.

## 보초법

선형검색은 반복할 때마다 2가지 종료 조건을 체크한다. 단순한 판단이지만 이 과정을 반복하면 종료 조건을 검사하는 비용을 무시할 수 없게된다. 이 비용을 반으로 줄이는 방법이 바로 `보초법(Sentinal method)`이다.

```mm
#선형 검색 알고리즘(실습3-1)을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
   """시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""

   a = copy.deepcopy(seq)  #seq를 deepcopy 한다.
   a.append(key)           #보초 key를 추가하는 명령어

   i = 0
   while True:
       if a[i] == key:
           break
       i += 1
   return -1 if i == len(seq) else i

if __name__ : '__main__':
   num = int(input('원소 수를 입력하시오. : ')     #num값을 입력
   x = [None] * num                             # 원소 수가 num인 배열 생성

   for i in range(num):
       x[i] = int(input(f'x[{i}]'))

   ky = int(input('검색할 값을 입력하세요.: '))    # 검색할 ky를 입력받는 함수

   idx = seq_search(x, ky)                      # 키 ky값과 같은 원소를 x에서 검색

   if idx == -1:
       print('검색값을 갖는 원소가 존재하지 않습니다.')

   else:
       print(f'검색값은 x[{idx}에 있습니다.')

```

보초법을 사용한 선형 검색 알고리즘이다.

배열 seq를 a로 복사하고 a의 마지막에 보초 key를 추가한다.
