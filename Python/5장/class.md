# 5-1 클래스

클래스는 C언어에는 없다.

굳이 필요하진 않지만 적재적소에 활용하면 이익이 크다고 할 수 있다.

더하기 기능을 파이썬으로 구현하면 다음과 같다.

```m
result = 0

def add(num):
    global = result
    result += num
    return result

print(add(3))
print(add(4))

-> 실행결과값
3
7
```

만약 계산기가 2대필요하다면? 계산기는 각각의 결과값을 유지해야 하기 때문에 함수를 각각 만들어야 한다.

```m
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return reuslt1

def add2(num):
    gloabl result2
    result2 += num
    reutrn reslut2

print(add1(5))
print(add1(6))
print(add2(7))
print(add2(8))
```

위와 같은 프로그램을 실행시키면

```
5
11
7
15
```

의 결과가 나온다.

그렇다면 클래스(class)를 이용하여 만들어보자.

```m
class Calculator:
    def _init_(self):
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(5))
print(cal1.add(6))
print(cal2.add(7))
print(cal2.add(8))
```

클래스를 사용하여 만든 프로그램을 실행하면

```
5
11
7
15
```

와 같이 함수 2개를 사용한 경우와 동일한 결과가 출력된다.

Calculator 클래스로 만든 별도의 계산기 cal1, cal2(파이썬에서는 이들을 객체라고 부른다.)가 각각의 입력된 역할을 수행한다.

그리고 cal1,cla2는 다른 계산기의 결과값과 관계없이 독립적인 값을 유지한다. 클래스를 사용하면 계산기 대수가 늘어도 객체만 생성하면 되기 때문에 매우 간단하다.

calculator 클래스에 빼기 기능 함수를 추가해보자.

```m
def sub(self, num):
    self.result -= num
    return self.result
```

---

## 클래스와 객체

<img src = "https://wikidocs.net/images/page/28/class_cookie.png">

위의 이미지에서

- 과자 틀 -> 클래스(class)
- 과자 틀로 만들어진 과자 -> 객체(objec)

라고 생각하면 편하다.

클래스로 만든 객체에는 중요한 특징이 있다. 바로 객체마다 고유한 성격을 지닌다는 것이다.

파이썬 클래스의 간단한 예를 알아보자

```m
class Cookie:
    pass
```

아무런 기능도 지니지 않는 클래스이다. 허나 이런 기능하나 없는 클래스도 객체를 생성할 수 있다.

객체는 클래스로 만들며 1개의 클래스로 무수히 많은 객체를 생성할 수 있다.

```m
a = Cookie()
b = Cookie()
```

> [객체와 인스턴스의 차이]

```
클래스로 만든 객체를 인스턴스라고도 한다. 그렇다면 객체와 인스턴스의 차이는 무엇일까?
a =Cookie() 이렇게 만든 a는 객체이다. 그리고 a객체는 Cookie의 인스턴스이다.
즉 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 관계 위주로 설명할 때 사용한다.
a는 객체, a는 Cookie의 인스턴스 라는 표현이 잘 어울린다.
```

## 사칙연산 클래스 만들기

백견이 불여일타. 정말 좋은 말이라고 생각한다.

먼저 'a =Fourcal()' 입력해서 a라는 객체를 만든다.

```
a = Fourcal()
```

그다음 a.setdata(4,2)처럼 입력해서 숫자 4,2를 a에 지정해주고

```
a.setdata(4,2)
```

그 뒤에 a.add()를 수행하면 두 수를 합한 결과(4+2)를 돌려주고

```m
print(a.add())
6
```

a.mul())을 수행하면 두 수를 곱한 결과(4\*2)를 돌려주고

```m
print(a.mul())
8
```

a.sub()를 수행하면 두 수를 뺀 결과 (4-2)를 돌려주고

```m
pirnt(a.sub())
2
```

a.div()를 수행하면 두 수를 나눈 결과 (4 / 2)를 돌려준다.

```m
print(a.div())
2
```

이렇게 동작하는 Fourcal 클래스를 만들어보자.

### 클래스 구조 만들기

1. a = Fourcal() 처럼 객체를 만들어 보자.

```m
>>> class Fourcal:
...     pass
...
```

> <span style=color:gray>※ pass는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 주로 사용한다.</span>

우선 대화형 인터프리터에서 pass란 문장만을 포함한 Fourcal 클래스를 만든다. 아무런 함수나 변수를 포함하지 않아도 우리가 원하는 객체 a를 만들 수 있다.

확인해보자

```m
>>> a = Fourcal()
>>> type(a)
<class '__main__.Fourcal'>
```

`a = Fourcal()`로 a 객체를 먼저 만들고 그 다음에 `type(a)`로 객체가 어떤타입인지 알아보았다.

> <span style=color:gray>※ type 함수는 파이썬이 자체로 가지고 있는 내장 함수로 객체 타입을 출력한다.</span>

## 객체에 숫자 지정할 수 있게 만들기

하지만 생성된 객체 a는 아무런 기능도 하지 못한다. 이제 더하기, 나누기, 곱하기, 빼기등의 사칙연산을 하려면 사용할 숫자 2개를 먼저 알려주어야 한다.

