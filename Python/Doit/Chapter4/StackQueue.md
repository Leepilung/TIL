# 스택

`스택(stack)`이란 데이터를 임시 저장할 떄 사용하는 자료구조로써 데이터의 입력과 출력 순서가 `후입선출`이라는 방식을 갖는다.

스택에 데이터를 넣는 것을 `푸시(push)`라고 하고 꺼내는 작업을 `팝(pop)`이라고 한다.

## 스택의 구현

- 스택 배열 : stk

푸시한 데이터를 저장하는 스택 본체인 list 배열이다.

    ```
    index   stk           --
    0       19  --        ㅣ
    1       22  ㅣ ptr    ㅣ
    2       37  ㅣ        ㅣ
    3       53  --        ㅣ  capacity

ptr 4 ㅣ
5 ㅣ
6 ㅣ
7 --

````

이미지파일을 찾을수 없어 대체하여 그린것이다.. 엉성하지만 나중에 복습할때 알아보기 힘들다면
책 p.155를 참조하자..

인덱스가 0인 원소를 스택의 바닥이라고 한다. 따라서 가장 먼저 푸시하여 데이터를 저장하는 곳은 stk[0]이다.

- 스택 크기 : capacity
  스택의 최대 크기를 나타내는 int형 정수(스택을 최대 몇개까지 쌓을 수 있는가?를 나타내는 지표)
  이 값은 배열 stk의 원소 수 len(stk)와 일치한다.

- 스택 포인터 : ptr

스택에 쌓여있는 데이터의 개수를 나타내는 정수값을 `스택 포인터(stack pointer)`라고 한다. 스택이 비어있으면 ptr의 값은 0이 되고 가득 차 있으면 capacity와 동일한 값이 된다. 위의 엉성한 예시에서 ptr[0]은 19가 된다. 가장 마지막에 푸시한 데이터는 stk[ptr01]인 53이다.

- ptr은 한마디로 가장 마지막에 푸시한 원소의 인덱스에 1을 더한 값과 일치한다.
  스택에 데이터를 푸시할 때 ptr을 1증가시키고, 스택에서 데이터를 pop할때 1감소시키면 된다.

---

> 고정 길이 클래스 FixedStack

고정 길이 스택을 구현하는 FixedStack 클래스 예제를 통해 스택이 동작하는 원리와 스택을 동작시키는 함수에 대해 알아보자.

```mm
#고정 길이 스택 클래스 Fixed stack.

from typing import Any

class FixedStack:
    '고정 길이 스택 클래스문'

    class Empty(Exception):
        '비어있는 FixedStack에 푸시할때 보내는 예외 처리 클래스문'
        pass
````

- 예외 처리 클래스 `Empty`

pop()함수나 ppek()함수를 호출시 스택이 비어있으면 보내는 예외 처리 클래스이다.

```mm
    class Full(Exception):
        '가득찬 FixedStack에 푸시할때 보내는 예외 처리 클래스문'
        pass
```

- 예외 처리 클래스 `Full`

push()함수를 호출할 때 스택이 가득차 있으면 내보내는 예외 처리 클래스이다.

```mm
    def __init__(self, capacity: int = 256) -> None:
        '스택 초기화 하는 함수'
        self.stk = [None]*capacity  # 스택의 본체 크기. 내용물이 None인 배열을 capacity만큼 생성
        self.capacity = capacity    # 스택의 크기를 나타냄
        self.ptr = 0                # 스택 포인터 (시작부분이기 때문에 0으로 초기화)
```

- 초기화 하는` __init__()`함수

`__init__()` 함수는 스택 배열을 생성하는 등의 준비 작업을 수행하는 함수이다. 매개변수 capacity로 전달받은 값을 스택의 크기로 나타내는 필드인 self.capacity로 복사하고 원소수가 capcity이고 모든 원소가 None인 리스트형 stk을 생성한다. 그리고 당연히 초기 상태이므로 스택이 비어있기 때문에 ptr의 값을 0으로 한다.

```mm
    def __len__(self) -> int:
        ' 스택에 쌓여있는 데이터 갯수를 반환하는 함수'
        return sefl.ptr
```

- 데이터 개수를 찾아내는 len 함수

