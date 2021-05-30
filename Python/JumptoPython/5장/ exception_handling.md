# 예외 처리

프로그램을 만들면 수없이 많은 오류를 만난다. 오류의 발생 이유는 프로그램이 잘못 동작하는 것을 막기 위한 파이썬의 배려라고 보면 된다.

하지만 때때로 이런 오류를 무시하고 싶을 때 사용하는 방법이 있는데 대표적으로 `try`, `except`문을 사용하는 것이다.

---

## 오류는 어떤 때 발생하는가?

파이썬에는 굉장히 많은 오류가 있다. 대표적으로 실제 프로그램에서 자주 발생하는 오류를 중심으로 어떤 오류가 발생하는지를 알아보자.

우선 디렉토리 안에 없는 파일을 열려고 시도했을 때 발생하는 오류이다.

```mm
>>> f = open("나없는파일", 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'
```

없는 파일을 열려고 시도하면 `FileNotFoundError` 오류가 발생한다.

다음은 0으로 다른숫자를 나누는 경우이다.

```mm
>>> 4 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

4를 0으로 나누려고 하니 `ZeroDivisionError` 오류가 발생한다.

그리고 가장 대표적인 오류를 알아보자.

```mm
>>> a = [1,2,3]
>>> a[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

out of range 오류이다. 위 예시에서 리스트 a는 [1,2,3]인데 a[4]는 a 리스트에서 얻을 수 없는 값이다. 따라서 IndexError 오류가 발생한다. 파이썬에서는 이런 오류들이 발생하면 프로그램을 중단하고 오류 메시지를 보여 준다.

---

## 오류 예외 처리 기법

대표적으로 `try`문과 `except`문이 있다.

이 둘의 기본 구조는 다음과 같다.

```mm
try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
```

try 블록 수행 중에 오류가 발생하면 except 블록이 수행된다. 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

excpet구문을 자세히 살펴보면

- <span style=color:gray>except [발생 오류 [as 오류 메시지 변수]]:3 </span>
  위 구문은 [] 기호를 사용하는데, 이 기호는 괄호 안의 내용을 생략할수 있다는 관례적 표기법이다. 즉 except 구문은 다음 3가지 방법으로 사용이 가능하다.

## 1. try,except만 쓰는 방법

```m
try:
    ~~~
except:
    ~~~
```

이 경우에는 오류 종류와 관계없이 오류가 발생하면 except 블록을 수행한다.

## 2. 발생 오류만 포함한 except문

```m
try:
    ~~~
except 발생 오류:
    ~~~
```

이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행한다는 의미이다.

## 3. 발생 오류와 오류 메시지 변수까지 포함한 except문

```m
try:
    ~~~
except 발생 오류 as 오류 메시지 변수:
    ~~~
```

이 경우는 2번째 경우에서 오류 메시지의 내용까지 알고 싶을 떄 사용하는 방법이다.

3번째 방법의 예를 들어보자.

```m
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
```

예시처럼 4를 0으로 나누려고하면 ZeroDivisionError가 발생하여 except 블록이 실행되고 변수 e에 담기는 오류메시지를 다음과 같이 출력한다.

- <span style=color:gray>결과값 : division by zero </span>

---

## try .. finally

try 문에는 finally 절을 사용할 수 있다. finally 절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 보통 finally절은 사용한 리소스를 close해야할 때 많이 사용한다.

에시를 들어보자

```
f = open('foo.txt', 'w')
try:
    #어저구저쩌구를 수행한다.
finally:
    f.close()
```

위 예시를 해석하면 foo.txt 파일을 쓰기 모드로 연 후에 try문을 수행한 후 예외 발생 여부와 상관없이 finally절에서 f.close()로 열린 파일을 닫을 수 있다.

## 여러개의 오류 처리하기

try문 안에서 여러 개의 오류를 처리하려면 다음과 같이 구문을 사용하면 된다.

```m
try:
    ~~~
except 발생 오류1:
    ~~~
except 발생 오류2:
    ~~~
```

위 구문을 예시로 들어보자면 0으로 나누는 오류와 인덱싱 오류를 한번에 처리할 수 있다.

```m
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print('인덱싱 할 수 없습니다.')
```

위를 실행시켜보면 '인덱싱 할 수 없습니다.'라는 에러메시지만 등장한다.

a는 2개의 요솟값을 가지고 있기 때문에 a[3]는 IndexEeror를 발생시켜 '인덱싱할 수 없습니다' 라는 문자열이 출력된다.

이는 인덱싱 오류가 먼저 발생하여서 4/0으로 발생되는 'ZeroDivisionError'오류는 발생하지 않은 것이다.

그리고 위에서 알아본 것과 마찬가지로 오류메시지를 다음과 같이 가져올 수도 있다.

```m
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
```

위 프로그램을 실행시키면 'list index out of range' 오류메시지가 출력된다.

그리고 ZeroDivisionError와 IndexError를 동시에 처리할 수도 있다.

```m
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
```

2개 이상의 오류를 동일하게 처리하기 위해서는 위와 같이 괄호를 사용하여 함께 묶어 처리하면 된다.

---

## try문에 else절 사용하기

try문에는 다음처럼 else절을 사용할 수 있다.

```m
try:
    ~~~
except [발생 오류[as 오류 메시지 변수]]:
    ~~~
else: #오류가 없을 경우에만 수행된다.
    ~~~
```

try문 수행중에 오류가 발생하면 except절이 수행되고 오류가 없으면 else절이 수행되는 것이다.

다음은 try문에 else절을 활용한 예시이다.

```m
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
```

나이를 입력하라는 질문에 숫자가 아닌 다른값을 입력할 경우 오류가 발생하여 '입력이 정확하지 않습니다'라는 문장을 출력하고, 오류가 없을 경우에는 else절을 수행한다.

실행한 결과는 다음과 같다.

```m
나이를 입력하세요: 15
미성년자는 출입금지입니다.

나이를 입력하세요: 19
환영합니다.

나이를 입력하세요:      #아무것도 입력하지 않았음
입력이 정확하지 않습니다.
```

---

## 오류 회피하기

프로그래밍을 하다 보면 특정 오류가 발생할 경우 그냥 통과시켜야 할 때가 있다.

ex)

