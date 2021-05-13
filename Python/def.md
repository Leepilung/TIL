# 파이썬 함수 구조

```
def 함수명(매개변수)
    <문장1>
    <문장2>
```

def는 함수를 만들 때 사용하는 예약어이다.
함수명은 임의로 설정이 가능하다.

```m
def add(a, b):
    return a + b
```

위 함수를 정리하면 함수 이름은 add  
 a, b 2개의 값으로 입력을 받으며 결과값은 a + b 이다.

★ **return은 함수의 결과값을 돌려주는 명령어이다.**

예시로 add 함수를 만들면 다음과 같다.

```m
def add(a,b):
    return a+b
```

이를 응용해서 사용하면

```
a = 5
b = 6
c = add(a, b)
print(c)
11
```

다음의 결과가 나온다.

---

## 매개변수와 인수

매개변수(parameter)와 인수(arguments)는 혼용되서 사용되어 헷갈리는 용어들이다.

```
def add(a, b):
    return a+b
```

위에서 # a, b는 매개변수에 해당된다.

```
print(add(3, 4))
```

add함수 안의 3, 4는 인수에 해당된다.

---

## 일반적인 함수

```
def 함수이름(매개변수):
    <수행문장1~N>

    return 결과값
```

-입력값과 결과값이 있는 함수의 일반적 형태이다.

예시1)

```m
def add(a,b):
    result = a+b
    return result
```

위의 형태는 add라는 함수를 정의하고 이 add 함수는 a, b라는 두개의 입력값을 받아 a+b 라는 result를 만들고 return함수에 의해 이 결과값을 돌려받는다.  
라고 해석하면 된다.

그렇다면 위의 함수를 사용하는 방법은 다음과 같다.

```m
def add(a,b):
    result = a+b
    return result

a = add(6,7)
print(a)
```

위의 함수를 선언해 둔상태에서 결과를 받을 변수 = 함수명(인수1,인수2)의 형태를 만들면 되는 것이다.

---

## 입력값이 없는 함수

```
def say()
    return 'Hello World'
```

입력값이 없는 함수의 기본 형태이다.
매개변수를 나타내는 ( ) 괄호 부분이 비어있다.

이 함수를 사용하는 예시는

```
def basic():
    return 'Hello World'

a = basic()
print(a)
Hello World
```

의 형태를 이용한다. basic()에 아무것도 넣지 않아도 Hello world가 출력되는 모습이다.

---

## 결과값이 없는 함수

```m
def add (a, b):
    print ("%d의 힘과  %d의 힘을 합치면 %d의 힘이됩니다."% (a, b, a+b*2))
```

임의로 짠 형태이나 결과값이 존재하지 않는 형태는 위와 같다.

위와 같은 형태를 사용하기 위해선

```md
def add (a, b):
print ("%d의 힘과 %d의 힘을 합치면 %d의 힘이됩니다."% (a, b, a+b\*2))

test = add(30,50)

> python3 ./BASIC.PY
> 30의 힘과 50의 힘을 합치면 130의 힘이됩니다.
```

다음의 결과가 나온다.

- 결국 함수명과 매개변수의 형태를 잡아놓고 별도로 변수 = 함수명(매개변수)의 꼴을 지정해줘야 사용할 수 있는 형태이다.

책에서의 주의사항 print 문은 위에서 언급한 <수행 문장>의 부분을 의미한다. 결과값을 돌려받는 명령어는 오직 return뿐임을 기억하자.

```md
def add (a, b):
print ("%d의 힘과 %d의 힘을 합치면 %d의 힘이됩니다."% (a, b, a+b\*2))

test = add(30,50)
print(test)

> python3 ./BASIC.PY
> 30의 힘과 50의 힘을 합치면 130의 힘이됩니다.
> None
```

위와 같은 형태를 살펴보면 결국
a 값은 None이 출력됨을 알 수있다.

---

## 입력값도 결과값도 없는 함수

```
def 함수명():
        print('Final Fantasy')

함수명()
Final Fantasy
```

매개변수 x return문도 x -> 입력값 x 결과값 x 의 함수이다.

이 함수의 활용 형태는 위와 같다고 할 수 있다.

---

## 매개변수 지정하기

```m
def 함수명(인수1, 인수2):
    return 인수1 + 인수2
```

위에선 add로 썼으나 함수명이라고 알아보기 쉽게 바꾼 예제이다.

매개변수를 다음과 같이 지정이 가능하다.

```m
def 함수명(인수1, 인수2):
    return 인수1 + 인수2

결과 = 함수명(인수1 = 30,인수2 = 70)
print(결과)
> python3 ./BASIC.PY
100
```

매개변수 지정시 순서는 상관없이 가능하다.

