# 딕셔너리(Dictionary)

- 목차

  [0. 딕셔너리란?](#0-딕셔너리란)  
   [1. 딕셔너리란 어떻게 만드는가?](#1-딕셔너리는-어떻게-만드는가)  
   [2. 딕셔너리의 쌍 추가, 삭제하기](#2-딕셔너리의-쌍-추가-삭제하기)  
   [　 2-1. 딕셔너리 쌍 추가하기](#2-1-딕셔너리-쌍-추가하기)  
   [　 2-2. 딕셔너리 요소 삭제하기](#2-2-딕셔너리-요소-삭제하기)  
   [3. 딕셔너리의 사용 방법](#3-딕셔너리의-사용-방법)  
   [4. key를 사용해 Value값 얻기](#4-key를-사용해-value값-얻기)  
   [5. 딕셔너리 생성시 주의 사항](#5딕셔너리-생성시-주의-사항)  
   [6. 딕셔너리 관련 함수들](#6-딕셔너리-관련-함수들)  
   [　 6-1. key 리스트 만들기(keys)](#6-1-key-리스트-만들기keys)  
   [　 6-2. Value 리스트 만들기(values)](#6-2-value-리스트-만들기values)  
   [　 6-3. key, Value 쌍 얻기(items)](#6-3-key-value-쌍-얻기items)  
   [　 6-4. Value 쌍 모두 지우기(clear)](#6-4-value-쌍-모두-지우기clear)  
   [　 6-5. key로 value얻기(get)](#6-5-key로-value얻기get)  
   [　 6-6. 해당 key가 딕셔너리 안에 있는지 조사하기(in)](#6-5-key로-value얻기get)

---

## 0. 딕셔너리란?

<ul>
<li>사람의 경우 "이름" = "김아무개", "생일" = "7월 20일"과 같이 구별이 가능하다.   
<li>이러한 대응 관계를 갖는 자료형을 연관 배열(Associative array) 또는 해시(Hash) 라고 한다.  
<li>파이썬에서는 이러한 자료형을 <span style="color:yellow">딕셔너리(Dictionary)</span>라고 한다.
<li> 단어 그대로를 해석하면 사전이라는 뜻 답게 "people" = "사람", "basketball" = "농구공"과 같이 key와 value값을 한쌍으로 갖는 자료형이다.
<li>여기서 key가 "people", "basketball"이라면 value는 "사람", "농구공"이 될 것이다.
<li> 리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않고 key 값을 통해 value값을 바로 읽는 것이 특징이다.
</ul>

---

## 1. 딕셔너리는 어떻게 만드는가?

다음은 딕셔너리의 기본 형태이다.

```
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```

여러 key값과 value 값이 { } 로 둘러 쌓여있고 각각의 요소는 쉼표','로 구분되어있다.

 <ul>
<span style="color:gray">※ Key에는 변하지 않는 값을 사용하고, Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다.
</ul>

예를 통해 알아보자

```m
>>> dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
```

이를 표로 정리하면 다음과 같을 것이다.

> 딕셔너리 예제 dic의 정보

| key   |    value    |
| ----- | :---------: |
| name  |     pey     |
| phone | 01199993323 |
| birth |    1118     |

- key값에는 'name', 'phone', 'birth'
- value값에는 'pey', '01199993323', '1118'

> 딕셔너리의 여러 예

key로 정수 값 1, value로 문자열 'hi'를 사용한 형태

```m
>>> a = {1: 'hi'}
```

또한 다음 예처럼 value에 리스트도 넣을 수 있다.

```m
>>> a = {'a': [1,2,3]}
```

---

## 2. 딕셔너리의 쌍 추가, 삭제하기

### 2-1. 딕셔너리 쌍 추가하기

```m
>>> a = {1: 'a'}
>>> a[2] = 'b'
>>> a
{1: 'a', 2: 'b'}
```

{1:'a'} 딕셔너리에 a[2] = 'b'와 같이 입력하면 딕셔너리 a에 key와 value가 각각 2와 'b'인 2:'b'라는 딕셔너리의 쌍이 추가된다.

```m
>>> a['name'] = 'pey'
>>> a
{1: 'a', 2: 'b', 'name': 'pey'}
```

딕셔너리 a에 'name': 'pey'라는 쌍이 추가되었다.

```m
>>> a[3] = [4,"fine"]
>>> a
{1: 'a', 2: 'b', 'name': 'pey', 3: [4,'fine']}
```

key는 3, value는 [4,'fine']이라는 트리거를 갖는 한 쌍이 추가되었다.

### 2-2. 딕셔너리 요소 삭제하기

```
>>> del a[1]
>>> a
{2: 'b', 'name': 'pey', 3: [4, 'fine']}
```

del 함수를 사용해서 del a[key]값을 지정입력 하면 지정 key에 대한 value가 쌍으로 삭제된다.

## 3. 딕셔너리의 사용 방법

딕셔너리는 주로 어떤걸 표현하는데 사용하는가?

예를 들어 4명의 사람이 있고 각자 특기를 표현할 방법에 대해 생각해보자. 리스트와 문자열로는 표현이 까다로울 수 밖에 없을 것이다.

하지만 딕셔너리는 간단하게 표현이 가능하다.

```
{"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "이필웅":"VSCODE"}
```

## 4. key를 사용해 Value값 얻기

```m
>>> grade = {'pey': 10, 'julliet': 99}
>>> grade['pey']
10
>>> grade['julliet']
99
```

리스트나 튜플, 문자열은 요솟값을 얻고자 할 때 인덱싱이나 슬라이싱 기법 중 하나를 사용했다.

그러나 딕셔너리는 key를 사용해 value를 구하는 방법 한가지만을 사용한다.

위 예시에서 'pey'라는 key의 value값을 얻기 위해 grade['pey']를 사용한 것 처럼 key 의 value를 얻기 위해선 딕셔너리변수이름[key]를 사용해야한다.

추가적인 예로 알아보자

```m
>>> a = {1:'a', 2:'b'}
>>> a[1]
'a'
>>> a[2]
'b'
```

먼저 a 변수에 {1:'a', 2:'b'} 딕셔너리를 대입하였다.

위 예에서 볼 수 있듯이 a[1]은 'a' 값을 돌려준다.

여기에서 a[1]이 의미하는 것은 리스트나 튜플의 a[1]과는 전혀 다르다.

**<span style ="color:gold">딕셔너리 변수에서 [ ] 안의 숫자 1은 두 번째 요소를 뜻하는 것이 아니라 Key에 해당하는 1을 나타낸다.**</span>

앞에서도 말했듯이 딕셔너리는 리스트나 튜플에 있는 인덱싱 방법을 적용할 수 없다.

따라서 a[1]은 딕셔너리 {1:'a', 2:'b'}에서 Key가 1인 것의 Value인 'a'를 돌려주게 된다. a[2] 역시 마찬가지이다.

## 5.딕셔너리 생성시 주의 사항

딕셔너리에서 key는 고유한 값이므로 중복되는 key 값이 존재하면 하나를 제외한 나머지가 모두 무시된다.

```m
>>> a = {1:'a', 1:'b'}
>>> a
{1: 'b'}
```

key가 중복되었을 때 1게를 제외한 나머지 key-value는 무시된다. 왜냐하면 key를 통해 value를 얻는 딕셔너리의 특징 때문이다.

그리고 key에 리스트는 쓸 수없다. 다만 튜플은 가능하다.

딕셔너리의 key값으로 쓸 수 있느냐 없느냐는 key값의 불변성에 달려 있다.

> 리스트를 key로 설정한 경우

```m
>>> a = {[1,2] : 'hi'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

다음과 같이 오류가 발생하여 사용 할 수 없다.

단 value값 에는 변하든 안변하든 상관없이 아무 값이나 넣을 수 있다.

## 6. 딕셔너리 관련 함수들

### 6-1. key 리스트 만들기(keys)

```
>>> a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
>>> a.keys()
dict_keys(['name', 'phone', 'birth'])
```

a.keys()는 딕셔너리 a의 key값을 모아서 dict_keys 객체로 돌려준다.

dict_keys 객체는 다음과 같이 사용할 수 있다. 리스트를 사용하는 것과 차이가 없지만, 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.

```m
>>> for k in a.keys():
...    print(k)
...
name
phone
birth
```

<ul>
    <li><span style ="color:gray">※ print(k)를 입력할 때 들여쓰기를 하지 않으면 오류가 발생하니 주의하자. for문 등 반복 구문에 대해서는 03장에서 자세히 살펴본다.</span>

dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.

```m
>>> list(a.keys())
['name', 'phone', 'birth']
```

### 6-2. Value 리스트 만들기(values)

```m
>>> a.values()
dict_values(['pey', '0119993323', '1118'])
```

Key를 얻는 것과 마찬가지 방법으로 Value만 얻고 싶다면 values 함수를 사용하면 된다. values 함수를 호출하면 dict_values 객체를 돌려준다.

### 6-3. key, Value 쌍 얻기(items)

```m
>>> a.items()
dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
```

items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.

dict_values 객체와 dict_items 객체 역시 dict_keys 객체와 마찬가지로 리스트를 사용하는 것과 동일하게 사용할 수 있다.

### 6-4. Value 쌍 모두 지우기(clear)

```m
>>> a.clear()
>>> a
{}
```

clear 함수는 딕셔너리 안의 모든 요소를 삭제한다.

빈 리스트를 [ ], 빈 튜플을 ( )로 표현하는 것과 마찬가지로 빈 딕셔너리도 { }로 표현한다.

### 6-5. key로 value얻기(get)

```m
>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
>>> a.get('name')
'pey'
>>> a.get('phone')
'0119993323'
```

get(x) 함수는 x라는 key에 대응되는 vlaue값을 돌려준다.a['name']과 동일한 결과값을 돌려받는다.

다만

```m
>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
>>> print(a.get('nokey'))
None
>>> print(a['nokey'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'nokey'
```

다만 다음 예제에서 볼 수 있듯이 a['nokey']처럼 존재하지 않는 키(nokey)로 값을 가져오려고 할 경우 a['nokey']는 Key 오류를 발생시키고 a.get('nokey')는 None을 돌려준다는 차이가 있다. 어떤것을 사용할지는 여러분의 선택이다.

<span style ="color:gray"> ※ 여기에서 None은 "거짓"이라는 뜻이라고만 알아두자.</span>

그리고 딕셔너리 안에 찾으려는 key 값이 없는 경우 미리 정해둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x,'디폴트 값')을 사용하면 편리하다.

```
>>> a.get('foo', 'bar')
'bar'
```

a 딕셔너리에는 'foo'에 해당하는 값이 없다. 따라서 디폴트 값인 'bar'를 돌려준다.

### 6-6. 해당 key가 딕셔너리 안에 있는지 조사하기(in)

```m
>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
>>> 'name' in a
True
>>> 'email' in a
False
```

name' 문자열은 a 딕셔너리의 Key 중 하나이다. 따라서 'name' in a를 호출하면 참(True)을 돌려준다.

반대로 'email'은 a 딕셔너리 안에 존재하지 않는 Key이므로 거짓(False)을 돌려준다.