다음과 같이 연산을 수행할 댁상 (4,2)를 지정하게 만들 자면 다음과 같다.

```m
a.setdata(4, 2)
```

위 문장을 수행하려면 다음과 같은 소스 코드가 필요하다.

```m
class Forucal:
    def setdata(self, first, second):
    self.first = first
    self.second = second
```

저기 앞에서 만든 foruclass 클래스 pass 문장은 잊어버리고 setdata로 선언된 함수를 보자.

클래스 안에 구현된 함수는 다른말로 메소드(Method)라고 부른다. 앞으로 클래스 내부의 함수는 항상 메소드라고 표현하니 메소드라는 용어를 기억하자.

일반적으로 파이썬에서 함수는 다음과 같이 작성한다.

```m
def 함수명(매개변수):
    수행 문장
```

메소드도 클래스에 포함되어 있다는 점만 제외하면 일반함수와 다를 것이 크게 없다.

```
def setdata(self, first, second):   #메소드의 매개변수
    self.first = first              #메소드의 수행문
    self.second = second            #메소드의 수행문
```

### 1. setdata 메소드의 매개변수

setdata 메소드는 매개변수로 self, first, second 3개의 입력값을 받는다. 그러나 일반 함수와 달리 메소드의 첫 번째 매개변수 self는 특별한 의미를 지닌다.

다음과 같이 a객체를 만들고 a 객체를 통해 setdata 메소드를 호출해보자.

```m
>>> class Fourcal:
...     def setdata(self,first,second):
...     self.first = first
...     self.second = second
...
>>> a = Fourcal()
>>> a.setdata(4,2)
```

그러나 뭔가 좀 이상하지 않은가? setdata 메소드에는 self, first, second 총 3개의 매개변수가 필요하나 실제로는 `a.setdata(4,2)`처럼 2개의 값만 전달했다.

왜 그럴까? 이유는 `a.setdata(4,2)`처럼 호출하면 setdata의 메소드는 첫 번째 매개변수 self에는 setdata 메소드를 호출한 객체 a가 자동으로 전달된다.

<img src = https://wikidocs.net/images/page/12392/setdata.png>

파이썬 메소드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.

객체를 호출 할 때 객체를 호출한 객체 자신이 전달 되기 때문에 self를 사용한다. 물론 self말고 다른 이름을 사용해도 상관없다.

### 2. setdata 메소드의 수행문

setdata 메소드의 수행문에 대해 알아보자.

```m
class Fourcal:
    def setdata(self, first, second):
    self.first = first
    self.second = second
```

여기에 a.setdata(4,2)처럼 호출하면 setdata 메소드의 매개변수 first, second에는 각각 4와 2가 전다로디어 setdata 메소도의 수행문은 다음과 같이 해석된다.

```m
self.first = 4
self.second = 2
```

self는 전잘된 객체 a이므로 다시 다음과 같이 해석된다.

```m
a.first = 4
a. second = 2
```

`a.first = 4`문장이 수행되면 a 객체에는 first라는 객체변수가 생성되고 값 4가 저장된다.
`a.second =2`의 경우도 같다.

```m
class Fourcal:
    def setdata(self, first, second):
    self.first = first
    self.second = second

>>> a = Fourcal()
>>> a.setdata(4,2)
>>> print(a.first)
4
>>> print(a.second)
2
```

a 객체에 first와 second가 생성됨을 확인할 수 있다.

이번에는 다음과 같이 a, b 객체를 만들어보자.

```m
>>> a = Fourcal()
>>> b = Fourcal()
```

그리고 a 객체의 객체변수 first를 다음과 같이 생성한다.

```m
>>> a = Fourcal()
>>> b = Fourcal()
>>> a.setdata(4,2)
>>> print(a.first)
4
>>> print(a.second)
2
```

그리고 b 객체에 객체변수 frist,second를 다음과 같이 생성한다.

```m
>>> a = Fourcal()
>>> b = Fourcal()
>>> b.setdata(10,20)
>>> print(b.first)
10
>>> print(b.second)
20
```

## 더하기 기능

2개의 숫자를 더하는 기능을 만들어보자.

```m
>>> a = FourCal()
>>> a.setdata(4, 2)
>>> print(a.add())
6
```

위와 같이 더하기 연산이 가능하도록 Fourcal 클래스를 만들어보자.

```m
class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result


a = Fourcal()
b = Fourcal()
a.setdata(10,20)
b.setdata(40,50)

print(a.add())
print(b.add())

30
90
```

이제 곱하기 빼기, 나누기 기능도 추가하여 보자.

```m
class Fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = Fourcal()
b = Fourcal()
a.setdata(10,20)
b.setdata(40,50)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

print(b.add())
print(b.sub())
print(b.mul())
print(b.div())

30
-10
200
0.5

90
-10
2000
0.8
```

정상 출력됨을 확인했으면 다음으로 넘어가자.

## 생성자 (Constructor)

이번에는 Fourcal 클래스를 다음과 같이 사용해보자.