```
def 함수명(인수1, 인수2):
    return 인수1 + 인수2

결과 = 함수명(인수2 = 30,인수1 = 70)
print(결과)
> python3 ./BASIC.PY
100
```

---

## 입력값이 여러개인 경우

입력값을 모두 더하는 함수를 만든다고 가정할 때 함수가 몇개가 필요한지는 모른다.

예시로 함수명이라는 함수에 인수로 (1,2)이면 3, (1,2,3)이면 6, (1,2,3,4,5,6,7,8,9,10) 이면 55를 돌려주는 함수를 만들어 보자.

```m
def 함수명(*매개변수n개):
    결과 = 0
    for i in 매개변수n개:
        결과 = 결과 + i
    return 결과
```

형태는 다음과 같을 것이다.

매개변수 앞에 *를 붙이면 입력값이 여러개여도 상관이 없다. *을 붙이면 입력값을 전부 모아 튜플로 자동으로 만들어 준다.

직접 실행해보자.

```m
def 함수명(*매개변수n개):
    결과 = 0
    for i in 매개변수n개:
        결과 = 결과 + i
    return 결과

결과 = 함수명(1,2,3)
print(결과)

결과 = 함수명(1,2,3,4,5,6,7,8,9,10)
print(결과)
> python3 ./BASIC.PY
6
55
```

의 결과가 나옴을 알 수 있다.

다음의 예를 보자.
매개변수가 (매개변수1,\*매개변수들)의 구성으로 되어있는 예시이다.

```m
def 함수명1(선택,*매개변수들):
    if 선택 == "더하기":
        결과 = 0
        for i in 매개변수들:
            결과 = 결과 + i
    elif 선택 == "곱하기":
        결과 = 1
        for i in 매개변수들:
            결과 = 결과 * i
    return 결과
```

이 함수의 경우 다음과 같이 사용할 수 있다.

```
def 함수명1(선택,*매개변수들):
    if 선택 == "더하기":
        결과 = 0
        for i in 매개변수들:
            결과 = 결과 + i
    elif 선택 == "곱하기":
        결과 = 1
        for i in 매개변수들:
            결과 = 결과 * i
    return 결과

결과 = 함수명1('더하기', 1,2,3,4,5)
print(결과)

결과 = 함수명1("곱하기", 1,2,3,4,5)
print(결과)
> python3 ./BASIC.PY
15
120
```

---

## 키워드 파라미터

키워드 파라미터를 사용할땐 매개변수 앞에 별 두개(\*\*)를 붙인다.

```m
def 함수명(**키워드파라미터):
    print(키워드파라미터)
```

실 사용 예는 다음과 같다.

```m
def 함수명(**키워드파라미터):
    print(키워드파라미터)

함수명(SAMPLE1='Python')

함수명(SAMPLE2='JavaScript')
> python3 ./BASIC.PY
{'SAMPLE1': 'Python'}
{'SAMPLE2': 'JavaScript'}
```

딕셔너리의 키 벨류 관계를 만들어서 출력시켜주는 함수다.

---

## 결과값은 하나뿐

```m
def 더하기_and_곱하기(a,b):
    return a+b, a*b
```

다음과 같은 형태에선 결과가 2개가 나올지 1개가 나올지 예상해보자.

```m
def 더하기_and_곱하기(a,b):
    return a+b, a*b

결과 = 더하기_and_곱하기(10,20)
print(결과)
> python3 ./BASIC.PY
(30, 200)
```

결과값으로 1개의 결과값이 나오고 그 결과값은 (30, 200)이라는 튜플 값을 갖게 된다.

하나의 튜플값이 아닌 2개의 결과값으로 받고 싶으면

```m
def 더하기_and_곱하기(a,b):
    return a+b, a*b

결과1, 결과2 = 더하기_and_곱하기(10,20)
print(결과1, 결과2)
> python3 ./BASIC.PY
30 200
```

의 형태로 하면 된다.

---

## return의 추가형태

```
def 함수명(매개변수1):
    if 매개변수1 == "웅이":
        return
    print("나의 별명은 %s 입니다."% 매개변수1)

함수명('웅이')
> python3 ./BASIC.PY
>
함수명('웅)
> python3 ./BASIC.PY
나의 별명은 웅 입니다.
```

return은 함수를 빠져나가고 싶은 상황에서 사용이 가능하다.

---

## 매개변수 초기값 설정

```m
def 내이름말하기(이름, 나이, 남성=True):
    print("나의 이름은 %s 입니다."% 이름)
    print("나이는 %s살 입니다."% 나이)
    if 남성:
        print("남성입니다.")
    else:
        print("여성입니다.")
```

'내이름말하기' 함수에서 남성=True 부분의 매개변수 처럼 매개변수에 미리 값을 엏어두는 방법을 말한다.