```m
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass
```

try문 안에서 FileNotFoundError가 발생할 경우 pass를 사용하여 오류를 그냥 회피하도록 작성한 예이다.

## 오류 일부러 발생시키기

프로그래밍을 하다 보면 종종 오류를 일부러 발생시켜야 할 경우도 있다. 파이썬에선 `raise`명령어를 사용해 오류를 강제로 발생시킬 수 있다.

예를 들어 Bird클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶은 경우를 예로 들어보자.

```mm
class Bird:
    def fly(self):
        raise NotImplementedError
```

- <span style=color:gray>※ NotImplementedError는 파이썬 내장 오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용한다.</span>

위 예제는 Bird 클래스를 상속받는 자식 클래스는 반드시 fly 함수를 구현해야 한다는 의지를 보여준다.

만약 자식 클래스 fly가 함수를 구현하지 않은 상태로 fly 함수를 호출한다면 어떻게 될까?

```mm
class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()
```

Eagle 클래스는 Bird 클래스를 상속받는다.

그런데 Eagle 클래스에서 fly 함수를 구현하지 않았기 때문에 Bird 클래스의 fly 함수가 호출된다.

그리고 fly 함수에 있는 raise문에 의해 NotImplementedError가 발생할 것이다.

```mm
Traceback (most recent call last):
  File "...", line 33, in <module>
    eagle.fly()
  File "...", line 26, in fly
    raise NotImplementedError
NotImplementedError
```

다음과 같이 NotImplementedError가 발생되지 않게 하려면 반드시 Eagle 클래스에 fly 함수를 구현하여서 Bird 클래스의 fly 함수를 덮어씌워야 한다.

- <span style=color:gray> \* <span style=color:gray>※ NotImplementedError는 파이썬 내장 오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용한다.</span> </span>

```mm
class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()
```

위 예시처럼 fly 함수를 구현하고 프로그램을 실행하면 오류없이 다음 문장이 잘 출력이 된다.

'very fast'

## 예외 만들기

프로그램 수행 도중 특수한 경우 예외 처리를 하기 위해 종종 예외를 만들어 사용한다.

예외는 파이썬 내장 클래스인 `Exception`클래스를 상속하여 만들 수 있다.

```mm
class MyError(Exception):
    pass
```

그리고 별명을 출력해주는 함수를 다음과 같이 작성하고 호출해보자.

```mm
def say_nick(nick):
  if nick == '바보':
      raise MyError()
  print(nick)

say_nick('천사')
say_nick('바보')
```

그러고 프로그램을 실행하면

```mm
천사
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    say_nick('바보')
  File "test.py", line 7, in say_nick
    raise MyError()
__main__.MyError
```

과 같은 에러가 발생한다.

이번에는 예외 처리 기법을 사용하여 MyError 발생을 예외처리 해보자.

```mm
class MyError(Exception):
    pass

def say_nick(nick):
  if nick == '바보':
      raise MyError()
  print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")
```

이 프로그램을 실행하면 다음과 같이 출력된다.

```
천사
허용되지 않는 별명입니다.
```

만약 오류 메시지를 사용하고 싶다면 다음처럼 예외 처리를 하면 된다.

```mm
class MyError(Exception):
    pass

def say_nick(nick):
  if nick == '바보':
      raise MyError()
  print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
```

하지만 위 프로그램을 실행해 보면 print(e)로 오류메시지가 출력되지 않는다.

오류 메시지를 출력했을 때 오류메시지가 보이게 하려면 오류 클래스에 다음과 같은 `__str__` 메소드를 구현해야 한다. `__str__` 메소드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메소드이다.

```mm
class MyError(Exception):
    def __str__(self):
        return '허용되지 않는 별명입니다'
```

이와 같이 MyError 클래스문을 수정하고 프로그램을 실행해보면 '허용되지 않는 별명입니다' 라는 오류메시지가 출력되는 것을 확인할 수 있다.