```m
>>> a = FourCal()
>>> a.add()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in add
AttributeError: 'FourCal' object has no attribute 'first'
```

fourcal 클래스에서 인스턴트 a에 setdata 메소드를 수행하지 않고 바로 add 메소드를 실행하면 다음과 같은 오류가 발생한다.

setdata 메소드를 수행해야 객체 a의 객체변수 first와 second가 생성되기 때문이다.

이렇게 객체에 초기값을 설정할 필요가 있을 때에는 setdata와 같은 메소드를 호출하여 초기값을 설정하기 보단 생성자를 구현하는 것이 더 안전한 방법이다.

생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메소드를 의미한다.

파이썬 메소드의 이름으로 **init**을 사용하면 이 메소드는 생성자가 된다.

**init**을 사용하여 위의 Fourcal 클래스에 생성자를 추가해보자.

```m
class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result
```

새롭게 추가된 생성자 `__init__`메서드만 따로 떼어 내서 살펴보자.

```m
def __init__(self, first, second):
    self.first = first
    self.second = second
```

`__init__` 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다. 단 메서드 이름을 `__init__`으로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.

그렇다면 다음의 예를 보자.

```m
>>> a = FourCal()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 2 required positional arguments: 'first' and 'second'
```

`a = Fourcal()`을 수행할 때 생정자 `__init__`이 호출되어 위와 같은 오류가 발생하였다. 오류가 발생한 이유는 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문이다.

위 오류를 해결하려면 다음처럼 first와 second에 해당되는 값을 전달하여 객체를 생성하여야 한다.

```
>>> a = FourCal(4, 2)
>>>
```

위와 같이 수행하면 **init** 메서드의 매개변수에는 각각 오른쪽과 같은 값이 대입된다.

| 매개변수 | 값            |
| :------- | ------------- |
| self     | 생성되는 객체 |
| first    | 4             |
| second   | 2             |

> <span style=color:gray> ※ `__init__` 메서드도 다른 메서드와 마찬가지로 첫 번째 매개변수 self에 생성되는 객체가 자동으로 전달된다는 점을 기억하자. </sapn>

따라서 `__init__` 메소드가 호출되면 setdata 메소드를 호출했을 때와 마찬가지로 frist와 sencd라는 객체변수가 생성될 것이다.

다음과 같이 객체변수의 값을 확인해 보자.

```m
a = Fourcal(10,20)
print(a.first)
print(a.second)

10
20
```

add나 div등도 확인해보자.

```m
a = Fourcal(10,20)
print(a.add())
print(a.div())
print(a.mul())
print(a.sub())

30
0.5
200
-10
```

## 클래스의 상속

상속(Inheritance)란 "물려받다"라는 뜻으로 '재산을 상속받다'라고 할 때의 상속과 같은 의미이다. 클래스에도 이 개념을 적용 할 수 있다.

어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다.

이번에는 상속 개념을 사용하여 우리가 만든 Fourcal 클래스에 a<sup>b</sup>을 구할 수 있는 기능을 추가해 보자.

앞에서 Fourcal 클래스는 이미 만들어 놨으므로 이를 상속하는 MoreFourcal 클래스는 다음과 같이 만들 수 있다.

```m
class MoreFourcal(Fourcal):
   pass

```

클래스를 상속하기 위해선 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.

- <span style = color:gray> calss 이름(상속할 클래스 이름)</sapn>

MoreFourcal 클래스는 Fourcal 클래스를 상속했으므로 Fourcal 클래스의 모든 기능을 사용할 수 있다.

확인해보자.

```m
class MoreFourcal(Fourcal):
    pass

a = MoreFourcal(10,20)

print(a.add())
print(a.mul())
print(a.div())
print(a.sub())

30
200
0.5
-10

```

> 왜 상속을 해야 할까?

보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.

이제 원래 목적인 a의 제곱(a<sup>b</sup>)을 게싼하는 MoreFourcal 클래스를 들어보자.

```m
class MoreFourcal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourcal(10,3)

print(a.pow())
1000

```

## 메서드 오버라이딩

이번에는 Fourcal 클래스를 다음과 같이 실행해보자.

```m
>>> a = FourCal(4, 0)
>>> a.div()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    result = self.first / self.second
ZeroDivisionError: division by zero
```

Fourcal 클래스의 객체 a에 4와 0값을 설정하고 div메소드를 호출하면 4를 0으로 나누려고 하기 때문에 ZeroDivisionError 오류가 발생한다.

하지만 0으로 나눌때 오류가 아닌 0을 돌려주고 싶다면 다음과 같이 만들면 된다.

Fourcal 클래스를 상속하는 SafeFourcal 클래스를 만들어보자.

```m
class SafeFOurcal(Fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
```

SafeFourcal 클래스는 Fourcal 클래스에 있는 div메소드를 동일한 이름으로 다시 작성하였다.

이렇게 부모 클래스(상속한 클래스 = Fourcal)에 있는 메소드를 동일한 이름으로 다시만드는 것을 메소드 오버라이딩(Overriding)