```
def 내이름말하기(이름, 나이, 남성=True):
    print("나의 이름은 %s 입니다."% 이름)
    print("나이는 %s살 입니다."% 나이)
    if 남성:
        print("남성입니다.")
    else:
        print("여성입니다.")

내이름말하기 ('이필웅',29)
내이름말하기 ('이필웅',29,True)
> python3 ./BASIC.PY
나의 이름은 이필웅 입니다.
나이는 29살 입니다.
남성입니다.
나의 이름은 이필웅 입니다.
나이는 29살 입니다.
남성입니다.
```

와 같은 형태에서는
아래 두 내이름말하기 함수의 결과값이 동일하다.
또한 남성 부분을 입력하지 않았음에도 초기값이 설정되어 있어서 남성으로 출력이 되고있는 모습이다.

---

## 함수 안에서 밖의 변수를 변경하는 방법.

> 1.  return 사용하기

```
a = 1
def 함수명(a):
    a = a +1
    return a

a = 함수명(a)
print(a)

> python3 ./BASIC.PY
2
```

'함수명' 함수는 입력으로 들어온 값에 1을 더한 값을 돌려준다.

이떄 변수 a = 함수명(a)로 대입해버리면 a가 '함수명'함수의 결과값으로 바뀐다. 물론 함수 안의 a 매개변수와 함수 밖의 변수 a는 다르다.

> 2.  global 사용하기

```m
a = 1
def 테스트():
    global a
    a = a+1

테스트()
print(a)

> python3 ./BASIC.PY
2
```

global 명령어를 사용한 방법. global a 이 문장은 함수 밖의 a 변수를 직접 사용하겠다는 의미이다.

그러나 프로그래밍에서는 global은 가급적 사용하지 않는것이 좋다. 함수는 독립적으로 존재하는 것이 좋기 때문.

## lambda(람다)

lambda는 함수를 생성할 때 사용하는 명령어로 def와 동일한 역할.

사용법은

> lambda 매개변수1, 매개변수2 .. : 매개변수 식

예제는 다음과 같다.

```m
더하기 = lambda a, b: a+b
result = 더하기(3, 4)
print(result)

> python3 ./BASIC.PY
7
```

def 함수와 비교해보자.

```m
def 더하기(a,b):
    return a+b

result = 더하기(3,4)
print(result)

> python3 ./BASIC.PY
7
```

차이점은 lambda 예약어로 만든 함수는 return 명령어가 없어도 결과값이 나온다는 점이다.

# 사용자 명령어

## 사용자 입력

> input

```
>>> a = input
>>> a = input()
Life is very good, but too short
>>> a
'Life is very good, but too short'
```

input은 입력되는 모든 값을 문자열로 취급한다.

> 프롬프트 사용

사용자에게 입력받을 때 "숫자를 입력하시오"나 "이름을 입력하시오"등의 안내 문구, 질문이 나오도록 하는 경우가 있다.

```
>>> input("입력하시오")
입력하시오
```

활용하여 예시를 만들어보자.

```m
숫자 = input("숫자를 입력하시오")
>>> 숫자 = input("숫자를 입력하시오")
숫자를 입력하시오3
print(숫자)
3
```

---

## print 에 대해

print문은 우리가 입력한 자료형을 출력하는 용도였다.

```
변수1 = 2021
print(변수1)
> python3 ./BASIC.PY
2021

변수2 = "Vscode+Phyton"
print(변수2)
> python3 ./BASIC.PY
Vscode+Phyton
```

