# 자바스크립트(JavaScript)란?

자바스크립트(JavaScript)는 객체(object) 기반의 스크립트 언어이다.

HTML로는 웹의 내용을 작성하고, CSS로는 웹을 디자인하며, 자바스크립트로는 웹의 동작을 구현한다.

자바스크립트는 주로 웹 브라우저에서 사용되나, Node.js와 같은 프레임워크를 사용하면 서버 측 프로그래밍에서도 사용할 수 있다.

현재 컴퓨터나 스마트폰 등에 포함된 대부분의 웹 브라우저에는 자바스크립트 인터프리터가 내장되어 있다.

역사에 대해서는 대충 넘어가도록 하자.

# 자바스크립트의 특징

자바스크립트가 가지고 있는 언어적 특징은 다음과 같다.

1. 자바스크립트는 객체 기반의 스크립트 언어
2. 자바스크립트는 동적이며, 타입을 명시할 필요가 없는 인터프리터 언어
3. 자바스크립트는 객체 지향형 프로그래밍과 함수형 프로그래밍을 모두 표현할 수 있다.

> 인터프리터 언어란?

C언어와 같은 언어는 소스 파일을 작성한 후, 해당 파일을 컴파일(compile)하여 사용자가 실행할 수 있는 실행 파일(.exe)로 만들어 사용한다.

하지만 인터프리터 언어는 이러한 컴파일 작업을 거치지 않고, 소스 코드를 바로 실행할 수 있는 언어를 의미한다.

자바스크립트는 웹 브라우저에 포함된 자바스크립트 인터프리터가 소스 코드를 직접 해석하여 바로 실행해준다.

# 자바와 자바스크립트

공부하기 전에도 해깔려 했듯이 자바와 자바스크립트는 그 이름만 놓고 보면 서로 관련이 있는 언어로 생각되기 쉽다.

그러나 두 언어는 서로 직접적인 관련은 없으며, 비슷한 점보다는 다른 점이 훨씬 많다.

문법상 비슷한 부분이 많다고 하는데 이는 두 언어의 문법이 모두 C언어를 기반으로 만들어졌기 때문이라고 한다.

- 자바
  컴파일 언어
  타입 검사를 엄격하게 함
  클래스(class) 기반의 객체 지향 언어

- 자바스크립트
  인터프리터 언어
  타입을 명시하지 않음
  프로토타입(prototype) 기반의 객체 지향 언어

# 자바스크립트 소개

자바스크립트를 사용하면 웹 프로그래밍에서 다음과 같은 일들이 가능하다.

- 자바스크립트는 HTML의 `'내용'`, `'속성'`, `'스타일'`을 변경할 수 있다.

# 자바스크립트 문법

> 프로그램(Program)이란 ?

프로그램은 컴퓨터가 실행할 수 있는 명령(instruction)으로 이루어진다.

컴퓨터 프로그래밍에서 컴퓨터가 실행할 수 있는 명령들을 실행문(statement)이라고 부른다.

즉, 프로그램이란 특정 결과를 얻기 위해서 컴퓨터에 의해 실행되는 실행문의 집합이라고 할 수 있다.

## 자바스크립트 문법

자바스크립트의 실행문은 세미콜론(;)으로 구분된다.

ex)

```js
var x = 10;

var result = x + 3;
```

또한 자바스크립트는 대소문자를 구분한다.

자바스크립트에서 변수나 함수의 이름, 예약어 등을 작성하거나 사용할 때에는 대소문자를 정확히 구분해서 사용해야 한다.

ex)

```js
var javascript = 10; // 변수 javascript와 JavaScript는 서로 다른 두 개의 변수로 인식됨.

var JavaScript = 20;

Var Script = 30; // 변수의 선언은 var 키워드로만 할 수 있으면 Var는 동작하지 않음.
```

# 리터럴(Literal)

리터럴은 직접 표현되는 값 그 자체를 의미한다.

리터럴의 종류는 다음 예제를 통해 알아보자.

ex)

