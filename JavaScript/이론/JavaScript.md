# 자바 스크립트 (JavaScript)

객체 지향 프로그래밍 (OOP)에서 자주 사용되는 개념의 목록들은 다음과 같다.

- 객체와 메소드, 속성
- 클래스
- 캡슐화(Encapsulation)
- 집합(Aggregation)
- 재사용성(Reusability) / 상속(Inheritance)
- 다형성(Polymorphism)

## 객체

객체 지향이라는 이름에서 알 수 있듯이 객체가 중요하다. 객체란 사물(누군가 or 무언가)의 표현이며, 프로그래밍 언어의 도움으로 표현된다.

예를 들어 고양이 같은 공통 객체를 가정해 보면 서로 다른 색상, 이름, 무게 등의 특정 속성을 가지고 야옹거리기, 숨기, 잠자기 등과 같은 일부 동작을 수행할 수 있다.

OOP에서 객체의 특성을 `속성`이라고 하고 동작을 `메소드`라고 부른다.

그리고 보통

- 객체는 보통 책과 사람 같은 명사를 사용해 명명된다.
- 메소드는 읽기, 실행과 같은 동사이다.
- 속성의 값은 형용사다.

다음의 규칙들을 따른다.

예를 들어 '검은 고양이가 매트 위에서 잔다' -> 'The black cat sleeps on the mat'이라는 문장에서

'The cat'(명사)가 `객체`이고 'balck'(형용사)가 color를 나타내는 `속성`값이고 'sleep'(동사)가 OOP의 `동작`또는 `메소드`이다. 더 나아가 'on the mat'은 'sleep' 동작에 대해 뭔가 지정한다고 말할 수 있다. 따라서 sleep 메소드에 전달되는 `매개변수`로 동작한다.

그리고 객체의 다른이름은 `인스턴스(instance)`이다.

## 클래스

실생활에서는 유사한 대상을 몇 가지 기준에 따라 그룹화할 수 있다. 벌새와 독수리는 둘 다 새이므로 Birds 라는 클래스에 속하는 것으로 분류할 수 있다. 클래스는 객체의 청사진 또는 레시피다. 객체의 다른 이름은 인스턴스이다. 따라서 독수리가 일반적인 Birds 클래스의 하나의 구체적인 인스턴스라고 할 수 있다.

객체가 템플릿을 기반으로 하는 구체적인 인스턴스라면 클래스는 단순한 템플릿이므로 동일한 클래스를 사용하여 다른 객체를 생성할 수 있다.

자바스크립트에서 모든 것은 객체를 기반으로 한다. 자바스크립트는 객체이기도한 프로토타입 개념을 가진다.

## 캡슐화

캡슐화(encapsulation)은 객체 다음을 포함한다는 사실을 보여주는 다른 OOP(객체지향프로그래밍) 관련 개념이다.

- 데이터(속성에 저장됨)
- 데이터로 무엇인가를 수행하는 방법(메소드를 사용)

캡슐화와 함께 사용되는 또 다른 용어는 정보 숨기기다.

MP3를 예로 들어보자. MP3 플레이어와 같은 객체에서 객체의 사용자인 우리에게 버튼, 디스플레이 와 같이 작업할 수 있는 인터페이스를 사용한다. 기기 내부에서 어떻게 동작하는지는 알지 못하며, 대부분은 신경 쓸 필요가 없다. 즉, 인터페이스의 구현은 숨겨져있다. OOP에서 코드가 메소드를 호출하여 객체를 사용할 때도 마찬가지이다.
코드를 어떻게 짰던간에 매소드가 내부적으로 동작하는지 알 필요가 없다.

정보 숨기기의 다른 측면은 메소드와 속성의 가시성(visibillity)이다.

## 집합

여러 객체를 새로운 하나의 객체로 결합하는 것을 집합(aggregation) 또는 컴포지션(composition)이라고 한다. 문제를 더 작고 관리하기 쉬운 부분으로 나누는 방법이다. 문제 범위가 너무 복잡하여 전체를 세부적으로 생각할 수 없는 경우 , 문제를 여러 개의 작은 영역으로 분리하는 방법이라고 보면 된다.

PC를 예로 들면 PC는 복잡한 개체이나 Computer 객체를 구성하는 모든 객체를 각각 Monitor 객체, Mouse 객체, Keyboard 객체 등의 하위 객체로 나눠 자세히 살펴볼 수 있다.

다른 비유로는 Book 객체는 하나 이상의 Author 객체와 하나의 Publisher 객체, 여러 Chapter 객체와 하나의 TOC(Table of Contents = 목차)객체 등을 포함할 수 있다고 보면 된다.

## 상속

삭속(inheritance)은 기존 코드를 재사용하는 방법이다.

예를 들어, name과 birth와 같은 속성을 가지며, walk, talk, sleep, eat 기능을 구현하는 일반 객체인 Person을 갖고 있다고 가정하자. 그런 다음 Programmer라는 객체가 필요하다는 것을 알게 됐다고 해보자. Person 객체가 가지고 있는 모든 메소드와 속성을 다시 구현할 수는 있지만, Programmers 객체가 Person 객체를 상속받았다고 말하는 것이 더 현명한 방법이고 불필요한 작업을 줄일 수 있는 방법이다. 이렇게 하면 Programmers 객체는 Person 객체의 모든 기능을 재사용하고 추가로 필요로하는 특정 기능(= 메소드)만 구현하면 되는 것이다.

자바스크립트에는 클래스가 없으므로 객체는 다른 객체를 상속한다. -> ECMA6 표준부터는 추가됐다고 들었는데 확인 필요함.

