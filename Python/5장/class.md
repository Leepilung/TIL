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
4
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

```
class Cookie:
    pass
```

아무런 기능도 지니지 않는 클래스이다. 허나 이런 기능하나 없는 클래스도 객체를 생성할 수 있다.

객체는 클래스로 만들며 1개의 클래스로 무수히 많은 객체를 생성할 수 있다.

```

```
