# 올림 표기법

```mm
def ceil(num):
  rem = 1 if num % 1 != 0 else 0
  return int(num // 1 + rem)
```

소수점 있는지 확인하는 ceil 함수 정의한 것.

---

## 다른 올림 표기법

i = 95
j = 2
식 Cal = (100 - i / 2) = 2.5
식 Cal = (100 - i // 2) = 2
5 / 2 = 2.5
5 // 2 = 2

그러나
i = 95
j = 2
식 cal = (i-100 / 2) = -2.5
식 cal = (i-100 // 2) = -3

-5 / 2 = -2.5
-5 // 2 = -3

음수의 경우 자동으로 -5 // 2를 해도 자동으로 내림 처림 되어서 -3이 되므로

-(i - 100 // j) = 3이라는 올림과 같은 결과를 가져올 수 있다.

---

# 3진법 변환 로직 (10진법을 N진법으로 변환) 내장함수 사용X

num = 45
answer = ''

while num >= 1:
rest = num % 3
num //= 3
answer += str(rest)

print(answer)

---

# 이중 배열

grid = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]

```mm
print(len(grid)) # -> 이중 배열안에 있는 리스트의 개수 출력
>>> 4
print(len(grid[0])) # -> 이중 배열안에 있는 리스트들 중 첫번째 리스트의 원소 개수 출력
>>> 5
```

## 이중배열 [[] for i in range(n)] 형태

```mm
n = 5
m = [[] for i in range(n+1)]

print(m)
>>> [[], [], [], [], [], []]
```

---

# 코딩 표준(변수 명명법)

## PascalCasing (파스칼 케이싱)

￭ 클래스, 열거형, 이벤트, 메서드 등의 이름을 만들 때에는 대문자로 시작하는 변수명을 사용한다.
￭ 복합어일 경우 중간에 시작하는 새로운 단어는 대문자로 적는다.
예) UtilityBox, MainFrame

## CamelCasing (카멜 케이싱)

￭ 메서드의 매개변수의 이름에 적용되는데 첫번째 문자는 소문자로 시작하고 복합어 일 경우 파스칼 케이싱과 동일하게 적용한다.
￭ 동일한 이름을 가지는 두 항목을 구분하는 용도로도 사용한다.
예) utilityBox, mainFrame

---

# 숫자로된 문자열 정렬시 기준(Python sort()함수)

```md
a = ["119", "97674223", "1195524421"]
a.sort() = ['119', '1195524421', '97674223']

a = ["1234", "1235", "567",'1112414']
a.sort() = ['1112414', '1234', '1235', '567']
```

숫자로된 문자열 정렬시

문자열의 각각 index 0번부터 작은순서대로 나열됨.

예를 들어 '1234', '1235'는 각각 index 0~2까지는 같으나 index3에서 1234의 index3(=4)가 1235의 index3(=5)보다 작기때문에 앞에 정렬됨.

'1112414'도 동일. 다른 숫자로된 문자열들과 다르게 index가 0~2번까지 전부 1로 되어있기 때문에 다른 문자열보다 앞으로 정렬됨.

---

# key / value (Dictionary)

dict.get(key, default)

The method get() returns a value for the given key. If key is not available then returns default value.

get()의 역할은 key값에 주어진 value값을 불러온은 것이다. 그러나 만약 key값이 없을 경우 default로 적어둔 value를 return 해준다.

---

# sort(key = lambda x : ~~조건문)

labmda의 경우 labmda x는

def key:
retrun x와 같은 형태라고 보면 된다.

여기서 x : ~~~조건문을 사용하면 그 조건문을 기준으로 정렬을 진행한다.

예를 들어 x = [(2,1), (0,1),(3,5)] 라고 할 때

x.sort(key=lambda x : x[0])이렇게 하면

x배열의 x[0]원소를 기준으로 정렬되고

x.sort(key=lambda x : x[1])으로 한다면

x배열의 x[1]의 원소값을 기준으로 정렬된다.

가장 큰 수 알고리즘에서

x.sort(key=lambda x : x*3) 과 같이 x*정수꼴인 경우에는 해당 문자열에 \*3을 한 문자열들을 기준으로 원본값을 정렬한다고 보면 알기 쉽다.

ex) x = [221,2,10]
x.sort(key=lambda x : x\*3)

x\*3기준으로 [221221221,222,101010] 이므로

오름차순 정렬하면 101010, 221221221, 222 와 같이 되고

이건 어디까지나 기준점이기 때문에 원본으로 정렬하면

[10, 221, 2]와 같이 정렬된다.

---

# 순열 (Permutation)

. 순열(permutations)
permutations(반복 가능한 객체, n) // n=몇개를 뽑을 것인지

중복을 허용하지 않는다.
순서에 의미가 있다 (= 같은 값이 뽑히더라도 순서가 다르면 다른 경우의 수로 판단)
from itertools import permutations

1. print(list(permutations([1,2,3,4], 2)))

2. print(list(permutations([1,2,3,1], 2)))

```mm
# result1
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

# result2
# [(1, 2), (1, 3), (1, 1), (2, 1), (2, 3), (2, 1), (3, 1), (3, 2), (3, 1), (1, 1), (1, 2), (1, 3)]
```

## 중복 순열 (Product)

product(반복 가능한 객체, repeat=num)

중복을 허용하는 순열
from itertools import product

1. print(list(product([1,2,3,4], repeat=2)))

2. print(list(product([1,2,3,1], repeat=2)))

```mm
# result1
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]

# result2
# [(1, 1), (1, 2), (1, 3), (1, 1), (2, 1), (2, 2), (2, 3), (2, 1), (3, 1), (3, 2), (3, 3), (3, 1), (1, 1), (1, 2), (1, 3), (1, 1)]
```

for 문을 사용한 permutaion 구현

```md
def permute(arr):
result = [arr[:]]
c = [0] \* len(arr)
i = 0
while i < len(arr):
if c[i] < i:
if i % 2 == 0:
arr[0], arr[i] = arr[i], arr[0]
else:
arr[c[i]], arr[i] = arr[i], arr[c[i]]
result.append(arr[:])
c[i] += 1
i = 0
else:
c[i] = 0
i += 1
return result
```