객체가 다른 객체에서 상속받으면 일반적으로 상속된 메소드에 새로운 메소드를 추가해 이전 객체를 확장한다. 또한 상속된 객체는 하나 이상의 메소드를 선택하고 이를 재정의해서 필요에 맞게 사용자 정의하여 사용할 수 있다. 또한 새로운 객체에서 호출될 때 메소드가 다르게 동작하게 만들 수 도 있는데 이렇게 메소드의 동작을 재정의하는 방법을 `재정의`라고 한다.

## 다형성

앞의 예제에서 Programmer 객체는 부모의 Person 객체의 모든 메소드를 상속받았다. 그러므로 모두 talk라는 메소드를 제공한다고 볼 수 있다. 이제 코드 어딘가에 Bob이라는 변수가 있다고 가정할 때 Bob이 Person 객체인지 Programmers 객체인지는 모른다. Bob 객체에서 talk 메소드를 호출할 수 있으며 코드는 잘 작동할 것이다. 이렇게 서로 다른 객체에서 동일한 메소드를 호출하고 각각이 고유한 방식으로 응답하도록 하는 기능을 다형성(polymorphism)이라고 한다.

---

# 변수

변수는 데이터를 저장하는 데 사용된다. 변수는 구체적인 값을 위한 자리표시자(placeholder)이다. 예를 들어 프로그램 작성시 3.1415192653589793으로 쓸 바에 pi로 작성하는 것이 훨씬 간편하기 때문에 실제 데이터 대신 변수를 사용하는 것이 편리하다. 특히 프로그램내에서 여러번 사용되는 경우에는 더더욱 편리하다.

변수에 저장된 데이터는 처음 할당된 후 변경될 수 있으므로 이를 `변수(variable)`라고 부른다.

변수를 사용하려면 두 단계가 필요하다.

1. 변수의 선언
2. 변수의 초기화 -> 값을 부여

변수를 선언하려면 다음 코드와 같은 `var문`을 사용한다.

```
> var a;
undefined
> var thisIsVariable;
undefined
> var _and_this_too;
undefined
> var mix12three;
undefined
```

변수의 이름에는 문자와 숫자, 밑줄 문자 및 달러 기호의 조합등을 사용할 수 있다. 그러나 숫자로 시작할 수 는 없다.

다음과 같은 변수 선언은 유효하지 않는다.

```
> var 2three4five;
var 2three4five;
    ^

Uncaught SyntaxError: Invalid or unexpected token
```

이어서 변수를 초기화하려면 초기값을 지정해야 한다. 다음 두 가지 방법이 있다.

1. 변수를 먼저 선언하고, 초기화한다.
2. 단일 문으로 변수를 선언하면서 초기화한다.

2번의 경우의 예는 다음과 같다.

```
var a = 1;
```

이제 a라는 변수에는 값 1이 들어있다.

하나의 var문으로 여러 변수를 선언하고 선택적으로 초기화할 수 있다. 다음 코드와 같이 선언을 쉼표로 구분하면 된다.

```
var v1, v2, v3 = 'hello', v4 = 4, v5;
```

그러나 가독성을 위해 다음과 같이 한 줄에 하나의 변수만 사용해 작성하는 경우가 많다.

```
var v1,
    v2,
    v3 = 'hello',
    v4 = 4,
    v5;
```

> 변수의 대소문자

변수 이름은 대소문자를 구분한다. 다음의 예로 알아보자

```
> var case_matters = 'lower';
undefined
> var CASE_MATTERS  = 'upper';
undefined
> case_matters
'lower'
> CASE_MATTERS
'upper'
```

'>' 기호는 사용자가 입력한 코드를 보여준다. 콘솔에 출력된 결과를 의미한다.

```
콘솔에서 변수를 정의헀을때 출력값이 undefined로 출력됨을 알 수 있다. 이렇게 나오는 이유는 입력 값을 평가할 때 콘솔은 반환 값을 출력한다. var =1 과 같은 일부 표현식은 명시적으로 아무 것도 반환하지 않는다. 이 경우 암시적으로 특별 값인 `UNDEFINED`를 반환한다. 표현식이 어떤 값을 반환하면, 결과 값이 출력된다. 모든 콘솔이 undefined 값을 출력하지는 않는다.
```

# 연산자

연산자(Operator)는 하나 또는 두 개의 값을 받아 연산을 수행하고 값을 반환한다.

용어를 명확하게 이해하기 위해 간단한 예를 살펴보자

```
> 1+2;
3
```

