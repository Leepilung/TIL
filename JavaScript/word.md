# 자바스크립트(Java Script) 단어장

> OOP(객체지향프로그래밍)

OOP란 객체지향 프로그래밍의 줄임말로 (Object Oriented Programming)이다. OOP에서 객체의 특성을 속성, 동작을 메소드라고 부른다.

> npm(Node packge manage)

노드 패키지 매니저. 수많은 패키지들이 공개되어 있다.# node에서 각종 패키지를 관리하고 설치, 삭제, 의존성 관리를 도와준다.

npm에 업로드된 노드 모듈을 패키지라고 부른다. 모듈이 다른 모듈을 사용할 수 있는 것처럼, 패키지도 다른 패키지를 사용할 수 있다. 이러한 관계를 의존 관계라고 한다.

> package.json

프로젝트를 진행하다보면 무수히 많은 패키지들을 추가하게 된다. 이러한 패키지들은 저마다 고유한 버전이 있으므로 이것들을 기록해둘 필요가 있다. 이때 설치한 패키지들을 관리하는 파일이 바로 package.json이다. 우리가 node로 프로젝트를 시작한다면 가장 먼저 만들어야 할 파일이 package.json이다. npm은 package.json을 만드는 명령어를 제공한다.

> 브라우저 벤더

브라우저 벤더란 브라우저를 만들거나 파는 회사들이다. 각 회사들이 브라우저 벤더들이다.

> 마일스톤(milestone)

마일스톤(milestone)이란 프로젝트 진행 과정에서 특정할 만한 건이나 표를 말한다. 예를 들어, 프로젝트 계약, 착수, 인력투입, 선금 수령, 중간보고, 감리, 종료, 잔금 수령 등 프로젝트 성공을 위해 반드시 거쳐야 하는 중요한 지점을 말한다.

> 트랜스파일러(Transpiler)

트랜스파일러는 같은 언어이지만, 문법적으로 변환해 주는 도구를 말합니다. 컴파일러는 머신언어로 변경해서 언어와 파일 자체가 변경되지만, 트랜스파일러는 같은 언어지만, 문법만 바꿔주는 역할을 해줍니다.

> 컴파일러(Compiler)

인간의 언어에 가까운 고급 언어로 작성된 원시 프로그램을 입력으로 받아 기계어로 된 목적 프로그램을 출력하기 위해 사용되는 언어 번역 프로그램.

> 명령줄 인터페이스(CLI)

CLI는 Command-Line Interface 또는 Command-Line user Interface 또는 Character User Interface 의 약자이다.

CLI는 윈도우에선 CMD, Powershell, 리눅스에선 Terminal(터미널)을 사용한다.

## Babel

Babel이란 주로 ECMAScript 2015+ 코드를 이전 JavaScript 엔진에서 실행할 수있는 이전 버전과 호환되는 JavaScript 버전으로 변환하는 데 사용되는 무료 오픈 소스 JavaScript 트랜스 컴파일러를 말한다.

Babel은 빌드 시스템, 프레임워크 및 언어에서부터 템플릿 엔진에 이르기까지 광범위하게 사용될 수 있으며,

좋은 명령줄(command line) 및 REPL(read - eval - print - loop)를 내장하고 있다.

> REPL(read - eval - print - loop)

REPL(Read Eval Print Loop)는 글자 그대로 읽고(read), 평가하고(eval), 출력하는(print) 반복(loop)을 의미

주로 CLI(쉘 or 콘솔이라 부름) 위에서 사용한다.

---

## 개발 의존성

> 의존성(Dependency)이란?

1. 코드에서 두 모듈 간의 연결.
2. 객체지향언어에서는 두 클래스 간의 관계라고도 말함.
3. 일반적으로 둘 중 하나가 다른 하나를 어떤 용도를 위해 사용함.

> 의존성(Dependency)이 위험한 이유

1. 하나의 모듈이 바뀌면 의존한 다른 모듈까지 변경이 이루어지기 때문.
2. 테스트 가능한 어플을 만들 때 의존성이 있으면 유닛테스트 작성이 어려움.
3. 유닛테스트의 목적 자체가 다른 모듈로부터 독립적으로 테스트하는 것을 요구하기 때문.



## 템플릿 리터럴(Template Literal)

템플릿 리터럴이란 자바스크립트에서 문자열을 입력하는 방식이다. 기존에는 var str = 'Hello ES6'와 같은 방식으로 사용하였으나 ES6에서는 백틱(back-tick)이라는 기호(`)를 사용하여 정의한다.

```mm
const str = `Hello ES6`;
```
위와 같이 백틱을 이용하게 되면 여러 줄에 걸쳐 문자열을 정의할 수도 있고, 자바스크립트의 변수를 문자열 안에 바로 연결할 수 있는 이점이 생긴다.


>여러 줄에 걸쳐 문자열 선언하기


기존 자바스크립트의 문자열 선언 방식인 작은 따옴표(')의 문제점은 아래와 같았다.
```m
var str = 'Template literals are string literals allowing embedded expressions. \n' + 
'You can use multi-line strings and string interpolation features with them. \n' + 
'They were called "template strings" in prior editions of the ES2015 specification.';
```
위와 같이 작은 따옴표를 이용하여 긴 문자열을 선언하게 되면 자동으로 개행이 되지 않기 때문에 라인 브레이커(line breaker)인 \n를 개행할 곳 중간 중간에 추가해야 했다. 

이렇게 되면 문장이 길면 길수록 +와 \n를 계속 추가해줘야 하는 번거로움이 생긴다.

그러나 백틱을 이용해서 문자열을 선언하게 되면 위와 같이 개행할 필요가 없다.
```mm
const str = `Template literals are string literals allowing embedded expressions.
You can use multi-line strings and string interpolation features with them.
They were called "template strings" in prior editions of the ES2015 specification.`;
```



## Raw strings (원래 문자열)
Raw string은 이스케이프 문자를 해석하지 않은 일반 문자열이다.

String.raw 태그함수를 사용하면 템플릿 문자열을 입력한 대로 출력할 수 있다.
```mm
let s = String.raw`xy\n${1+1}z`;
console.log(s);     //xy\n2z
```

태그 함수를 만들어 원래의 문자열을 반환하려면 첫 번째 인자의 raw 프로퍼티를 사용하면 된다.
```mm
let tag = function(strings) {
    return strings.raw[0];
}

let str = tag`Hello\nWorld.`;
console.log(str);       //Hello\nWorld.
```

---

## 조건문 3항 연산자 '`?`'

if, else와 다르게 3항연산자로 사용된다. 

이렇게도 사용된다.
```mm
var a = 123;
a = a > 100 ? 100 : a < 50 ? 50 : a;
```
조건식은 우선 a > 100이고 ? 뒤에서 100 : a는 각각 True일 때의 값과 False일 때의 값이다. 위의 식은 a가 100보다 작다면 false 식(a < 50)을 다시 판단하여 또다시 True(50)나 false(a)값을 반환한다고 보면 된다.