> 큰따옴표(")로 둘러 싸인 문자열은 +연산과 동일하다.

```
print("hello" "my" "yesterday")
> python3 ./BASIC.PY
hellomyyesterday
print("hello"+"my"+"yesterday")
> python3 ./BASIC.PY
hellomyyesterday
```

> 문자열 띄어쓰기는 콤마로 한다.

```
 print("hello","my","yesterday")
 > python3 ./BASIC.PY
hello my yesterday
```

> 한 줄에 결과값 출력

for문에서 구구단 예제의 일부분을 생각하면 된다.
한줄에 이어서 출력하고싶으면 end를 사용하면 된다.

```
for i in range(3):
    print(i)
> python3 ./BASIC.PY
0
1
2
```

이경우에는 이렇게 출력이 되므로

```
for i in range(3):
    print(i, end=(" "))
> python3 ./BASIC.PY
0 1 2
```

이런식으로 사용해야 한다.

print문은 평소에 끝부분이 자동으로 줄바꿈 처리되기 때문에 end=' '를 별도로 지정해서 처리하는것이라고 보면 된다.

# 파일 읽고 쓰기

파일을 통한 입출력 방법을 정리하는 항목이다.

## 파일 생성하기

```
f = open("새파일.txt", 'w')
f.close
```

와 같이 입력하면 vscode 좌측에 새파일.txt라는 파일이 새로 생성된다.

open함수는 파이썬 내장 함수인데

- 파일 객체 = open(파일 이름, 파일 열기 모드)

의 형태를 가진다.

파일 열기 모드는 다음의 표를 참고하자.

| 파일열기모드 |                            설명                            |
| :----------- | :--------------------------------------------------------: |
| r            |            읽기모드 - 파일을 읽기만 할 때 사용             |
| w            |            쓰기모드 - 파일에 내용을 쓸 때 사용             |
| a            | 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용 |

파일을 쓰기모드 'w'로 쓸 경우 해당 파일이 존재하면 기존 내용이 모두 사라지고 해당파일이 존재하지 않으면 새로운 파일이 생성된다.

위의 예시로 예를들면 새파일.txt를 쓰기모드 'w'로 열면 새파일.txt라는 이름의 새로운 파일이 현재 디렉토리에 생성되는 원리이다.

그리고 만약 특정 디렉토리 경로에 이를 생성시키고 싶다면 다음과 같이 작성한다.

```
f = open("/home/ek3434/TIL/Python/새파일.txt","w")
f.close
```

위와 같이 VSCODE 기반의 경로를 지정하여 실행시킬경우 실제 새파일.txt의 내용이 삭제되고 다시 생성됨을 확인 할 수 있었다.

---

## 파일을 쓰기 모드로 열어 출력값 적기

파일을 직접 열고 출력값을 파일에 쓰기모드로 작성하는 예는 다음과 같다.

```m
f = open("/home/ek3434/TIL/Python/새파일.txt","w")
for 변수 in range(1, 5):
    데이터 = "%d번째 줄입니다.\n" % 변수
    f.write(데이터)
f.close()
```

위의 예시를 아래의 예시와 비교해보자.

```
for 변수 in range(1, 5):
    데이터 = "%d번째 줄입니다.\n" % 변수
    print(data)
```

두 프로그램 예시의 차이점은 data를 출력하는 방법에 있다.

두 번째 방법인 print문은 모니터 화면에 출력하는 방법이고

첫번째 방법인 f.wirte문은 파일에 직접 결과값을 입력하는 방법이다.
f.write에서 f는 파일 객체명이다.

> readline()함수 이용하기.

```
f = open("/home/ek3434/TIL/Python/새파일.txt","r")
line = f.readline(20)
print(line)
f.close()
```

f.open("새파일.txt", 'r')로 파일을 읽기모드로 연후 readline을 이용하여 첫번째 줄을 읽어 출력한다.
여기서 line = f.readline()에서 ()안에 숫자를 입력하면 입력한 만큼의 문장을 출력한다.(list처럼)

- 모든 줄을 출력 하고싶을 경우

```
f = open("/home/ek3434/TIL/Python/새파일.txt","r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
```

while Ture:의 반복 루프안에서 더이상 읽어들일 f.readline()이 없으면 break되어 프로그램을 종료한다.

> readlines 함수

다른 방법은 realines 함수 사용 방법이다.

```
f = open("/home/ek3434/TIL/Python/새파일.txt","r")
line = f.readlines()
for 줄 in line:
    print(줄)
f.close()
```

readlines는 for문을 사용한다.
모든 줄을 각각 읽어서 각각의 줄을요소로 갖는 리스트로 되돌려주는 함수이다.

> read 함수 사용

또 다른 방법은 read함수 사용법이다.

```m
f = open("/home/ek3434/TIL/Python/새파일.txt","r")
데이터 = f.read()
print(데이터)
f.close
```

f.read()는 파일의 내용 전체를 문자열로 돌려서 출력해준다.

---

## 파일에 새로운 내용 추가.

쓰기모드 ('w')로 파일을 열면 이미 존재하는 파일을 열 경우에는 내용이 모두 사라진다.

그러나 추가모드('a')로 열면 새로운 값만 추가가 가능하다.

```m
f = open("/home/ek3434/TIL/Python/새파일.txt","a")
for 줄 in range(4,8):
    데이터 = "%d번째 추가한 줄입니다.\n"% 줄
    f.write(데이터)
f.close()
```

---

## With문 사용

```m
f = open("/home/ek3434/TIL/Python/새파일.txt",'w')
f.write("삶은 매우 짧다. 파이썬이 필요하다")
f.close()
```

파일을 열면 항상 닫아주는 것이 좋다.
하지만 파일을 열고 닫는 것을 자동으로 처리할 수 있는 명령문이 바로 with문이다.

```m
with open("/home/ek3434/TIL/Python/새파일.txt",'w') as f:
    f.write("with문 연습용 문장입니다.")
```

오픈 함수부분은 동일하다.
다만 변수 지정을 as f:로 선언하고 시작을 with로 하는 부분이 다르다.

아무튼 with문을 사용하면 with블록을 벗어난 순간 열린 파일 f가 자동으로 close 된다.