- `+` 기호는 연산자다.
- 연산은 더하기다.
- 입력 값은 1과 2이다(피연산자(operand라고도 부른다)
- 결과 값은 3이다.
- 전체를 표현식(expression)이라고 부른다.

표현식에서 값 1, 2를 직접 사용하는 대신 변수를 사용할 수도 있다.

```
> var a = 1
undefined
> var b = 2;
undefined
> a + 1;
2
> b +2;
4
> a + b;
3
> var c = a + b;
undefined
> c;
3
```

기본 산술 연산자의 종류는 다음과 같다
|연산자 기호| 연산 | 예제 |
|:-----:|:------:|:-----------------------------------:|
|`+`|덧셈|>1+2; = 3|
|`-`|뺼셈|>99.99-11; = 88.99|
|`*`|곱셈|>2\*3; = 6|
|`/`|나눗셈|>6/4; = 1.5|
|`%`|모듈러(Modulo),나머지|>6%3; = 0 5%3; = 2 가끔은 숫자가 짝수인지 홀수인지 테스트하는 용도로도 사용한다.
|`++`|값을 1씩 증가| 후행 증가는 입력 값이 반환된 후 증가한다. 예를 들면 다음과 같다. var a =123; var b = a++ >b; = 123 >a; = 124 그러나 선행 증가는 반대다. 입력 값이 1만큼 증가된 후 반환된다. 예를 들면 다음과 같다. >var a = 123; >var b = ++a; >b = 124; >a; = 124|
|`--`|값을 1씩 감소|위으 값의 증가와 같이 후행 감소와 그 반대의 경우 2개로 나뉜다. 후행 감소의 경우 var a = 123; var b = a--; b; = 123 a; = 122의 형태이고 반대의 경우인 var a = 123; var b = --a; b; = 122 a; = 122의 값을 가진다.|

var a = 1;또한 연산자이다. 간단한 할당(assignment) 연산이며 =는 간단한 대입 연산자이다.

또한 대입 연산자와 산술 연산자의 조합인 연산자도 있다. 이것을 복합(compound) 연산자라고 한다.

```
> a +=3;
8
> a -=5
3
> a *=2;
6
> a /=5;
1.2
> a %= 2;
1.2
> a %= 1.2;
0
>
```

자바 스크립트는 항상 세미콜론으로 표현식을 끝낸다. 세미 콜론이 들어가지 않는다면 오류의 원인이 될 수 있으므로 항상 표현식을 종료하는 위치를 명시적으로 표기해야 한다.

---

# 원시 데이터 유형

1. 숫자(Number) : 부동 소수점 숫자와 정수를 포함한다. -1, 100, 3.14는 모두 숫자로 취급된다.
2. 문자열(string)임의의 개수의 문자로 구성된다. 예를 들어 a, one, one 2 three는 모두 문자열로 취급이다.
3. 부울(boolean) : true 또는 false가 될 수 있다.
4. 정의되지 않음(Undefined) : 존재하지 않는 변수에 접근하려고 할 때 특별한 값인 undefined를 받는다. 변수에 값을 할당하지 않고 선언할 때도 마찬가지이다.
5. Null : 하나의 값, 즉 null 값만 가질 수 있는 또 다른 특별한 데이터 유형이다.
   값이 없거나 빈 값임을 의미한다. 변수가 null값을 가지면 여전히 정의돼 있다는 것이다.

위의 5가지 원시 유형 중 어느 것에도 속하지 않는 값이 객체(object)이다. null또한 객체로 간주된다.

- 원시
- 비 원시

자바스크립트의 데이터 유형은 크게 이 2가지로 나뉜다고 보면 된다.

## typeof 연산자 (값 유형 찾기)

변수 또는 값의 유형을 알고 싶다면 특별한 typeof 연산자를 사용할 수 있다.
typeof 연산자를 사용했을 때 반환 값은 다음 중 하나이다.

- 숫자(number)
- 문자열(string)
- 부울(boolean)
- 정의되지 않음(undefined)
- 객체(object)
- 함수(function)

## 숫자

가장 간단한 숫자는 정수이다. 변수에 1을 대입하고 typeof 연산자를 사용하면 다음과 같이 number 문자열을 반환한다.

```
> var n = 1;
undefined
> typeof n;
'number'
> n = 2341;
2341
> typeof n;
'number'
```

위의 예제에서 두 번째로 변수의 값을 설정할 때에는 var문이 필요하지 않았다.

숫자에는 부동 소수점도 사용이 가능하다.

```
> var n2 = 1.23;
undefined
> typeof n2;
'number'
```

> 8진수와 16진수

숫자가 0으로 시작하면 8진수로 간주된다.

```
> var n3 = 0377;
undefined
> typeof n3;
'number'
> n3
255
```

예제에서 마지막 줄은 8진수 값을 10진수 표현으로 출력한다.
ES6는 접두사 0o를 제공하여 8진수를 나타낸다.

CSS에서는 색상을 정의하는 몇가지 옵션이 있다. CSS 스타일시트에서는 색상을 정의하는데 16진수 값을 사용하는데

- 10진수 값을 사용해 R,G,B의 양(0~255)를 지정한다. 예를 들어 RGB(0,0,0)은 검정이며 RGB(255,255,255)는 하얀색이다.
- 16진수를 사용하고 각 R,G,B 값에 대해 두 개의 문자를 지정한다. 예를 들어 #000000은 검은색, #ff0000은 빨간색이다. ff가 255의 16진수 값이기 때문이다.

자바스크립트에서 16진수 값 앞에는 0x를 넣을 수 있다.

```
> var n4 = 0x00;
undefined
> typeof n4
'number'
> n4;
0
> var n5 = 0xff;
undefined
> typeof
... n5
'number'
> n5
255
```

---

## 바이너리 리터럴

ES6에서는 0b(또는 0B) 프리픽스(prefix)를 사용해 다음과 같이 바이너리 정수를 나타낼 수 있다.

```
> console.log(0b111);
7
undefined
> console.log(0b1111);
15
undefined
```

## 지수 리터럴

le1(또는 le+1이나 1E1, 1E+1이라고도 쓴다)은 숫자 1뒤에 0이 오는것을 나타낸다. 즉 10이다.

유사하게 2E+3 숫자 2 뒤에 세 개의 0이 있음을 나타낸다. 즉 2000이다.

```
> 1e1;
10
> 1e+1;
10
> 1e+2;
100
> 2e+3;
2000
```

2e+3은 숫자 2의 오른쪽으로 소수점 3자리를 이동시키는 것을 의미한다. 반대로 2e-3도 있다.

## 무한대

자바스크립트에는 무한대(infinity)라는 특별한 값이 있다. 자바스크립트가 처리할 수 없는 너무 큰 숫자를 나타낸다.

```
> typeof Infinity
'number'
> Infinity;
Infinity
> 1e309;
Infinity
```

자바스크립트에서 처리할 수있는 가장 큰 수는 1.797631348623157e+308이고 가장 작은 수는 5e-324ㅇ이다.

그리고 0으로 나누면 무한대가 된다.

```
> var a = 6 /0 ;
undefined
> a
Infinity
```

Infinity가 가장 큰 숫자인데 가장 작은 숫자는 -Infinity와 같이 무한대 앞에 -기호를 붙이면 된다.

```
> var i = -Infinity;
undefined
> i
-Infinity
> typeof i
'number'
```

그리고 Infinity와 -Infinity를 합치면 0이 출력되는게 아닌 `NaN(Not a Number)`가 된다.

```
> Infinity - Infinity
NaN
> -Infinity + Infinity;
NaN
```

ES6에는 이 값이 Infinity인지 아닌지를 확인시켜주는 isFinite()메소드가 추가됐다.

## NaN

NaN은 그 이름에도 숫자이기도 한 특별한 값이다.

```mm
> typeof NaN;
'number'
```

그러나 숫자를 가정하고 연산을 수행하면 연산은 실패하고 NaN을 받는다. 예를 들어 10에 문자 'f'를 곱하려고 하면 'f'는 곱셉을 위한 유효한 피연산자가 아니기 때문에 결과는 NaN이 나온다.

```mm
> var a = 10 * 'f';
undefined
> a
NaN
```

NaN은 전염성이 있어 산술 연산에 NaN이 하나만 있어도 전체 결과는 NaN이 되버린다.

```
> 1+2+NaN;
NaN
```

> Number.isNaN

이 메소드는 값이 NaN인지 아닌지를 판별한다.

```mm
> console.log(Number.isNaN('test'));
false
undefined
> console.log(Number.isNaN(123));
false
undefined
> console.log(Number.isNaN(NaN));
true
undefined
> console.log(Number.isNaN(123/'ab'));
true
undefined
```

그러나 이건 값이 NaN인지 아닌지만 판단하기 때문에 숫자인지 아닌지 여부를 판단하는 데는 사용하기 힘들다.

그렇기 때문에 모질라에선 다음과 같이 폴리필(polyfill) 메소드를 제안한다고 한다.

```mm
> function isNumber(value) {
... return typeof value == 'number' && !Number.isNaN(value);
... }
```

> Number.isInteger

Number.isInteger는 Es6의 새로운 메소드이다. 숫자가 유한하고 소수점을 포함하지 않으면 True를 반환한다.

```mm
> console.log(Number.isInteger('test'));
false
undefined
> console.log(Number.isInteger(Infinity));
false
undefined
> console.log(Number.isInteger(NaN));
false
undefined
> console.log(Number.isInteger(123))
true
undefined
> console.log(Number.isInteger(1.23))
false
undefined
```

---

## 문자열

문자열은 텍스트를 나타내는 데 사용되는 일련의 문자다. 작은 따음표나 큰 따옴표 사이에 있는 값은 문자열로 간주된다. 즉 1은 숫자지만 '1' 은 문자열이 되는 것이다. 문자열과 함계 사용하면 typeof는 'string'문자열을 반환한다.

그리고 아무것도 입력하지 않은 경우에도 여전히 문자열(빈 문자열)이다.

```m
var s = ''; typeof s;
'string'
```

그리고 파이썬때와 마찬가지로 문자열 끼리 더하기 기호를 사용하면 문자열 연결(concatenation)연산이 된다. 두 문자열을 연결해 반환한다.

```m
> var s1 = 'web';
undefined
> var s2 = 'site';
undefined
> var s = s1 + s2;
undefined
> s
'website'
> typeof s;
'string'
```

문자열을 연결하려는 경우 모든 피연산자가 문자열인지 확인을 해야 한다.

## 문자열 변환

산술 연산의 피연산자에 '1'과 같이 숫자 같은 문자열을 사용하면, 백그라운드에서 문자열은 숫자로 변환된다.

```m
> var s = '1';
undefined
> s = 3* s;
3
> typeof s;
'number'
> var s = '1';
undefined
> s
'1'
> typeof s
'string'
> s++;
1
> typeof s;
'number'
```

이는 모호함 때문에 덧셈을 제외한 모든 산술 연산에 적용된다.

숫자 같은 문자열을 숫자로 변환하는 쉬운 방법은 1을 곱하는 것이다.

```m
> var s = '100'; typeof s;
'string'
> s = s * 1;
100
> typeof s;
'number'
```

그러나 반환이 실패하면 NaN을 받는다.

```m
> var movie = '101 dalma';
undefined
> movie * 1;
NaN
```

## 특수 문자열

> `\\`

`\\` 에서 `\`는 이스케이프 문자이다. 문자열 내에서 따옴표를 사용하려면 이스케이프 처리해서 자바스크립트가 문자열의 끝으로 처리하지 않도록 한다.

ex ) var s = 'i don\t know' : 자바스크립트는 i don만 문자열로 판단하고 나머지는 무효로 처리하기 때문에 오류다.
다음과 같은 형태는 유효하다.

```
> var s = 'i don\'t know';
undefined
> s
"i don't know"

> var s = "i don't know"
undefined
> s
"i don't know
```

> `\n`

줄의 끝을 의미한다.

```
> var a = '\n1\n2\n3';
>s;
'
1
2
3
'
```

> `\t`

탭을 의미한다.

```
var s = '1\t2';
>s;
'1 2'
```

---

## 문자열 템플릿 리터럴

ES6에서는 템플릿 리터럴을 도입했다. 템플릿 리터럴이란 표현식이 내장된 단일, 다중 행 문자열이다.

예를 들어

```m
> var log_level ='debug'
undefined
> var log_message = 'meltdown';
undefined
> console.log('Log level: ' + log_level + ' - message : ' + log_message);
Log level: debug - message : meltdown
```

위의 형태를 템플릿 리터럴을 사용하면 다음과 같이 수행할 수 있다.

```m
> console.log(`Log level: ${log_level} - message : ${log_message}`)
Log level: debug - message : meltdown
```

파이썬에서 format 사용했을 때와 유사하다.

템플릿 리터럴은 일반적인 큰 따옴표 또는 작은 따옴표 대신 백틱(back-tick) (``) 문자로 묶는다.

템플릿 리터럴 자리표시자는 달러 기호와 중괄호(${~~~~~~~})의 형태로 표시된다.

함수 호출을 내장시킬 수도 있다.

```m
> var a = 10;
undefined
> var b = 10;
undefined
> function sum(x,y){
... return x+y
... }
undefined
> function multi(x,y){
... return x*y
... }
undefined
> console.log(`Sum is ${sum(a,b)} and Multi would be ${multi(a,b)}.`);
Sum is 20 and Multi would be 100.
```

템플릿 리터럴은 여러줄 문자열 구문을 단순화 시킬 수 도 있다.

```m
> console.log("This is line one \n" + "and this is line two")
This is line one
and this is line two
```

```m
> console.log(`This is line one and this is line two`);
This is line one and this is line tw
```

또한 ES6에는` 태그된 템플릿 리터럴`이라는 흥미롱운 리터럴 유형이 있다.

함수를 사용하여 출력을 수정할 수 있다. 템플릿 리터럴에 표현식을 프리픽스로 사용하면 프리픽스는 호출할 함수로 간주된다.

---

# 부울

부울 데이터 유형에 속하는 값은 두 가지뿐이다.

```m
> var b= false
undefined
> typeof b
'boolean'

> var a = true;
undefined
> typeof a
'boolean'
```

true 또는 false에 따옴표를 사용하면 문자열이 된다.

```m
> var b = 'true';
undefined
> typeof b;
'string'
```

## 논리 연산자

부울 값을 사용하는 논리 연산자에는 다음과 같은 세 가지 연산자가 있다.

- ! - 논리 NOT(부정)
- && - 논리 AND
- || - 논리 OR

예제를 통해 더 살펴보자

not(!)의 사용법이다.

```m
> var b = !true;
undefined
> b
false
> var b = !!true;
undefined
> b
true
```

부울이 아닌 값에 논리 연산자를 사용하면 백그라운드에서 값이 다음과 같이 부울로 변한다.

```m
> var b = 'one';
undefined
> !b
false
```

문자열 'one'은 부울 true로 변화한 다음 부정되어 false로 출력된다.

```m
> var b = 'one';
undefined
> !!b
true
```

not(!)을 2번쓰면 다음과 같이 true로 출력됨을 알 수있다.

이렇게 임의의 값을 이중 부정을 상용해 부울 등식으로 변환할 수 있다.
false로 변환되는 다음을 제외하고는 대부분의 값은 true로 변환된다.

- 빈 문자열 ""
- null
- undefined
- 숫자 0
- 숫자 NaN
- 부울 false

위의 6개의 값은 false로 참조되지만 나머지는 모두 true로 변환된다.

그리고 논리 연산의 경우 !가 가장 높은 우선 순위를 가지며, 달리 괄호가 없다면 가장 먼저 계산된다. 그 다음 우선순위에 따라 &&와 ||가 계산된다.

## 지연 평가

여러 논리연산이 차례로 진행될 경우, 어느 시점이 되면 결과가 명확해지고 마지막 연산이 최종 결과에 영향을 미치지 않기 때문에 마지막 연산은 수행되지 않는다.

ex)

```
> true || true || ture || true || teur;
true
```

모두 or연산이고 피연산자 중 하나가 true이면 결과는 true가 되기 때문에 뒤의 어떤 값이 나오던 결과는 true로 고정된다. 따라서 자바스크립트 엔진은 지연 평가를 결정하고 최종 결과에 영향을 미치지 않는 코드를 평가하는 불필요한 작업을 피한다. 이 단락 동작은 다음 코드 블록과 콘솔에서 실험하여 확인할 수 있다.

```m
> var b = 5
undefined
> true || (b = 6);
true
> b
5
> true && (b = 6);
6
> b
6
```

위의 예제는 또 다른 흥미로운 동작을 보여준다. 자바스크립트가 논리 연산에서 피연산자로 부울이 아닌 표현식을 발견하면 결과로 부울이 아닌 값을 반환한다.

```m
> true || 'something';
true
> true && 'somthing';
'somthing'
> true && 'something' && true;
true
```

다음으로 변수에 변수가 정의돼 있으면 그 값이 유지되고 그렇지 않으면 값이 10으로 초기화 되는 형태이다.

```m
> var num = num || 10;
undefined
> num
10
```

그러나 이 형태는 num이 정의돼 있고 0 또는 6개의 false값 중 하나로 초기화되면, 코드가 예상대로 동작하지 않는다.

```m
> var num = 0;
undefined
> var num = num || 10;
undefined
> num
10
```

---

# 비교

비교 연산자에는 다양한 종류가 있다.

> `==`

동등 비교 연산자로 두 연산자가 같으면 true를 반환한다. 피연산자는 비교되기 전에 동일한 유형으로 변환된다. 느슨한 비교로 불린다.

```m
> 1 == 1;
true
> 1 == 2;
false
> 1 == '1';
true
```

> `===`

동등 및 유형 비교 연산자다. 두 연산자가 같고 동일한 유형이면 true를 반환한다. 엄격한 비교로 불린다.

```m
> 1 === '1';
false
> 1 === 1;
true
```

> `!=`

비 동등 비교이다. 서로 같지 않을 경우 true를 반환한다.

```m
> 1 != 1;
false
> 1 != '1';
false
> 1 != 2
true
```

> `!==`

유형 변환 없이 비동등 비교 연산자 이다. 피연산자가 같지 않거나 유형이 다른 경우 true를 반환한다.

```m
> 1 !==1;
false
> 1 !== '1';
true
```

> `>`

크기 비교 연산자 중 하나이다. 왼쪽 피연산자가 오른쪽보다 클 경우 true를 반환한다.

> `>=`

왼쪽 피연산자가 오른쪽 피연산자보다 크거나 같으면 true를 반환한다.

반대는 동일하다.

NaN의 경우 자기 자신을 포함한 그 어떠한 것과도 같지 않다.

```m
> NaN == NaN;
false
```

## Undefined와 Null

존재 하지 않는 변수를 사용하려고 할 경우 다음과 같은 오류가 발생한다.

```
> foo
Uncaught ReferenceError: foo is not defined
```

typeof 연산자를 사용하는 경우는 오류가 아니다. "undefined" 문자열이 반환된다.

```
> typeof foo;
'undefined'
```

변수에 값을 지정하지 않고 변수를 선언하는 경우도 오류가 아니다. 그러나 typeof는 여전히 "undefined"를 반환한다.

```
> var someavar;
undefined
> someavar
undefined
> typeof someavar
'undefined'
```

이것은 변수를 초기화하지 않고 선언할 경우 자바스크립트가 undefined로 변수를 자동으로 초기화 하기 때문이다.

반면 null 값은 자바스크립트가 백그라운드에서 할당하지 않는다.

```m
> var a = null;
undefined
> a
null
> typeof a;
'object'
```

null과 undefined의 차이는 작지만 경우에 따라 아주 중요할 수 있다.

```m
> var i = 1 + undefined;
undefined
> i
NaN
> var i = 1 + null;
undefined
> i
1
```

이는 null과 undefined가 다른 원시 유형으로 변환되기 때문이다.

- 숫자로 변환
  > 1 \* undefined = NaN
- NaN으로 변환
  > 1 \* null = 0
- 부울로 변환
  > !!undefined = false // !!null = false
- 문자열로 변환
  > "value : " + null; = "value: null"

## 심볼

ES6에는 심볼(symbol)이 도입되었다.

```m
> var atom = Symbol()
undefined
```

심볼을 생성할 때 new 연산자는 사용하지 않는다. new 연산자를 사용하면 오류가 발생하기 때문이다.

```m
> var atom = new symbol()
Uncaught ReferenceError: symbol is not defined
```

또한 symbol의 설명을 기술할 수도 있다.

```mm
> var atom = Symbol('atomic symbol')
> atom
Symbol(atomic symbol)
```

심볼을 설명하자면 심볼은 심볼들이 여기저기 흩어져 있는 큰 프로그램을 디버깅할 때 매우 편리하다.

Symbol의 가장 중요한 속성은 고유하고 불변이라는 점이다.

```mm
> console.log(Symbol() === Symbol())
false
undefined
> console.log(Symbol('atom') === Symbol('atom'))
false
undefined
```

심볼은 고유한 식별자가 필요한 곳에서 속성 키로 사용된다는 정도만 우선 이해하자.

## 원시 데이터 유형 요약

> 자바스크립트에는 다섯 가지 원시 데이터 유형이 있다.

- 숫자
- 문자열
- 부울
- Undefined
- Null

> 원시 데이터 유형이 아닌 것은 모두 객체이다.

- 원시 데이터 유형은 양수 및 음수의 정수, 부동 소수점, 16진수, 8진수, 지수, 특수문자 NaN, Infinity가 될 수 있다.

> 문자열 데이터 유형에는 따옴표로 묶인 문자가 표함된다. 템플릿 리터럴을 사용하는 경우 표현식을 포함시킬 수 있다.

> 부울 데이터 유형의 유일한 값은 true와 false이다.

> 널(Null) 데이터 유형의 유일한 값은 undefined이다.

> 다음의 6가지 false 값을 제외한 모든 값은 부울로 변환하면 true가 된다.

- " "
- null
- undefined
- 0
- NaN
- false

---

# 배열

배열은 단순히 값의 목록(시퀀스)일 뿐이다. 하나의 변수를 사용해 하나의 값을 저장하는 대신, 하나의 배열 변수를 사용하여 배열 요소에 여러 개의 값을 저장할 수 있다.

빈 배열을 포함하는 변수를 선언하려면 대괄호를 사용한다. 다음 코드에 표시된 것처럼 대괄호 사이에는 아무것도 없다.

그러나 세 개의 요소가 있는 배열을 정의하려면 다음과 같이 코드를 작성하면 배열의 내용이 담겨지고 출력된다.

```m
> var a = [];
undefined
> a
[]
> var a = [1,2,3];
undefined
> a
[ 1, 2, 3 ]
```

## 배열의 요소 추가 / 업데이트

인덱스를 사용해 배열 요소의 값을 업데이트할 수 있다.
a = [1,2]인 배열에 인덱스를 활용해 추가해보면

```m
> a[2] = 'three';
> a
[ 1, 2, 'three' ]
```

와 같은 형태로 추가된다.
새 요소를 추가했지만 배열에 간격을 두면 요소는 존재하지않으며 접근할 경우 undefined 값을 반환한다.

```
> var a =[1,2,3]
undefined
> a[6] = 'new';
'new'
> a
[ 1, 2, 3, <3 empty items>, 'new' ]
```

## 요소 삭제

요소를 삭제하려면 delete 연산자를 사용한다. 그러나 요소를 삭제한 후에도 배열의 길이는 변경되지 않는다. 이런 경우 배열에 구멍이 생길 수 있다.

```m
> var a = [1,2,3];
undefined
> delete a[1];
true
> a
[ 1, <1 empty item>, 3 ]
> typeof a[1];
'undefined'
> typeof a[0];
'number'
```

## 배열의 배열

배열은 다른 배열을 포함한 모든 유형의 값을 포함할 수 있다.

```m
> var a = [1, 'two', false, null, undefined];
undefined
> a
[ 1, 'two', false, null, undefined ]
> a[5] = [1,2,3];
[ 1, 2, 3 ]
> a
[ 1, 'two', false, null, undefined, [ 1, 2, 3 ] ]
```

- 배열은 데이터 저장소다.
- 배열은 인덱싱된 요소를 포함한다.
- 인덱스는 0부터 시작하여 각 요소에 대하여 1씩 증가한다.
- 배열 요소에 접근하려면 대괄호 안에 인덱스를 사용한다.
- 배열은 다른 배열을 포함한 모등 유형의 데이터를 포함할 수 있다.

---

# 조건과 루프

조건은 간단하지만 코드 실행 흐름을 제어하는 강력한 방법을 제공한다. 루프를 사용하면 적은 코드로 반복적 작업을 수행할 수 있다.

종류는 다음과 같다.

- if 조건
- switch 문
- whild, do ... while, for, for ... in 루프

## 코드 블록

코드 블록은 다음 예제 코드와 같이 중괄호로 묶인 0개 이상의 표현식으로 구성된다.

```m
 {
... var a = 1;
... var b = 3;
... }
```

블록은 무제한 중첩시킬 수 있다.

```m
{
    var a = 1;
    var b = 2;
    var c, d;
    {
        c = a+b;
        {
            d = a-b;
        }
    }
}
```

## if 조건

if 조건의 간단한 예로 어떠한 형태를 가지는지 알아보자

```m
> var result = '', a =3;
undefined
> if (a>2) {
... result = 'a is greater than 2';
... }
'a is greater than 2'
```

if 조건은 다음과 같이 구성된다.

- if 문
- 괄호 안의 조건
- 조건이 만족되면 실행되는 {}로 둘러싸인 코드 블록

조건(괄호 안의 부분)은 항상 부울 값을 반환하며 다음을 포함할 수 있다.

- 논리 연산, ! 또는 &&, ||
- ===, !=, >등의 비교
- 부울로 변환될 수 있는 모든 값 또는 변수
- 위의 조합

## else 절

if 조건에는 else 문을 선택적으로 사용할 수 있다. 조건이 false로 평가되면 실행되는 코드 블록이 온다.

```m
> if (a > 2) {
... result = 'a is greater than 2';
... } else {
... result = 'a is NOT greater tahn 2';
... }
'a is greater than 2'
```

if 문과 else문 사이에 else..if 조건은 무제한으로 올 수 있다.

```m
> if (a >2 || a < -2) {
... result = 'a is not between -2 and 2';
... } else if ( a === 0 && b === 0) {
... result = 'both a and b are zeros';
... } else if (a === b) {
... result = 'a and b are equal';
... } else {
... result = 'give up';
... }
'a is not between -2 and 2'
```

## 변수가 존재하는지 확인

변수가 존재하는지 확인할 필요가 있을 때가 종종 있다. 이를 수행하는 가장 쉬운 방법은 변수를 if문의 조건 부분에 넣는것이다. 그러나 가장 좋은 방법은 아니다. 변수가 존재하는지 테스트하는 예제를 살펴보자

```m
var result = '';
> if (asdfaf) {
... result = 'yes';
... }
Uncaught ReferenceError: asdfaf is not defined
> result;
''
```

코드의 최종 결과가 yes이기 때문에 분명히 동작한다. 하지만 첫째, 코드는 오류를 생성했다. asdfaf가 정의되지 않았고, 우리가 원하는 동작이 아니다.

둘째, if(asdfaf)가 false를 반환했다고 해서 asdfaf가 정의되지 않았음을 의미하지는 않는다. asdfaf가 정의되고 초기화됐지만 false 또는 0과 같은 값을 포함할 수 있다.

고로 변수가 정의돼 있는지 알아보는 더 좋은 방법은 typeof를 사용하는 것이다.

```m
> if (typeof somevar !== "undefined") {
... result = 'yes';
... }
undefined
> result
''
```

typeof 연산자는 항상 문자열을 반환하므로, 문자열 'undefined'와 비교할 수 있다. somevar 변수는 선언됐지만 아직 값이 할당되지 않았을 수도 있고 동일한 결과를 얻을 수 있다.

따라서 이와 같이 typeof로 테스트하면 ,실제로 변수가 undefined 값이 아닌 다른 값을 가지고 있는지를 테스트 하는 것이다.

````m
> var somevar;
undefined
> if (typeof somevar !== 'undefined') {
... result = 'yes';
... }
undefined
> result
''

> somevar = undefined
undefined
> if (typeof somevar !== 'undefined') {
... result = 'yes';
... }
undefined
> result
''

변수가 정의되지 않고 undefined가 아닌 다른 값으로 초기화 되었다면, 다음 예제와 같이 typeof에 의해 반환된 유형은 더 이상 'undefined'가 아니다.

```m
> somevar = 123;
123
> if (typeof somevar !== "undefined") {
... result = 'yes';
... }
'yes'
> result
'yes'
>
````

## 대체 if 구문

간단한 조건이 있을 때 if 구문을 사용할 수있다.

```m
> if (a === 1) {
... result = 'a is one';
... } else {
... result = 'a is not one';
... }
'a is one'
```

다음과 같이 작성도 가능하다.

```m
> var a = 1;
undefined
> var result = (a === 1) ? "a is one" :" ais not one";
undefined
> result
'a is one'
```

이 구문에서 변수 = 조건 ? a : b 형태로 되있는데 조건에 부합하여 true값이면 a를 아니면 b를 출력하는 양식이다.

간단한 조건에서만 사용해야 하는 구문이다.

숫자가 특정 범위, 50~ 100사이인지 확인한다고 가정해보자.

```m
> var a = 123;
undefined
> a = a > 100 ? 100 : a < 50 ? 50 : a;
100
```

`?:`는 세 개의 피연산자가 필요하기 때문에 삼항 연산자 라고도 불린다.

## 스위치

if 조건을 사용하고 너무 많은 else if 문을 사용한다면 if를 switch로 변경하는 것을 고려해 볼 수 있다.

```m
> var a = '1',
... result = '';
undefined
> switch (a) {
... case 1:
... result = 'Number 1';
... break;
... case '1':
... result = 'String 1';
... break;
... default:
... result = 'I don't know';
... break;
}
```

실행 결과는 'String 1'이다.

switch문의 전개 과정을 살펴보자

- 괄호 안의 표현식, 표현식은 보통 변수를 포함하지만, 값을 반환하는 어떤 것도 될 수 있다.
- 중괄호로 묶인 다수의 case 블록
- 각 case문 다음엔 표현식이 온다.표현식의 결과는 switch 문 다음에 나오는 표현식과 비교된다. 비교 결과가 true이면, case와 콜론 다음에 나오는 코드가 실행된다.
- case 블록의 끝을 알리는 break 문이 있다. 이 break문에 도달하면 switch문은 종료된다. 누락되 있을 경우에는 다음 case 블록으로 넘어간다.
- 코드 블록의 끝에 default 문으로 표시되는 선택적인 디폴트 case가 있다. 앞의 case중 하나도 true로 평가되지 않으면 이 defualt case가 실행된다.

단계별 절차로는 다음과 같다.

1. 괄호 안의 switch 표현식을 평가.
2. 첫 번째 case로 이동, 그 값을 1단계의 값과 비교
3. 2단계의 비교 결과가 true이면, case 블록의 코드를 실행한다.
4. case블록이 실행된 후, 끝에 break문이 있으면 switch를 벗어난다.
5. break가 없거나 2단계에서 false가 반환되면, 다음 case 블록으로 이동한다.
6. 2~5 단계를 반복한다.
7. 4단계에서 벗어나지 못하면, default 문의 코드를 실행한다.

---

# 루프

- while 루프
- do - while 루프
- for 루프
- for - in 루프

## while 루프

가장 단순한 유형의 반복이다. 형태는 다음과 같다.

```m
> var i = 0;
undefined
> while (i < 10) {
... i++;
... }
```

조건이 true로 평가되는한, 코드 블록은 계속해서 반복 실행 된다.

## Do - while 루프

do.. while 루프는 while 루프의 약간의 변형이다.

```m
> var i = 0;
undefined
> do {
... i ++;
... } while (i < 10);
```

do 문 다음에 코드 블록이 오고, 코드 블록 다음에 조건이 온다. 즉, 코드 블록은 조건이 평가되기 전에 항상 최소 한번 이상은 실행된다.

## for 루프

for 루프는 가장 널리 사용되는 루프 유형이다.

- 초기화 부분에서, 변수를 정의하거나 기존 변수의 초기값을 설정할 수 있다. 가장 자주 사용되는 변수는 i다.
- 조건 부분에서, i를 경계 값과 비교할 수 있다.
- 증가 부분에서 i++와 같이 i를 1씩 증가시킬 수 있다.

ex)