```js
12; // 숫자 리터럴
("JavaScript"); // 문자열 리터럴
("안녕하세요"); // 문자열 리터럴
true; // 불리언 리터럴
```

# 식별자(identifier)

식별자는 변수나 함수의 이름을 작성할 때 사용하는 이름을 의미한다.

자바스크립트에서 식별자는 영문자(대소문자), 숫자, 언더스코어(\_) 또는 달러($)만을 사용할 수 있다.

> 기억해야할 포인트

- 자바스크립트에서 식별자는 숫자와 식별자의 구별을 빠르게 할 수 있도록 숫자로는 시작할 수 없다.

- 자바스크립트는 유니코드(unicode) 문자셋을 사용한다.

## 식별자 저장 방식

자바스크립트에서는 식별자를 작성할 때 다음과 같은 작성 방식을 사용할 수 있다.

1. Camal Case 방식

2. Underscore Case 방식

> Camal Case 방식

Camel Case 방식이란 식별자가 여러 단어로 이루어질 경우에 첫 번째 단어는 모두 소문자로 작성하고, 그다음 단어부터는 첫 문자만 대문자로 작성하는 방식이다.

> Underscore Case 방식

Underscore Case 방식은 식별자를 이루는 단어들을 소문자로만 작성하고, 그 단어들은 언더스코어(\_)로 연결하는 방식이다.

자바스크립트에서는 식별자를 작성할 때 관행적으로 Camal Case 방식을 많이 사용한다.

ex)

```js
var firstVar = 10;           // Camel Case 방식
function my_first_func {     // Underscore Case 방식
    var firstLocalVar = 20;  // Camel Case 방식
}
```

> 기억해야할 포인트

- 자바스크립트에서 하이픈(-)은 뺄셈을 위해 예약된 키워드이므로, 식별자를 작성할 때는 사용할 수 없다.

# 키워드

자바스크립트에서는 몇몇 단어들을 특별한 용도로 사용하기 위해 미리 예약하고 있다.

이렇게 미리 예약된 단어들을 키워드(keyword) 또는 예약어(reserved word)라고 한다.

이러한 키워드들은 프로그램 내에서 식별자로 사용할 수 없다.

ex)

```js
var firstVar = 10;      // var는 변수의 정의를 위해 예약된 키워드이다.
function myFirstFunc {  // function은 함수의 정의를 위해 예약된 키워드이다.

    var secondVar = 20; // var는 변수의 정의를 위해 예약된 키워드이다.
}
```

# 주석(comment)

주석(comment)이란 코드 내에 삽입된 일종의 설명문이다.

주석은 작성자나 다른 개발자가 나중에 코드를 수정할 때 참고할 수 있으며, 웹 페이지 개발 시 디버깅에도 사용된다.

이러한 주석은 자바스크립트 코드의 어느 부분에라도 작성할 수 있으며, 웹 브라우저의 동작에는 전혀 영향을 미치지 않는다.

자바스크립트 주석은 다음과 같은 두 가지 형식을 지원한다.

```js
1. 한 줄 주석 : // 주석문

2. 여러 줄 주석 : /* 주석문 */
```

ex)

```js
var x = 10;
// var y = 20; 한 줄의 주석문 : 이 부분은 실행되지 않는다.

/*
x = x + y;
여러 줄의 주석문 :
이 부분 또한 실행되지 않는다.
*/
document.getElementById("text").innerHTML = x;
```

다음은 자바스크립트에서 여러 줄 주석 안에 또 다른 주석을 삽입하는 예제이다.

ex)

```js
/* 여러 줄
    // 이렇게 두 줄 주석 안에 또 다른 한 줄 주석을 삽입할 수 있다.
주석 예제 . */
```

위의 예제처럼 자바스크립트에서는 여러 줄 주석 내부에 또 다른 한 줄 주석을 삽입할 수 있다.

하지만 여러 줄 주석 내부에 또 다른 여러 줄 주석을 삽입할 수는 없다.

ex)

```js
/* 여러 줄
    /* 또 다른 여러 줄 주석 예제 */
주석 예제. */
```