`__len__` 함수는 스택에 쌓여있는 데이터 개수를 반환한다. 스택 포인터 ptr의 값을 반환한다.

```mm
    def is_empty(self) -> bool:
        '스택이 비어있는지를 판단하는 함수'
        return self.ptr <= 0        # 포인터(ptr)이 0보다 작거나 같으면 무조건 0이므로 스택이 비어있음을 나타냄.
                                    # 스택이 비어있으면 True, 아니면 False 출력
    def is_full(self) -> bool:
        '스택이 가득차있는 지를 판단하는 함수'
        return self.ptr >= self.capacity    #스택이 가득차있으면 True, 아니면 False 출력
                                            #ptr이 capacity보다 크거나 같으면 가득차있다는 의미.
```

- 스택이 비어있는지`is_empty()`함수, 가득차있는지를 나타내는 `is_full()`함수

ptr을 기준으로 해당 스택이 비었는지 가득찼는지를 판단한다.
`is_empty`함수의 경우 스택이 비었으면 True, 아닐경우 False를 반환

`is_full`함수의 경우 스택이 가득 찼으면 True, 안리경우 False를 반환한다.

```mm
#4-1a에 이어지는 내용

    def push(self, value: Any) -> None:
        '스택에 value를 푸시(데이터를 넣음)'
        if self.is_full():                  #스택이 가득찬 경우 (is_full에 해당하는 경우)
            raise FixedStack.Full           #full 클래스 raise시킨다.
        self.stk[self.ptr] = value          # self.ptr의 초기값은 0
        self.ptr += 1                       # self.ptr에 가산. 다음 인덱스로 넘어가야 하기 때문
```

- 데이터를 푸시하는 `push()`함수

push()함수는 스택에 데이터를 추가하는 함수이다. 그러나 스택이 가득찬 경우 더이상 푸시할 수 없기 때문에 FixedStack.Full을 통하여 예외처리를 보낸다.

허나 스택이 가득차있지 않는 경우에는

stk = [19,22,37,53] prt = 4 인경우 s.push(24)로 푸쉬하는 경우

stk = [19,22,37,53,24] ptr =5 의 형태로 24가 맨마지막에, ptr의 값이 1 증가한다.

```mm
    def pop(self) -> Any:
        '스택에서 데이터를 팝(꼭대기 데이터를 꺼내는 함수)'
        if self.is_empty():                 #스택이 비어있는 경우(is_empty에 해당하는 경우)
            raise FixedStack.Empty          #empty 클래스 raise시킨다.
        self.ptr -= 1                       #스택이 비어있지 않은경우 ptr의 값 -1시키고
        return self.stk[self.ptr]           #stk[ptr]에 저장된 값 반환
```

- 데이터를 팝하는 `pop()`함수

pop()함수는 스택의 꼭대기(맨마지막)에서 데이터를 꺼내어 그 값을 반환한다. 스택이 비어서 팝할 수 없는 경우에는 FixedStack.Empty를 통하여 예외처리를 보낸다.

허나 스택이 비어있지 않은 경우에는

stk = [19,22,37,53,24] ptr =5 에서 stk.pop() 하는 경우

stk = [19,22,37,53] ptr = 4로 맨마지막 원소 24가 뽑혀나가고 ptr의 값을 1감소시킨다.

```mm
    def peek(self) -> Any:
        '스택에서 데이터를 피크(꼭대기 뎅디터를 들여다 봄)'
        if self.is_empty():                 # 스택이 비어있는 경우 볼 원소가 없으므로
            raise FixedStack.Empty          #empty 클래스를 raise 시킨다.
        self.ptr -= 1                       #스택이 비어있지 않은경우 ptr의 값 -1시키고
        return self.stk[self.ptr-1]         #꼭대기 원소의 인덱스값보다 ptr의 값이 1만큼 더 크기때문에 -1해줘야함
```

- 데이터를 들여다보는 `peek()`함수

peek() 함수는 스택의 꼭데기 데이터(팝의 대상이 되는 데이터)를 들여다 본다. 그러나 스택이 비어있는 경우 FixedStack.Empty를 통해 예외처리를 보낸다.

허나 스택이 비어있지 않은 경우에는 꼭대기 원소 stk[ptr-1]의 값을 반환한다. 데이터의 입출력이 있는 것은 아니라서 ptr의 값은 변하지 않는다.