```m
var puni = ''
> for ( var i = 0; i < 100; i++) {
... puni += 'i will never do this again';
... }
```

그러나 다음과 같이 변수를 for 문 안에서 정해줄 수도 있다.

```m
> for ( var i = 0, puni = ''; i<100; i++){
... puni += 'i will never do this again';
... }
```

## for .. in 루프

for - in 루프는 배열, 객체의 요소를 반복하는데 사용된다. 이것이 유일한 용도여서 for나 while을 대체할 범용적 반복 메커니즘으로 사용할 수 없다.

## 주석

자바스크립트 프로그램 내에 주석을달 수 있다. 주석은 자바스크립트 엔진에 의해 무시되며 프로그램 동작 방식에 영향을 미치지 않는다. 그러나 코드를 다시 살펴보거나 유지보수를 위해 다른사람에게 코드를 전송하는 경우 아주 유용할 수 있다.

- 한줄 주석은 //로 시작하고 줄의 끝에서 끝난다.
- 여러줄 주석은 /_로 시작하고 _/로 끝나야 한다. 주석의 시작과 끝 사이의 모든 코드는 무시된다.

```m
// 줄의 시작

var a = 1; // 줄의 아무 곳이나

/* 한 줄로 작성된 여러 줄 주석 */

/*
여러줄 주석입니다.
으아아으아으어ㅓ으
*/
```

# 요약

자바스크립트의 원시 데이터 유형은

- 숫자
- 문자열
- 부울
- Undefined
- Null

값이 있는것을 기억하자.

그리고 연산자 또한 다음과 같은 종류가 있다.

- 산술 연산자 : + , -, \*, /, %
- 증가 연산자 : ++, --
- 할당 연산자 : =, +=, -=, \*=, /=, %=
- 특별 연산자 : typeof, delete
- 논리 연산자 : &&, ||, !
- 비교 연산자 : ==, ===, !=, !==, <, >, >=, <=
- 삼항 연산자 : ?

그리고 배열을 사용해 데이터를 저장, 접근하는 법, 조건문을 사용하는 방법, 루프사용하는 방법등을 정리했으니 복습할 때 이를 생각하면서 보도록 하자.