위의 예제처럼 여러 줄 주석 안에 또 다른 여러 줄 주석을 삽입하게 되면, 삽입한 주석의 종료를 알려주는 기호(_/)를 첫 번째 주석이 자신의 종료를 알려주는 기호(_/)로 인식하게 된다.

따라서 위의 예제에서 세 번째 라인은 주석으로 정상 인식되지 않으며, Uncaught SyntaxError가 발생하여 실행중이던 스크립트는 중지될 것이다.

그러므로 자바스크립트에서 여러 줄 주석은 절대로 중첩해서 사용해서는 안 된다.

# 자바스크립트 출력

자바스크립트는 여러 방법을 통해 결과물을 HTML 페이지에 출력할 수 있다. 그 방법에는 여러가지가 있는데 다음과 같다.

1. window.alert() 메소드

2. HTML DOM 요소를 이용한 innerHTML 프로퍼티

3. document.write() 메소드

4. console.log() 메소드

---

## windows.alert() 메소드

자바스크립트에서 가장 간단하게 데이터를 출력할 수 있는 방법은 window.alert() 메소드를 이용하는 것이다.

window.alert() 메소드는 브라우저와는 별도의 대화 상자를 띄워 사용자에게 데이터를 전달해준다.

ex)

```js
<script>
  function alertDialogBox(){" "}
  {alert("확인을 누를 때까지 다른 작업을 할 수 없다.")}
</script>
```

[실습링크]("http://tcpschool.com/examples/tryit/tryhtml.php?filename=js_intro_output_01")

- window 객체의 모든 메소드나 프로퍼티를 사용할 때는 window라는 접두사를 생략할 수 있다.

## HTML DOM 요소를 이용한 innerHTML 프로퍼티

실제 자바스크립트 코드에서 출력을 위해 가장 많이 사용되는 방법은 HTML DOM 요소를 이용한 innerHTML 프로퍼티를 이용하는 방법이다.

우선 document 객체의 getElementByID()나 getElementsByTagName() 등의 메소드를 사용하여 HTML 요소를 선택한다.

그리고서 innerHTML 프로퍼티를 이용하면 선택된 HTML 요소의 내용(content)이나 속성(attribute)값 등을 손쉽게 변경할 수 있다.

ex)

```js
<script>
  var str = document.getElementById("text"); str.innerHTML = "이 문장으로
  바뀌었습니다!";
</script>
```

[실습링크]("http://tcpschool.com/examples/tryit/tryhtml.php?filename=js_intro_output_02")

---

## document.write() 메소드

document.write() 메소드는 웹 페이지가 로딩될 때 실행되면, 웹 페이지에 가장 먼저 데이터를 출력한다.

따라서 document.write() 메소드는 대부분 테스트나 디버깅을 위해 사용된다.

ex)

```js
<script>document.write(4 * 5);</script>
```

실습링크 : http://tcpschool.com/examples/tryit/tryhtml.php?filename=js_intro_output_03

하지만 웹 페이지의 모든 내용이 로딩된 후에 document.write() 메소드가 실행되면, 웹 페이지 내에 먼저 로딩된 모든 데이터를 지우고 자신의 데이터를 출력하게 된다.

따라서 document.write() 메소드를 테스트 이외의 용도로 사용할 때에는 충분히 주의해서 사용해야 한다.

ex)

```js
<button onclick="document.write(4 * 5)">버튼을 눌러보세요!</button>
```

[실습 링크]("http://tcpschool.com/examples/tryit/tryhtml.php?filename=js_intro_output_04")

---

## console.log()메소드

console.log() 메소드는 웹 브라우저의 콘솔을 통해 데이터를 출력하거나 IDE의 터미널에 출력하기도 한다.

대부분의 주요 웹 브라우저에서는 F12를 누른 후, 메뉴에서 콘솔을 클릭하면 콘솔 화면을 사용할 수 있다.

이러한 콘솔 화면을 통한 데이터의 출력은 좀 더 자세한 사항까지 출력되므로, 디버깅하는데 많은 도움을 준다.