```mm
    def clear(self) -> None:
        '스택의 모든 데이터를 삭제'
        self.ptr = 0                        # 스택포인터의 값 ptr = 0으로 하면 끝난다.
```

- 데이터를 전부 삭제하는 `clear()`함수

clear()함수는 스택에 쌓여있는 데이터를 모두 삭제하여 빈 스택을 만든다. 이것은 스택 포인터 ptr의 값을 0으로 하면 끝난다.

```mm
def find(self, value:Any) -> Any:
    '스택에서 value를 찾아 인덱스를 반환(없으면 -1을 반환한다)'
    for i in range(self.ptr -1, -1, -1):    #ex) self.ptr = 7이면 (6,-1,-1) 6부터 -1까지 -1의 간격으로 검색
        if self.stk[i] == value:            # 6 5 4 3 2 1 0 이런순으로 검색함.
            return i                        #검색 성공시 i값 출력
        return -1                           #검색 실패시 -1출력
```

- 데이터를 검색하는 `find()`함수

`find()`함수는 스택 본체의 배열 stk안에 value와 같은 값이 포함되어 있는지 확인하고, 포함되어 있다면 배열의 어디에 들어있는지를 검색한다.

예를 들어 stk = [19,25,37,53,25,17]이라면 stk.find(25)를 검색할 경우 꼭대기에 가까운 25의 인덱스 4를 반환한다. 꼭대기 쪽부터 스캔하여 4를 반환하는 이유는 find가 pop할 데이터를 찾아가기 위해서 이다.

```mm
def count(self, value: Any) -> bool:
    '스택에 있는 value의 개수를 반환'
    c = 0
    for i in range(self.ptr):       #예를 들어 스택 = [19,25,37,53,25,17] 이라면
        if self.stk[i] == value:    #25라는 value를 검색할 시 self.stk[i] == value 일때마다
            c += 1                  #c 에 1씩 가산되므로 c 의 값은 2가 나온다.
        return c
```

- 데이터 개수를 세는 `count()` 함수.

`count()`함수는 스택에 쌓여 있는 데이터(vlaue)의 개수를 구하여 반환한다. #예를 들어 스택 = [19,25,37,53,25,17] 이라면 25라는 value를 검색할 시 self.stk[i] == value 의 조건을 성립할 때마다 c 에 1씩 가산되므로 c 의 값은 2가 나온다.

```mm
def __contains__(self, value:Any) -> bool:
    '스택에 value값이 포함되있는지 판단'
    return self.count(value)        # count 함수를 불러와서 값이 있는경우 True, 아니면 False를 출력
```

- 데이터가 포함되어 있는지를 판단하는 `__contains__()`함수

`__contains()`함수는 스택에 데이터(value)가 있는지를 판단한다. count 함수를 사용하여 데이터가 있으면 True, 아니면 False를 반환한다.

예를 들어 스택 s에 x라는 데이터가 포함되어 있는지를 판단하려면 `s.__contains__(x)`를 사용하거나` x in s`를 사용하면 된다.

```mm
def dump(self) -> None:
    '덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)'
    if self.is_empty():             #스택이 빈경우
        print('스택이 비어있습니다.')
    else:
        print(self.stk[:self.ptr])      #self.ptr까지 출력.
```

- 스택의 모든 데이터를 출력하는 `dump()`함수

dump()함수는 스택에 쌓여있는 ptr개의 모든 데이터를 바닥부터 꼭대기까지 순서대로 출력한다.

만약 스택이 비어있으면 '스택이 비어있습니다'를 출력한다.

---

## `__len__()`함수와 `__contains__()` 함수 알아보기.

파이썬에서 시작과 끝에 언더스코어(\_)가 2개 붙은 함수는 특별한 의미가 있다.

`__len__()` 함수의 경우 클래스에 `__len__()`함수를 정의하면 클래스형의 인스턴스를 `__len__()`함수에 전달 할 수 있다. 예를 들어 클래스형의 인스턴스 obj에 대한 `__len__()`함수를 호출하는 `obj.__len__()`을 간단히 len(obj) 형태로 작성할 수 있다.

