# 파이썬 기초

- date 2021.05.11

## 목차

[ 1. 반복문 for](#1-반복문-for)  
[ 2. 반복문 while](#2-반복문-while)  
[ 3. 파이썬 함수](#3-파이썬-함수)  
[ 4. 파이썬 숫자형](#4-파이썬-숫자형)  
[ 5. 파이썬 문자열 자료형](#5-파이썬-문자열-자료형)  
[ 6. 여러줄인 문자열을 변수에 대입](#6-여러줄인-문자열을-변수에-대입)  
[ 7. 문자열 인덱싱](#7-문자열-인덱싱)  
[ 8. 문자열 포매팅](#8-문자열-포매팅)  
[ 9. 문자열 정렬](#9-문자열-정렬)  
[ 10. f 문자열 포매팅](#10-f-문자열-포매팅)  
[ 11. 문자열 관련 함수](#11-문자열-관련-함수)

---

## 1. 반복문 for

> for문을 사용하면 실행해야 할 문장을 여러 번 반복해서 실행시킬 수 있다. for문 사용하여 대괄호 사이의 값을 하나씩 출력한다.

```
>>> for a in [1, 2, 3]:
...   print(a)
...
1
2
3
```

## 2. 반복문 while

```
>>> i = 0
>>> while i < 3:
...     i=i+1
...     print(i)
...
1
2
3
```

> for문과 마찬가지로 반복 문장 수행이 가능하다. i 값이 3이상 일경우 종료된다.

## 3. 파이썬 함수

> 보통 def라는 함수를 만들때 사용하는 예약어를 사용한다.

```
def add(a, b):
    return a+b


a = add(3, 4)
print(a)
...
 7
...
```

## 4. 파이썬 숫자형

- 나눗셈 몫을 반환 하는 // 연산자

```
>>> 7 // 4
1
```

1.75에서 몫에 해당하는 정수값 1만을 돌려준다.

## 5. 파이썬 문자열 자료형

> 총 4가지 방법이 있다.

<ul>
    <li>큰 따옴표(")로 양쪽 둘러싸기
    <li>작은 따옴표(')로 양쪽 둘러싸기
    <li> 큰 따옴표 3개를 연속(""")
    <li> 작은 따음표 3개를 연속(''')
</ul>

## 6. 여러줄인 문자열을 변수에 대입

> 이스케이프 코드 삽입을 이용한다. 여기서 이스케이프 코드란? 여러 줄의 코드를 보기 좋게 정렬하는 용도로 주로 이용되는 코드를 말한다.

| 코드   |                          설명                           |
| ------ | :-----------------------------------------------------: |
| `\n`   |             문자열 안에서 줄을 바꿀 때 사용             |
| `\t`   |           문자열 사이에 탭 간격을 줄 때 사용            |
| `\\`   |             문자 \를 그대로 표현할 때 사용              |
| `\'`   |          작은따옴표(')를 그대로 표현할 때 사용          |
| `\"`   |           큰따옴표(")를 그대로 표현할 때 사용           |
| `\r`   | 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동) |
| `\f`   |    폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)    |
| `\a`   |    벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)    |
| `\b`   |                       백 스페이스                       |
| `\000` |                         널 문자                         |

이 중에서도 활용빈도가 높은 것들은 `\n`, `\t`, `\\`, `\'`, `\"` 이다.

예시)

```
>>> Multiline = "Life is too short\nYou need python"
Life is too short
You need python
```

그러나 이 경우 문장이 지저분해지고 길어진다.

큰 따음표나 작은 따음표를 사용하는 것이 훨씬 깔끔하다.

예시)

```
multiline='''(""")
Life is too short
You need python
'''(""")
```

## 7. 문자열 인덱싱

```m
a = "Life is too short, You need Python"
```

변수 a에 저장한 문자열의 번호를 매겨 보면 다음과 같다.

```m
Life is too short, You need Python
0         1         2         3
0123456789012345678901234567890123
```

파이썬은 숫자를 0부터 센다. 이점에 유의해야 한다.

## 8. 문자열 포매팅

> 숫자 대입의 경우 (%d)

```m
>>> "I eat %d apples." % 3
'I eat 3 apples.'
```

%에 숫자를 대입하는 경우에는 %d문자를 이용한다.

> 문자열 대입의 경우 (%s)

```m
>>> "I eat %s apples." % "five"
'I eat five apples.'
```

숫자 대신 문자열을 넣는 경우엔 %d가 아닌 %s 문자열을 사용해야 한다.

> 두가지 값 이상을 넣는 경우

```m
>>> number = 10
>>> day = "three"
>>> "I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'
```

| 코드 |           설명           |
| ---- | :----------------------: |
| %s   |      문자열(String)      |
| %c   |   문자 1개(character)    |
| %d   |      정수(Integer)       |
| %f   | 부동소수(floating-point) |
| %o   |          8진수           |
| %x   |          16진수          |
| %%   | Literal % (문자 % 자체)  |

> 포메팅 연산자 %s

%s는 뒤에 삽입되는 모든 문자를 문자열로 인식한다.

```m
>>> "I have %s apples" % 3
'I have 3 apples'
>>> "rate is %s" % 3.234
'rate is 3.234'
```

3을 문자열 안에 삽입하려면 %d를 사용하고, 3.234를 삽입하려면 %f를 사용해야 한다.  
하지만 %s를 사용하면 이런 것을 생각하지 않아도 된다.  
 왜냐하면 %s는 자동으로 % 뒤에 있는 값을 문자열로 바꾸기 때문이다.

> 포메팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다.

```m
>>> "Error is %d%%." % 98
'Error is 98%.'
```

다음의 형태를 기억해두자.

## 9. format 함수를 이용한 포매팅

> 숫자 대입의 경우

```m
>>> "I eat {0} apples".format(3)
'I eat 3 apples'
```

> 문자열 대입의 경우

```m
>>> "I eat {0} apples".format("five")
'I eat five apples'
```

> 숫자 값을 가진 변수 대입

```m
>>> number = 3
>>> "I eat {0} apples".format(number)
'I eat 3 apples'
```

> 2개 이상의 값 넣기

```m
>>> number = 10
>>> day = "three"
>>> "I ate {0} apples. so I was sick for {1} days.".format(number, day)
'I ate 10 apples. so I was sick for three days.'
```

2개 이상의 값을 넣을 경우 문자열의 {0} {1} 와 같은 인덱스 항목이 입력값 순서에 맞게 바뀐다.

> 이름으로 넣기

```m
>>> "I ate {number} apples. so I was sick for {day} days.".format(number=10, day="three")
'I ate 10 apples. so I was sick for three days.'
```

이경우 안에 값을 문자열로 할경우 " " 처리 해줘야한다.

## 9. 문자열 정렬

> 왼쪽 정렬 (<방향)

```m
>>> "{0:<10}".format("hi")
'hi        '
```

> 오른쪽 정렬 (>방향)

```m
>>> "{0:>10}".format("hi")
'        hi'
```

> 가운데 정렬 (^방향)

```m
>>> "{0:^10}".format("hi")
'    hi    '
```

> 공백 채우기 (=,!의 기호들)

```m
>>> "{0:=^10}".format("hi")
'====hi===='
>>> "{0:!<10}".format("hi")
'hi!!!!!!!!'
```

다른 문자열도 가능하나 단일 문자열만 가능함. 2단어 이상 불가.

> 소수점 표현

```m
>>> y = 3.42134234
>>> "{0:0.4f}".format(y)
'3.4213'
```

소수점을 4자리까지만 표현하는 함수.

> '{' 또는 '} '문자 표현하기

```m
>>> "{{ and }}".format()
'{ and }'
```

2중으로 사용하면 된다.

## 10. f 문자열 포매팅

> 파이썬 3.6 이상부터 사용 가능.

```m
>>> name = '홍길동'
>>> age = 30
>>> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
```

> f문자열 포매팅은 표현식을 지원한다

<ul><li><span style="color:gray">※ 표현식이란 문자열 안에서 변수와 +, -와 같은 수식을 함께 사용하는 것을 말한다.</li></ul>
```m
>>> age = 30
>>> f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'
```

> 딕셔너리

<ul><li><span style="color:gray">※ 딕셔너리는 Key와 Value라는 것을 한 쌍으로 갖는 자료형이다.</li></ul>
```m
>>> d = {'name':'홍길동', 'age':30}
>>> f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
```

> 정렬

```m
>>> f'{"hi":<10}'  # 왼쪽 정렬
'hi        '
>>> f'{"hi":>10}'  # 오른쪽 정렬
'        hi'
>>> f'{"hi":^10}'  # 가운데 정렬
'    hi    '
```

> 공백 채우기

```m
>>> f'{"hi":=^10}'  # 가운데 정렬하고 '=' 문자로 공백 채우기
'====hi===='
>>> f'{"hi":!<10}'  # 왼쪽 정렬하고 '!' 문자로 공백 채우기
'hi!!!!!!!!'
```

> 소수점 표현

```m
>>> y = 3.42134234
>>> f'{y:0.4f}'  # 소수점 4자리까지만 표현
'3.4213'
>>> f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
'    3.4213'
```

## 11. 문자열 관련 함수

> 문자 개수 세기 (Count)

```m
>>> a = "hobby"
>>> a.count('b')
2
```

문자열 중 b의 개수를 알려준다.

> 위치 알려주기1(find)

```m
>>> a = "Python is the best choice"
>>> a.find('b')
14
>>> a.find('k')
-1
```

문자열이 나온 위치를 반환한다.  
'b'의 경우 0부터 세기 때문에 14를 반환한다.  
'k'의 경우처럼 문자나 문자열이 존재하지 않는다면 -1의 값을 반환한다.

> 위치 알려주기2(index)

```m
>>> a = "Life is too short"
>>> a.index('t')
8
>>> a.index('k')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: substring not found
```

찾고자 하는 문자의 위치를 반환한다. 대소문자의 차이도 구별하기 때문에 유의할 것

> 문자열 삽입(join)

```m
>>> ",".join('abcd')
'a,b,c,d'
```

abcd 문자열 사이에 ','를 삽입

> 소문자-> 대문자 변환(upper)

```m
>>> a = "hi"
>>> a.upper()
'HI'
```

> 대문자 -> 소문자 변환(lower)

```m
>>> a = "HI"
>>> a.lower()
'hi'
```

> 왼쪽 공백 지우기 (lstrip)

```m
>>> a = " hi "
>>> a.lstrip()
'hi '
```

> 오른쪽 공백 지우기(rstrip)

```m
>>> a= " hi "
>>> a.rstrip()
' hi'
```

> 양쪽 공백 지우기(strip)

```m
>>> a = " hi "
>>> a.strip()
'hi'
```

> 문자열 바꾸기(replace)

```m
>>> a = "Life is too short"
>>> a.replace("Life", "Your leg")
'Your leg is too short'
```

> 문자열 나누기(split)

```m
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> b = "a:b:c:d"
>>> b.split(':')
['a', 'b', 'c', 'd']
```

split 함수는 a.split()처럼 괄호안에 아무값이 없으면 공백을 기준으로 문자열을 자동으로 나눈다.

만약 b.split(':')처럼 괄호안에 특정 값이 있을 경우에는 괄호안의 값을 기준으로 문자열을 나눠준다.