ex)

```js
<p>F12를 눌러서 콘솔 화면을 열면 결과를 확인할 수 있습니다.</p>

<script>
    console.log(4 * 5);
</script>
```

실습링크 : http://tcpschool.com/examples/tryit/tryhtml.php?filename=js_intro_output_05

# 자바스크립트 적용

HTML 문서에 자바스크립트 코드를 적용하는 방법에는 다음과 같은 방법이 있다.

1. 내부 자바스크립트 코드로 적용
2. 외부 자바스크립트 파일로 적용

## 내부 자바스크립트 코드

자바스크립트 코드는 `<script>`태그를 사용하여 HTML 문서 안에 삽입할 수 있다.

```html
<!-- 문법 -->
<script>
  document.getElementById("text").innerHTML = "여러분을 환영합니다!";
</script>
```

이렇게 삽입된 자바스크립트 코드는 HTML 문서의 `<head>`태그나 `<body>`태그, 또는 양쪽 모두에 위치할 수 있다.

다음 예제는 HTML 문서의 <head>태그에 자바스크립트 코드를 삽입한 예제이다.

```js
<head>
    <meta charset="UTF-8">
    <title>JavaScript Apply</title>
    <script>
        function printDate() {
            document.getElementById("date").innerHTML = Date();
        }
    </script>
</head>
```

[실습링크]("http://tcpschool.com/examples/tryit/tryhtml.php?filename=js_intro_apply_01")

자바스크립트 코드를 <head>태그에 삽입하나 <body>태그에 삽입하나 동작상의 차이는 없다.

```js
<body>
    <p>자바스크립트를 이용하면 현재 날짜와 시간 정보에도 손쉽게 접근할 수 있어요!</p>
    <button onclick="printDate()">현재 날짜와 시간 표시하기!</button>
    <p id="date"></p>
    <script>
        function printDate() {
            document.getElementById("date").innerHTML = Date();
        }
    </script>
</body>
```

## 외부 자바스크립트 파일

자바스크립트 코드는 HTML 문서의 내부뿐만 아니라 외부 파일로 생성하여 삽입할 수도 있다.

외부에 작성된 자바스크립트 파일은 .js 확장자를 사용하여 저장한다.

해당 자바스크립트 파일을 적용하고 싶은 모든 웹 페이지에 `<script>`태그를 사용해 외부 자바스크립트 파일을 포함하면 된다.

```js
// example.js 라는 파일이라고 가정
function printDate() {
  document.getElementById("date").innerHTML = Date();
}
```

ex)

```html
<head>
  <meta charset="UTF-8" />
  <title>JavaScript Apply</title>
  <script src="/examples/media/example.js"></script>
</head>
```

[실습링크]("http://tcpschool.com/examples/tryit/tryhtml.php?filename=js_intro_apply_03")

외부 자바스크립트 파일을 사용하면 웹의 내용을 담당하는 HTML 코드로부터 웹의 동작을 구현하는 자바스크립트 코드를 분리할 수 있다.

이렇게 하면 HTML 코드와 자바스크립트 코드를 각각 읽기도 편해지고, 유지 보수도 쉬워진다.

또한, 외부 자바스크립트 파일은 웹 브라우저가 미리 읽어 올 수 있어 웹 페이지의 로딩 속도 또한 빨라지는 장점이 있다.

# 자바스크립트의 기본 타입

타입(data type)이란 프로그램에서 다룰 수 있는 값의 종류를 의미한다.

자바스크립트에서는 여러 가지 형태의 타입을 미리 정의하여 제공하고 있으며, 이것을 기본 타입이라고 정의한다.

자바스크립트의 기본 타입은 크게 `원시 타입`과 `객체 타입`으로 구분할 수 있다.

> 원시 타입

1. 숫자(number)
2. 문자열(string)
3. 불리언(boolean)
4. 심볼(symbol) : ECMAScript 6부터 제공됨
5. undefined

> 객체 타입

6. 객체(object)

EX )