그리고 `__contains__()` 함수의 경우 클래스에 `__contains__()`함수를 정의하면 클래스형의 인스턴스에 멤버십 판단 연사자인 int를 적용할 수 있다. 예를 들어 클래스형의 인스턴스 obj에 대한 `__contains__()`를 호출하는 `obj.__contains__(x)`를 간단히 x in obj로 작성할 수 있게 된다.

이렇게 밑줄 2개(\_\_)인 더블 언더스코어를 줄여서 던더(dunder)라고 부른다. 즉 더블 언더스코어 함수들을 던더 함수라고도 한다.

---

# Deque

파이썬의 내장 컨테이너는 딕셔너리, 튜플, 리스트, 집합(set)등이 있다. 이외에도 여러 컨테이너를 `collections` 모듈로 제공한다.

주요 컨테이너는 namedtuple(),`deque`,ChainMap,Counter,OrderedDict, defauldict,Userdict,Userlist,UserString 같은 컬렉션 등이 있다.

이 가운데 `deque` 모듈을 사용하면 스택을 간단하게 구현할 수 있다.

`deque`는 맨 앞과 맨 끝 양쪽에서 원소를 추가, 삭제하는 자료구조인 `deque`를 구현하는 컨테이너이다.

deque의 주요 속성과 함수는 다음 표와 같다.

|         속성과 함수         |                                                                            설명                                                                             |
| :-------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------: |
|         maxlen속성          |                                      deque의 최대 크기를 나타내는 속성으로 읽기 전용이다. 크기 제한이 없으면 None이다.                                      |
|       append(x) 함수        |                                                            deque의 맨 끝(오른쪽)에 x를 추가한다.                                                            |
|     appendleft(x) 함수      |                                                             deque의 맨 앞(왼쪽)에 x를 추가한다                                                              |
|         clear()함수         |                                                       deque의 모든 원소를 삭제하고 크기를 0으로 한다                                                        |
|         copy()함수          |                                                                  deque의 얕은 복사를 한다                                                                   |
|        count(x)함수         |                                                       deque안에 있는 x와 같은 원소의 개수를 계산한다                                                        |
|    extend(literable)함수    |                                    순차 반복 인수 literable에서 가져온 원소를 deque의 맨 끝(오른쪽)에 추가하여 확장한다                                     |
|  extendleft(literable)함수  |                                     순차 반복 인수 literable에서 가져온 원소를 deque의 맨 앞(왼쪽)에 추가하여 확장한다                                      |
| index(x[,start[,stop]])함수 | deque안에 있는(인덱스 start부터 인덱스 stop까지 양 끝을 포함한 범위) x가운데 가장 앞쪽에 있는 원소의 위치를 반환한다. x 가 없는 경우 value Error를 출력한다 |
|       insert(i,x)함수       |                       x를 deque의 i위치에 삽입한다. 이때 크기에 제한이 있는 deque일 경우 maxlen을 초과한 삽입은 IndexError를 출력한다                       |
|          pop()함수          |                   deque의 맨 끝(오른쪽)에 있는 원소 1개를 삭제하고 그 원소를 반환한다. 원소가 하나도 없는 경우에는 IndexError를 출력한다.                   |
|        popleft()함수        |                    deque의 맨 앞(왼쪽)에 있는 원소 1개를 삭제하고 그 원소를 반환한다. 원소가 하나도 없는 경우에는 IndexError를 출력한다.                    |
|      remove(value)함수      |                                         value의 첫 번째 항목을 삭제한다. 원소가 없는 경우에는 ValueError를 내보낸다                                         |
|        reverse()함수        |                                                      deque 원소를 역순으로 재정렬하고 None을 반환한다                                                       |
|      reotate(n=1) 함수      |                                       deque의 모든 원소를 n값만큼 오른쪽으로 밀어낸다. n이 음수라면 왼쪽으로 밀어낸다                                       |

---

양쪽 끝의 데이터를 인덱스로 접근하는 것은 O(1)로 시간복잡도가 빠르지만, 가운데 부분에 잇는 데이를 근접하는 것은 o(N)으로 시간복잡도 가 느리다. 그러므로 인덱스를 사용하여 임의의 원소를 무작위로 접근하는 것은 효율적이지 않다.