```js
var num = 10; // 숫자
var myName = "홍길동"; // 문자열
var str; // undefined
```

# 숫자(number)

자바스크립트는 다른 언어와는 달리 정수와 실수를 따로 구분하지 않고, 모든 수를 실수 하나로만 표현한다.

또한, 매우 큰 수나 매우 작은 수를 표현할 경우에는 e 표기법을 사용할 수 있다.

EX )

```js
var firstNum = 10; // 소수점을 사용하지 않은 표현
var secondNum = 10.0; // 소수점을 사용한 표현
var thirdNum = 10e6; // 10000000
var fourthNum = 10e-6; // 0.00001
```

# 문자열(string)

자바스크립트에서 문자열은 큰따옴표("")나 작은따옴표('')로 둘러싸인 문자의 집합을 의미한다.

큰따옴표는 작은따옴표로 둘러싸인 문자열에만 포함될 수 있으며, 작은따옴표는 큰따옴표로 둘러싸인 문자열에만 포함될 수 있다.

EX )

```js
var firstStr = "이것도 문자열."; // 큰따옴표를 사용한 문자열
var secondStr = "이것도 문자열."; // 작은따옴표를 사용한 문자열
var thirdStr = "나의 이름은 '김아무개'다."; // 작은따옴표는 큰따옴표로 둘러싸인 문자열에만 포함될 수 있음.
var fourthStr = '나의 이름은 "김가무개"다.'; // 큰따옴표는 작은따옴표로 둘러싸인 문자열에만 포함될 수 있음.
```

자바스크립트에서는 숫자와 문자열을 더할 수도 있다.

이럴 경우에 자바스크립트는 숫자를 문자열로 자동 변환하여, 두 문자열을 연결하는 연산을 수행한다.

EX )

```JS
var num = 10;
var str = "JavaScript";
document.getElementById("result").innerHTML = (num + str); // 10JavaScript
```

[실습링크](http://tcpschool.com/examples/tryit/tryhtml.php?filename=js_datatype_basic_03)

# 불리언(Boolean)

불리언 값은 참(true)과 거짓(false)을 표현한다.

자바스크립트에서 불리언 값은 예약어인 true와 false를 사용하여 나타낼 수 있다.

EX)

```JS
var firstNum = 10;
var secondNum = 11;
document.getElementById("result").innerHTML = (firstNum == secondNum); // false
```

[실습링크](http://tcpschool.com/examples/tryit/tryhtml.php?filename=js_datatype_basic_04)

# 심볼(symbol)

심볼 타입은 ECMAScript 6부터 새롭게 추가된 타입이다.

심볼은 유일하고 변경할 수 없는 타입으로, 객체의 프로퍼티를 위한 식별자로 사용할 수 있다.

EX )

```JS
var sym = Symbol("javascript");  // symbol 타입
var symObj = Object(sym);        // object 타입
```

[실습링크](http://tcpschool.com/examples/tryit/tryhtml.php?filename=js_datatype_basic_05)

- 심볼은 여전히 잘 이해가 안가는 파트. + 심볼 타입은 익스플로러에선 지원하지 않는다.

# typeof 연산자

typeof 연산자는 피연산자의 타입을 반환하는 피연산자가 단 하나뿐인 연산자이다.

EX)

```JS
typeof 10;        // number 타입
typeof "문자열";  // string 타입
typeof true;      // boolean 타입
typeof undefined; // undefined 타입
typeof null;      // object 타입
```

# null과 undefined

자바스크립트에서 null이란 object 타입이며, 아직 '값'이 정해지지 않은 것을 의미한다.

또한, undefined란 null과는 달리 '타입'이 정해지지 않은 것을 의미한다.

따라서 자바스크립트에서 undefined는 초기화되지 않은 변수나 존재하지 않는 값에 접근할 때 반환된다.

EX )

```js
var num; // 초기화하지 않았으므로 undefined 값을 반환함.
var str = null; // object 타입의 null 값
typeof secondNum; // 정의되지 않은 변수에 접근하면 undefined 값을 반환함.
```

null과 undefined는 동등 연산자(==)와 일치 연산자(===)로 비교할 때 그 결괏값이 다르므로 주의해야 한다.

null과 undefined는 타입을 제외하면 같은 의미지만, 타입이 다르므로 일치하지는 않는다.

EX )

```js
null == undefined; // true
null === undefined; // false
```

# 객체(object)

자바스크립트의 기본 타입은 객체(object)이다.

객체(object)란 실생활에서 우리가 인식할 수 있는 사물로 이해할 수 있다.

객체는 여러 프로퍼티(property)나 메소드(method)를 같은 이름으로 묶어놓은 일종의 집합체라고 보면 편하다.

EX )

```js
var dog = { name: "해피", age: 3 }; // 객체의 생성

// 객체의 프로퍼티 참조
document.getElementById("result").innerHTML =
  "강아지의 이름은 " + dog.name + "이고, 나이는 " + dog.age + "살 입니다.";
```

# 타입 변환

자바스크립트는 타입 검사가 매우 유연한 언어이다.

자바스크립트의 변수는 타입이 정해져 있지 않으며, 같은 변수에 다른 타입의 값을 다시 대입할 수도 있다.

EX )

```js
var num = 20; // Number 타입의 20
num = "이십"; // String 타입의 "이십"
var num; // 한 변수에 여러 번 대입할 수는 있지만, 변수의 재선언은 할 수 없다. 재선언문은 무시된다.
```

# 묵시적 타입 변환(implicit type conversion)

자바스크립트는 특정 타입의 값을 기대하는 곳에 다른 타입의 값이 오면, 자동으로 타입을 변환하여 사용한다.

즉, 문자열 값이 오길 기대하는 곳에 숫자가 오더라도 자바스크립트는 알아서 숫자를 문자열로 변환하여 사용한다는 의미이다.

EX )

```js
10 + "문자열"; // 문자열 연결을 위해 숫자 10이 문자열로 변환됨.
"3" * "5"; // 곱셈 연산을 위해 두 문자열이 모두 숫자로 변환됨.
1 - "문자열"; // NaN
```

위의 세 번째 예제에서 뺄셈 연산을 위해 문자열이 숫자로 변환되어야 하나, 해당 문자열은 두 번째 예제의 문자열과는 달리 숫자로 변환될 수 없는 문자열이다.

따라서 의미에 맞게 자동으로 타입을 변환할 수 없으므로, 자바스크립트는 NaN 값을 반환한다.

> NaN이란?

```
NaN은 Not a Number의 축약형으로, 정의되지 않은 값이나 표현할 수 없는 값이라는 의미를 가진다.

이러한 NaN은 Number 타입의 값으로 0을 0으로 나누거나, 숫자로 변환할 수 없는 피연산자로 산술 연산을 시도하는 경우에 반환되는 읽기 전용 값을 의미한다.
```

# 명시적 타입 변환(explicit type conversion)

자바스크립트에서는 묵시적 타입 변환을 많이 사용하지만, 명시적으로 타입을 변환할 방법도 제공한다.

명시적 타입 변환을 위해 자바스크립트가 제공하는 전역 함수는 다음과 같다.

1. Number()
2. String()
3. Boolean()
4. Object()
5. parseInt()
6. parseFloat()

EX )

```js
Number("10"); // 숫자 10
String(true); // 문자열 "true"
Boolean(0); // 불리언 false -> 1은 True
Object(3); // new Number(3)와 동일한 결과로 숫자 3
```

# 숫자를 문자열로 변환

숫자를 문자열로 변환하는 가장 간단한 방법은 String() 함수를 사용하는 것이다.

null과 undefined를 제외한 모든 타입의 값이 가지고 있는 toString() 메소드를 사용할 수도 있다.

숫자(Number) 객체는 숫자를 문자열로 변환하는 다음과 같은 메소드를 별도로 제공한다.

1. toExponential()
2. toFixed()
3. toPrecision()

|     메소드      |                                            설명                                            |
| :-------------: | :----------------------------------------------------------------------------------------: |
| toExponential() | 정수 부분은 1자리, 소수 부분은 입력받은 수만큼 e 표기법을 사용하여 숫자를 문자열로 변환함. |
|    toFixed()    |                소수 부분을 입력받은 수만큼 사용하여 숫자를 문자열로 변환함.                |
|  toPrecision()  |               입력받은 수만큼 유효 자릿수를 사용하여 숫자를 문자열로 변환함.               |

`메소드(method)`란 객체의 프로퍼티 값으로 함수를 갖는 프로퍼티를 의미한다.

지금 해당 개념에 대해가지치기를 하다보면 밑도끝도 없어지니 나중에 자세히 다뤄보자.

# 불리언 값을 문자열로 변환

불리언 값을 문자열로 변환하는 방법에는 String() 함수와 toString() 메소드를 사용하는 방법이 있다.

EX )

```js
String(true); // 문자열 "true"
false.toString(); // 문자열 "false"
```

# 날짜를 문자열이나 숫자로 변환

날짜를 문자열로 변환하는 방법에는 String() 함수와 toString() 메소드를 사용하는 방법이 있다.

자바스크립트에서 날짜(Date) 객체는 문자열과 숫자로 모두 변환할 수 있는 유일한 타입이다.

날짜(Date) 객체는 날짜를 숫자로 변환하는 다음과 같은 메소드를 별도로 제공한다.

1. getDate()
2. getDay()
3. getFullYear()
4. getMonth()
5. getTime()
6. getHours()
7. getMinutes()
8. getSeconds()
9. getMilliseconds()

|      메소드       |                                      설명                                      |
| :---------------: | :----------------------------------------------------------------------------: |
|     getDate()     |                     날짜 중 일자를 숫자로 반환함. (1 ~ 31)                     |
|     getDay()      |            날짜 중 요일을 숫자로 반환함. (일요일 : 0 ~ 토요일 : 6)             |
|   getFullYear()   |                  날짜 중 연도를 4자리 숫자로 반환함. (yyyy년)                  |
|    getMonth()     |               날짜 중 월을 숫자로 반환함. (1월 : 0 ~ 12월 : 11)                |
|     getTime()     | 1970년 1월 1일부터 현재까지의 시간을 밀리초(millisecond) 단위의 숫자로 반환함. |
|    getHours()     |                      시간 중 시를 숫자로 반환함. (0 ~ 23)                      |
|   getMinutes()    |                      시간 중 분을 숫자로 반환함. (0 ~ 59)                      |
|   getSeconds()    |                      시간 중 초를 숫자로 반환함. (0 ~ 59)                      |
| getMilliseconds() |        시간 중 초를 밀리초(millisecond) 단위의 숫자로 반환함. (0 ~ 999)        |

EX )

```js
String(Date()); // Mon May 16 2016 19:35:25 GMT+0900
Date().toString(); // Mon May 16 2016 19:35:25 GMT+0900
var date = new Date(); // Date 객체 생성
date.getFullYear(); // 2016
date.getTime(); // 1463394925632 -> 1970년 1월 1일부터 현재까지의 시간을 밀리초 단위의 숫자로 반환함.
```

# 문자열을 숫자로 변환

문자열을 숫자로 변환하는 가장 간단한 방법은 Number() 함수를 사용하는 것이다.

자바스크립트는 문자열을 숫자로 변환해 주는 두 개의 전역 함수를 별도로 제공한다.

1. parseInt()
2. parseFloat()

|     함수     |                     설명                     |
| :----------: | :------------------------------------------: |
|  parseInt()  | 문자열을 파싱하여 특정 진법의 정수를 반환함. |
| parseFloat() |  문자열을 파싱하여 부동 소수점 수를 반환함.  |

# 불리언 값을 숫자로 변환

불리언 값을 숫자로 변환하는 방법에는 Number() 함수를 사용하는 방법이 있다.

EX )

```js
Number(true); // 숫자 1
Number(false); // 숫자 0
```
