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

> 여러 줄에 걸쳐 문자열 선언하기

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

# 구조화 = 비구조화 할당(Destructuring Assignment)

`비구조화 할당(Destructuring Assignment)`이란 배열이나 객체의 속성을 해체하여 그 값을 개별 변수에 담을 수 있게 하는 자바스크립트 표현식이다.

> 기본 문법(배열)

```mm
const animalList = ["CAT", "DOG", "TIGER"];
const cat = animalList[0];
const dog = animalList[1];
const tiger = animalList[2];
console.log(cat); // CAT
console.log(dog); // DOG
console.log(tiger); // TIGER
```

animalList는 "CAT", "DOG", "TIGER" 값을 가지고 있는 배열이다. 이 배열의 값을 각각 변수에 할당 하려면 위처럼 각각 하나씩 지정해 줘야 한다. 번거로운 작업이며, 코드도 복잡해보이는 단점이 있다.

```mm
const [cat, dog, tiger] = ["CAT", "DOG", "TIGER"];
console.log(cat); // CAT
console.log(dog); // DOG
console.log(tiger); // TIGER
```

비구조화 할당을 이용하면 위처럼 간단하게 작성할 수 있다. 좌항이 호출될 변수명 집합, 우항이 할당할 값이다. 좌항의 각 요소에는 같은 index를 가지는 배열값이 할당된다.

> 나머지 패턴

```mm
const [cat, ...rest] = ["CAT", "DOG", "TIGER"];
console.log(cat); // CAT
console.log(rest); // ["DOG", "TIGER"]
```

전개 연산자(...)를 활용하면 좌항에서 명시적으로 할당되지 않는 나머지 배열 값을 사용할 수 있다.

> 기본 문법(객체)

```mm
const animals = {
  cat: "CAT",
  dog: "DOG",
  tiger: "TIGER"
};
const cat = animals.cat;
const dog = animals.dog;
const tiger = animals.tiger;
console.log(cat); // CAT
console.log(dog); // DOG
console.log(tiger); // TIGER
```

객체도 배열과 마찬가지로 일일히 값을 따로 넣어주려면 번거롭다.

```mm
const { cat, dog, tiger } = {
  cat: "CAT",
  dog: "DOG",
  tiger: "TIGER"
};
console.log(cat); // CAT
console.log(dog); // DOG
console.log(tiger); // TIGER
```

> 나머지 패턴

```mm
const { cat, ...rest } = {
  cat: "CAT",
  dog: "DOG",
  tiger: "TIGER"
}
console.log(cat); // CAT
console.log(rest); // {dog: "DOG", tiger: "TIGER"}
```

배열과 마찬가지로 객체도 나머지 패턴이 있다.

> 기본 key값 대신 다른 변수명 사용

```mm
const { cat: catName, dog: dogName, ...rest } = {
  cat: "CAT",
  dog: "DOG",
  tiger: "TIGER",
  monkey: "MONKEY"
}
console.log(catName); // CAT
console.log(dogName); // DOG
console.log(rest); // {tiger: "TIGER", monkey: "MONKEY"}
```

좌항의 변수에 다른이름으로 사용할 변수명을 우항에 대입하면 되며, 나머지 값을 뜻하하는 전개 연산자(...)는 우항의 key에 영향을 받지 않으므로 ...rest: restName와 같은 표현식은 무의미 하며 에러가 난다.

> 우항의 key 값이 변수명으로 사용 불가인 경우

```mm
const { 'cat-name', 'dog name' } = {
  'cat-name': "CAT",
  'dog name': "DOG"
}
// error
```

좌항으로 전달 받는 key 값이 `cat-name`같이 사용 불가능한 문자열이 있는 경우 에러를 호출한다. 이럴 경우는 아래와 같은 방식으로 비구조화 할 수 있다.

```mm
const key = 'dog name';
const { 'cat-name': cat_name, [key]: dog_name } = {
  'cat-name': "CAT",
  'dog name': "DOG"
}
console.log(cat_name); // CAT
console.log(dog_name); // DOG
```

다만 이 경우 'cat-name'과 매칭할 변수명 cat_name을 작성하지 않으면 에러가 발생한다.

## 기본값 할당

> 배열의 기본값 할당

```mm
const [cat, dog, tiger] = ["CAT", "DOG"];
console.log(cat); // CAT
console.log(dog); // DOG
console.log(tiger); // undefined
```

비구조화의 범위를 벗어나는 값 할당을 시도하면 undefined를 반환한다. 이럴 경우를 방지하기 위해 아래처럼 호출될 변수명에 기본값을 할당할 수 있다.

```mm
const [cat, dog, tiger = "TIGER"] = ["CAT", "DOG"];
console.log(cat); // CAT
console.log(dog); // DOG
console.log(tiger); // TIGER
```

비구조화의 범위를 벗어나는 값 할당을 시도하면 undefined를 반환한다. 이럴 경우를 방지하기 위해 아래처럼 호출될 변수명에 기본값을 할당할 수 있다.

```mm
const [cat, dog, tiger = "TIGER"] = ["CAT", "DOG"];
console.log(cat); // CAT
console.log(dog); // DOG
console.log(tiger); // TIGER
```

> 객체의 기본값 할당

```mm
const { cat, dog, tiger = "TIGER" } = {
  cat: "CAT",
  dog: "DOG"
};
console.log(cat); // CAT
console.log(dog); // DOG
console.log(tiger); // TIGER
```

배열과 마찬가지로 객체도 기본값을 지원한다.

```mm
const { monkey: monkey_name = 'MONKEY' } = {};
console.log(monkey_name); // MONKEY
```

위 코드처럼 객체의 key에 새로운 변수명을 할당하는 방식에도 기본 기본값 할당을 사용할 수 있다.

## 복사

전개 연산자를 사용하여 배열, 객체의 깊은 복사를 할 수 있다.

> 배열의 깊은 복사

```mm
let arr = [1, 2, 3];
let copy1 = arr;
let [...copy2] = arr;
let copy3 = [...arr];

arr[0] = 'String';
console.log(arr); // [ 'String', 2, 3 ]
console.log(copy1); // [ 'String', 2, 3 ]
console.log(copy2); // [ 1, 2, 3 ]
console.log(copy3); // [ 1, 2, 3 ]
```

얕은 복사인 copy1은 arr를 참조하기 때문에 0번째 요소가 같이 수정되었지만, 전개 연산자를 사용한 copy2와 copy3은 깊은 복사가 되었기 때문에 0번째 요소가 변경되지 않았다.

> 객체의 깊은 복사

객체 역시 전개 연산자로 깊은 복사를 사용할 수 있다. 무엇보다 강력한 점은 복사와 함께 새로운 값을 할당할 수 있다는 점이다.

```mm
let prevState = {
  name: "foo",
  birth: "1995-01-01",
  age: 25
};
let state = {
  ...prevState,
  age: 26
};

console.log(state); // {name: "foo", birth: "1995-01-01", age: 26}
```

위와 같이 ...prevState를 사용하여 기존 객체를 복사함과 동시에 age에 새로운 값을 할당했다.

## 함수에서의 비구조화 할당

함수의 파라미터 부분에서도 비구조화 할당을 사용할 수 있다. 이러한 문법은 특히 API 응답값을 처리하는데에 유용하게 사용된다.

```mm
function renderUser({name, age, addr}){
  console.log(name);
  console.log(age);
  console.log(addr);
}
const users = [
  {name: 'kim', age: 10, addr:'kor'},
  {name: 'joe', age: 20, addr:'usa'},
  {name: 'miko', age: 30, addr:'jp'}
];

users.map((user) => {
  renderUser(user);
});
// kim
// 10
// kor
// joe
// 20
// usa
// miko
// 30
// jp
```

users 배열의 map 메소드로 인하여 renderUser 함수에 users의 객체가 각각 전달된다.

각 객체의 key 값이 renderUser함수의 파라미터 받는 부분에서 비구조화 할당을 받았기 때문에 함수 내에서 객체의 key 값을 각각 가져올 수 있게 된다.

```mm
 const users = [
  {name: 'kim', age: 10, addr:'kor'},
  {name: 'joe', age: 20, addr:'usa'},
  {name: 'miko', age: 30, addr:'jp'}
];

users.map(({name, age, addr}) => {
  console.log(name);
  console.log(age);
  console.log(addr);
});
```

마찬가지로 위처럼 map 메소드의 파라미터에도 바로 사용할 수 있다.

## for of 문을 이용한 비구조화 할당

배열 내 객체들은 for of 문을 사용하여 비구조화 할 수 있다.

```mm
const users = [
  {name: 'kim', age: 10, addr:'kor'},
  {name: 'joe', age: 20, addr:'usa'},
  {name: 'miko', age: 30, addr:'jp'}
];

for(let {name : n, age : a} of users){
  console.log(n);
  console.log(a);
}
```

중첩된 객체 및 배열의 비구조화
중첩된 객체 및 배열 역시 비구조화가 가능하다.

```mm
const kim = {
  name: 'kim',
  age: 10,
  addr: 'kor',
  friends: [
    {name: 'joe', age: 20, addr:'usa'},
    {name: 'miko', age: 30, addr:'jp'}
  ]
};

let { name: userName, friends: [ ,{ name: jpFriend }] } = kim;
console.log(userName); // kim
console.log(jpFriend); // miko
```

## 보일러플레이트란?

컴퓨터 프로그래밍에서 보일러플레이트 또는 보일러플레이트 코드라고 부르는 것은 최소한의 변경으로 여러곳에서 재사용되며, 반복적으로 비슷한 형태를 띄는 코드를 말한다.

## JSON 포맷이란?

JavaScript Object Notation 의 줄임말인 `JSON`은 Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷이다. 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용한다.

# this 키워드

this란 선언이 실행 되는 시점의 나의 문맥을 나타낸다.(=기억한다)

this의 값은 호출한 방법에 의해 결정된다. 실행중에는 할당으로 설정할 수 없고 함수를 호출할 때 마다 다를 수 있다.

> 전역 문맥

```mm
// 웹 브라우저에서는 window 객체가 전역 객체
console.log(this === window); // true

a = 37;
console.log(window.a); // 37

this.b = "MDN";
console.log(window.b)  // "MDN"
console.log(b)         // "MDN"
```

> 함수 문맥
> 함수 내부에서 this의 값은 함수를 호출한 방법에 의해 좌우된다.

단순 호출

# 엄격 모드(Strict mode)

엄격하지 않은 기본값을 느슨한 모드(sloppy mode)라고 부르기도 한다.

JavaScript 의 엄격모드는 JavaScript 의 제한된 버전을 선택하여 암묵적인 "느슨한 모드(sloppy mode)" 를 해제하기 위한 방법이다.

그러나 엄격모드를 지원하지 않는 브라우저(Internet Explorer 10 버전 이하)에서는 엄격 모드의 코드가 다른 방식으로 동작 (그렇기 때문에 엄격 모드에 의존하면 안된다.)

엄격모드의 code와 비엄격모드의 code는 공존이 가능하다. 고로 엄격 모드를 일부만 선택하는 것이 점진적으로 가능하게 된다.

전체 스크립트 또는 부분 함수에 적용 가능하다. 그러나 {} 괄호로 묶여진 block 문, context에 적용되지 않는다.

엄격 모드는 평범한 자바스크립트의 시멘틱스에 몇가지 변경을 일으킨다.

1. 기존에는 조용히 무시되던 에러들을 throwing한다.
2. JavaScript 엔진의 최적화 작업을 어렵게 만드는 실수들을 바로잡는다. 가끔씩 엄격 모드의 코드는 비-엄격 모드의 동일한 코드보다 더 빨리 작동하도록 만들어진다.
3. 엄격 모드는 ECMAScript의 차기 버전들에서 정의 될 문법을 금지한다.

엄격한 모드는 일부 이전에 허용되었던 실수를 오류로 바꿔 놓는다.

자바 스크립트는 초보 개발자에게 쉬운 것이 되도록 설계되었으며, 때로는 오류를 일으킬만한 동작을 에러없이 시행한다. 이러한 방법은 즉각적인 문제를 해결하는데 도움이 되지만, 더 심각한 문제를 만들어 낼 수도 있다. 엄격한 모드는 이러한 실수를 오류로 처리해서 그것을 발견하고 즉시 고칠 수 있도록 한다.

## 시맨틱(Semantics)

프로그래밍에서,시맨틱은 코드 조각의 의미를 나타낸다.

## 래퍼 객체(wrapper object)

```mm
var str = "문자열";   // 문자열 생성

var len = str.length; // 문자열 프로퍼티인 length 사용
```

위 예제에서 생성한 문자열 str은 객체가 아닌데도 length 속성을 사용할 수 있다.

프로그램이 문자열 리터럴 str의 속성을 참조하려고 하면, 자바스크립트는 new String(str)을 호출한 것처럼 문자열 리터럴을 객체로 자동 변환해주기 때문이다.

이렇게 생성된 임시 객체는 String 객체의 메소드를 상속받아 속성을 참조하는 데 사용된다. 이후 속성의 참조가 끝나면 사용된 임시 객체는 자동으로 삭제된다.

이렇게 숫자, 문자열, 불리언 등 원시 타입의 프로퍼티에 접근하려고 할 때 생성되는 임시 객체를 래퍼 객체(wrapper object)라고 한다.

ex)

```mm
var str = "문자열";           // 문자열 리터럴 생성
var strObj = new String(str); // 문자열 객체 생성
str.length;                   // 리터럴 값은 내부적으로 래퍼 객체를 생성한 후에 length 속성을 참조함.
str == strObj;                // 동등 연산자는 리터럴 값과 해당 래퍼 객체를 동일하게 봄.
str === strObj;               // 일치 연산자는 리터럴 값과 해당 래퍼 객체를 구별함.
typeof str;                   // string 타입
typeof strObj;                // object 타입
```

# Property(속성)이란?

기본적으로 property란 어떤 값을 나타낸다. 그런데 이 값이 다른 값과 연관을 가지고 있을 때 `property`라고 부른다.

예를 들어 length라는 property가 있는데 이 property는 문자열 안에 있는 문자의 양을 정수로 나타낸 값을 담고 있다.

이하는 MDN에서 정의하는 Property이다.

Property란 해당 Object의 특징이다. Property는 보통 데이터 구조와 연관된 속성을 나타낸다. Property에는 2가지 종류가 있다.

- 인스턴스 property들은 특정 object 인스턴스의 특정한 데이터를 가지고 ㅇ있다.
- Static Property들은 모든 object 인스턴스들에게 공유 된 데이터를 가지고 있다.

property는 이름(a string)과 값(primitive, method 또는 object reference). 보통 "프로퍼티가 object를 가지고 있다"라고 말하는 것은 "property가 object reference"를 가지고 있다는 것을 줄여서 말한 것이라는 것을 기억하자. property의 값이 변한 후에도 object는 그대로 남아있기 때문에 이걸 구분하는 것은 중요하다.

> Property와 method의 관계

프로퍼티는 object를 위해서 데이터를 저장한다.

메소드는 object가 요청 받을 수 있는 액션이다.

또한 일반적으로 함수를 담은 프로퍼티를 메소드라고 부른다.

> property에 접근하는 방법

프로퍼티에 접근하는 방법은 2가지가 있다. 대괄호로 접근하거나 점 표기법을 이용한다.

```js
var text = "purple haze";
test["length"]; //11
test.length; //11
```

# 서브 루틴(subroutin)

Subroutin은 아주 오래 된 개념이며 복잡한 코드를 간단하게 만드는 기초적인 수단이다.

서브루틴은 프로시저, 루틴, 서브프로그램, 매크로 등 다양한 이름으로 불린다. 이들은 모두 매우 단순하고 범용적인, 호출할 수 있는 한 단위를 일컫는 말이다.
또한 서브루틴은 대개 어떤 알고리즘을 나타내는 형태이다.

# 컬렉션(Collection)

- Map
- Set
- WeakMap
- WeakSet

등의 자료구조가 포함되어 있으며 Collection 객체는 여러 원소들을 담을 수 있는 자료구조를 뜻한다

배열이 가장 기본적인 컬렉션 자료구조에 속한다.

# 파싱

파싱 === 문자를 읽는다 정도의 개념으로 이해하면 된다.

우리의 컴퓨터 및 프로그램들은 좌에서 우로 그리고 위에서 아래로 문서를 파싱한다.

# 렌더링

렌더링(Rendering)은 컴퓨터 프로그램을 사용하여 모델(또는 이들을 모아놓은 장면인 씬(scene) 파일)로부터 영상을 만들어내는 과정을 말한다.

한마디로 클라이언트(사용자)에서 서버에 파일을 받아 브라우저에 뿌려주는 과정이라고 볼 수 있다.

클라이언트란 단어는 편하게 사용자라고 이해하면 쉽다. 모바일에서 접속하면, 모바일 === 클라인언트 // pc에서 접속하면, pc === 클라이언트가 되는 셈이다.

또한 컴퓨터는 html이 불러와 지고 그 다음 css 및 javascript가 렌더링 된다.

다음은 렌더링 되는 과정에 대해 네이버에서 설명해놓은 그림자료이다.
<img src = https://tuhbm.github.io/images/rendering/rendering1.png>

## DOM 트리

DOM 트리란 하나의 태그로 구성된 형태라고 보면 된다.

```
<div>
    <p>DOM트리</p>
</div>
```

위 예제를 통해 설명하자면 ‘div’라는 돔이 있고, 그자식으로 ‘p’라는 돔이 ‘DOM트리’ 라는 텍스트를 가지고 있다.

우리가 사용하는 태그 하나하나가 모두 DOM이 된다는 것이다.

## 렌더트리

렌더 트리란 쉽게표현해 html과 css 그리고 넓게는 javascript까지

스타일에 관여하는 모든 문서를 파싱하고 html의 돔에 적용을 시키기 전에

한마디로 그리기 전에 기억을 해두는 것이라고 생각을 하면 편하다.

어떠한 DOM은 display가 block이고, 어떠한 DOM은 color가 #000이고, 이러한 과정을 각각의 돔을 실제 그리기전에 스타일을 입히는 것을 의미한다.

> 웹킷
> <img src = https://tuhbm.github.io/images/rendering/rendering2.png>

> 모질라 게코
> <img src = https://tuhbm.github.io/images/rendering/rendering3.png>

한마디로 문서가 길수록, 구조가 복잡하면, 렌더링에 영향이 커진다.

그렇기 때문에 불필요한 태그 및 필요없는 부분을 지워야 하는 것이다.

# 비동기적 프로그래밍

> '비동기적'(Asynchronous) 이란?

일반적으로, 프로그램의 코드는 순차적으로 진행된다. 한번에 한가지 사건만 발생하면서 말이다. 만약 어떤 함수의 결과가 다른 함수에 영향을 받는다면, 그 함수는 다른 함수가 끝나고 값을 산출할 때까지 기다려야 한다. 그리고 그 과정이 끝날 때 까지, 유저의 입장에서 보자면, 전체 프로그램이 모두 멈춘 것처럼 보인다.

예를들면, 맥 환경에서 종종 회전하는 무지개색 커서(비치볼)가 있다고 한다. 이 커서는 오퍼레이팅 시스템이 이렇게 말하고 있는 것이라고 한다.

```
 당신이 지금 사용하고 있는 시스템은 지금 멈춰서서 뭔가가 끝나기를 기다려야만 합니다. 그리고 이 과정은 당신이 지금 무슨 일이 일어나고있는지 궁금해 할 만큼 오래 걸리고 있습니다."
```

이러한 경우는 요즘과 같이 컴퓨터가 여러개 프로세서를 돌리는 시대에는 컴퓨터 성능을 효율적으로 쓰지 못하는 처사이며 당황스러운 경우이다. 만약 내가 다른 코어 프로세서에 다른 작업들을 움직이게 하고 작업이 완료되면 알려줄 수 있을 때, 무언가를 기다리는 것은 의미가 없다.

그 동안 다른 작업을 수행할 수 있고, 이것이 비동기 프로그래밍의 기본이다. 또한 비동기 기법은 특히 웹 프로그래밍에 매우 유용하다.

왜냐하면 웹 앱이 브라우저에서 특정 코드를 실행하느라 브라우저에게 제어권을 돌려주지 않으면 브라우저는 마치 정지된 것처럼 보일 수 있다. 이러한 현상을 blocking 이라고 부른다.

> Blocking
> Blocking을 자세히 정의하자면, 사용자의 입력을 처리하느라 웹 앱이 프로세서에 대한 제어권을 브라우저에게 반환하지 않는 현상이다.

특히 자바스크립트는 본적으로 single threaded이기 때문에 이러한 현상에 취약하다.

컴퓨터가 여러 개의 CPU를 가지고 있어도 main thread라 불리는 단일 thread에서만 작업을 실행할 수 있다.

현대의 소프트웨어 설계는 프로그램이 한 번에 두 가지 이상의 일을 할 수 있도록 비동기 프로그래밍을 중심으로 돌아가고 있다는 점을 기억하자.

# 가비지 컬렉션

자바스크립트는 눈에 보이지 않는 곳에서 메모리 관리를 수행한다

원시값, 객체, 함수 등 우리가 만드는 모든 것은 메모리를 차지한다.

> 가비지 컬렉션 기준

자바스크립트는 도달 가능성(reachability) 이라는 개념을 사용해 메모리 관리를 수행한다.
‘도달 가능한(reachable)’ 값은 쉽게 말해 어떻게든 접근하거나 사용할 수 있는 값을 의미한다. 도달 가능한 값은 메모리에서 삭제되지 않는다.

다음 값들은 태생부터 도달 가능하기 때문에, 명백한 이유 없이는 삭제되지 않는다.

- 현재 함수의 지역 변수와 매개변수
- 중첩 함수의 체인에 있는 함수에서 사용되는 변수와 매개변수
- 전역 변수
- 기타 등등

이러한 값들을 루트(root)라고도 부른다.

또한 루트가 참조하는 값이나 체이닝으로 루트에서 참조할 수 있는 값은 도달 가능한 값이 된다.

전역 변수에 객체가 저장되어있다고 가정해 보자. 이 객체의 프로퍼티가 또 다른 객체를 참조하고 있다면, 프로퍼티가 참조하는 객체는 도달 가능한 값이 된다. 이 객체가 참조하는 다른 모든 것들도 도달 가능하다고 여겨진다.

자바스크립트 엔진 내에선 가비지 컬렉터(garbage collector)가 끊임없이 동작한다. 가비지 컬렉터는 모든 객체를 모니터링하고, 도달할 수 없는 객체는 삭제한다.

# DOMString

DOMString은 UTF-16 문자열을 의미한다. JavaScript의 String도 UTF-16 문자열이기 때문에 DOMString은 String으로 연결된다.

DOMString을 받는 매개변수에 null을 전달하면, 보통 문자열로 변환해 "null"이 된다.

# 린팅(Linting)

린팅(Linting)이란 코드를 작성할 때 규약을 자동으로 맞춰주는 도구이다. 린팅은 매우 중요하지는 않지만 매우 필수이다.

왜냐하면 린팅은 단순하게는 코드 포멧팅을 해주는 것이라 실행 시 영향을 미치는 부분이 아니라서 매우 중요하지는 않지만 규칙이 정확히 정해지지 않은 코드를 유지보수 하다보면 생산성이 떨어지기 때문에 매우 필수이다.

린팅은 간단하게는 단순히 함수 뒤에 띄어쓰기를 안했다던지 함수 인자에 띄어쓰기를 생략했다던지 할 때 강제로 띄어쓰기를 넣어주거나 삭제해주거나 등의 일을 하면서 코드의 포멧을 일정하게 잡아준다.

린팅의 규칙은 설정 파일을 통해 각 프로젝트 별로 다르게 지정할 수도 있고 이미 정한 규칙 설정을 확장하여 일부만 바꿔서 사용하는 것도 가능하다.

또한 대부분 린팅을 협업 시 코딩 규약을 맞추기 위함으로 알고 있는데, 혼자 작업을 하더라도 린팅은 필수이다. 왜냐하면 하나의 함수를 작성하더라도 다양한 형태로 코드를 작성할 수 있고, 작성 형식이 다르다보면 차후 해당 소스를 찾아볼때 검색에서 걸리지 않거나 여러 형태로 검색을 여러 번 해야하기 때문이다.

# 커밋 메시지 컨벤션(Commit Message Convention)

커밋 메시지를 작성할 때에는 원칙을 정하고 일관성 있게 작성할 필요가 있다.

## 장점

커밋을 작성할 때는 원칙을 정하고 일관성 있게 작성할 필요가 있다. 또한 커밋 메시지는 작업단위를 구분할 수 있도록 도와준다. ( 커밋의 타입을 지정할 때, 해당 커밋만 들어가도록 생각하기 때문에 작은 단위로 커밋을 분리하고 설명을 자세히 기재 할 수 있기 때문이다.)

또한 깃헙에서 커밋을 검색할 수 있는 만큼 동일한 레이아웃으로 커밋을 작성하게 된다면 검색또한 용이해진다. 또한 빌드와 배포 프로세스에서 어느 부분까지 배포할지 빌드할지 정할 수 있는 기준이 된다. 협업할 때에도 다른 동료 개발자가 무엇을 수정했는지 등을 쉽게 알수 있도록 해준다.

```js
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

1. `<type> `

타입은 커밋의 종류를 의미하는데 가장 기본적으로 커밋을 검색하기에 가장 큰 역할을 수행한다.

타입의 종류는 아래와 같다.

- fix : 버그 패치
- feat : 새 기능 추가
- docs : 문서 수정
- refactor : 버그도 아니고 새로운 기능이 추가되거나 그런게 아닌 코드 수정을 할 때
- style : 코드의 전체적인 중요 변경되는 것이 아니라 스타일이나 세미콜론 안찍은거나 띄어쓰기 같은관련 수정
- build : 빌드시스템에 변화가 있거나 외부 라이브러리를 추가했을 때
- perf : 퍼포먼스 측면에서 코드에 변화를 주었을 때
- test : 빠진 테스트나 테스트 코드를 수정할 때

2. [optional scope]

영향을 받은 npm 패키지 이름을 적는 것이라고함..!
자세한 내용은 아래에서 확인이 필요함.
https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines

3. <description>

설명을 적는 부분

4. [optional body]

설명보다 더 자세하게 작성하는 바디 부분이다. 선택사항이라 기재하지 않아도 된다.

5. [optional footer]

말꼬리 부분에 해당하는 부분이다. 여기또한 선택사항이라 기재하지 않아도 된다.

큰 변화가 있어서 타인에게 알려줘야할 때에는 footer 영역에 BREAKING CHANGE: 라는 단어를 쓰고 뒤에 설명을 쓰거나 type을 적고 ! 를 붙여 넣는다. 약간 강조를 해주는 느낌으로 사용하면된다.

# API (Application Programming Interfaces, API)란

API = 애플리케이션 프로그래밍 인터페이스(Application Programming Interface)는 애플리케이션 소프트웨어를 구축하고 통합하는 정의 및 프로토콜 세트이다.

때때로 API는 정보 제공자와 정보 사용자 간의 계약으로 지칭되며 소비자에게 필요한 콘텐츠(호출)와 생산자에게 필요한 콘텐츠(응답)를 구성한다.

예를 들어 날씨 서비스용 API에서는 사용자는 우편번호를 제공하고, 생산자는 두 부분(첫 번째는 최고 기온, 두 번째는 최저 기온)으로 구성된 응답으로 답하도록 지정할 수 있다.

즉, 컴퓨터나 시스템과 상호 작용하여 정보를 검색하거나 기능을 수행하고자 할 때 API는 사용자가 원하는 것을 시스템에 전달할 수 있게 지원하여 시스템이 이 요청을 이해하고 이행하도록 할 수 있다.

API를 사용자 또는 클라이언트, 그리고 사용자와 클라이언트가 얻으려 하는 리소스 사이의 조정자로 생각하면 된다. 또한 API는 조직이 보안 및 제어를 유지관리(누가 무엇에 액세스할 수 있는지 결정)하면서 리소스와 정보를 공유할 수 있는 방법이기도 하다.

API의 또 다른 이점은 리소스 검색 방법 또는 리소스의 출처에 대한 지식 없이도 사용이 가능하다는 점이 있다.

# REST란?

REST는 Representational State Transfer의 줄임말로써 자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다. 즉 자원(resource)의 표현(representation)에 의한 상태 전달을 의미한다.

이는 두 가지 의미로 나뉜다.

1. 자원(resource)의 표현(representation)

- 자원 : 해당 소프트웨어가 관리하는 모든 것을 의미한다. (ex : 문서, 그림, 데이터, 해당 소프트웨어 자체 등)
- 자원의 표현 : 그 자원을 표현하기 위한 이름을 의미한다. (ex : DB의 학생 정보가 자원일 때, 'students'를 자원의 표현으로 정한다.)

2. 상태(정보) 전달

- 데이터가 요청되어지는 시점에서 자원의 상태(정보)를 전달한다.
- json 혹은 xml 등을 통해 데이터를 주고받는 것이 일반적인 형태이다.

REST는 기본적으로 웹의 기존 기술과 HTTP 프로토콜을 그대로 활용하기 때문에 웹의 장점을 최대한 활용할 수 있는 아키텍처 스타일이다. 또한 REST는 네트워크 상에서 Client와 Server 사이의 통신 방식 중 하나이다.

## REST의 구체적인 개념

HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고, HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.

즉, REST는 자원 기반의 구조(ROA, Resource Oriented Architecture) 설계의 중심에 Resource가 있고 HTTP Method를 통해 Resource를 처리하도록 설계된 아키텍쳐를 의미한다.

웹 사이트의 이미지, 텍스트, DB 내용 등의 모든 자원에 고유한 ID인 HTTP URI를 부여한다.

CRUD Operation

- Create : 생성(POST)
- Read : 조회(GET)
- Update : 수정(PUT)
- Delete : 삭제(DELETE)
- HEAD: header 정보 조회(HEAD)

## REST의 장단점

> 장점

1. HTTP 프로토콜의 인프라를 그대로 사용하므로 REST API 사용을 위한 별도의 인프라를 구출할 필요가 없다.

2. HTTP 프로토콜의 표준을 최대한 활용하여 여러 추가적인 장점을 함께 가져갈 수 있게 해준다.

3. HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능하다.

4. Hypermedia API의 기본을 충실히 지키면서 범용성을 보장한다.

5. REST API 메시지가 의도하는 바를 명확하게 나타내므로 의도하는 바를 쉽게 파악할 수 있다.

6. 여러가지 서비스 디자인에서 생길 수 있는 문제를 최소화한다.

7. 서버와 클라이언트의 역할을 명확하게 분리한다.

> 단점

1. 표준이 존재하지 않는다.

2. HTML Method 형태가 제한적이라 사용할 수 있는 메소드가 4가지 뿐이다.

3. 브라우저를 통해 테스트할 일이 많은 서비스라면 쉽게 고칠 수 있는 URL보다 Header 값이 왠지 더 어렵게 느껴진다.

## REST가 필요한 이유

- 애플리케이션 분리 및 통합
- 다양한 클라이언트의 등장
- 최근의 서버 프로그램은 다양한 브라우저와 안드로이폰, 아이폰과 같은 모바일 디바이스에서도 통신을 할 수 있어야 하기 때문

이러한 멀티 플랫폼에 대한 지원을 위해 서비스 자원에 대한 아키텍처를 세우고 이용하는 방법을 모색한 결과, REST에 관심이 늘었다.

## REST의 구성 요소

1. 자원(Resource) : URI

   - 모든 자원에는 고유한 id가 존재하고, 이 자원은 server에 존재한다.
   - 자원을 구별하는 id는 ‘/groups/:group_id’와 같은 HTTP URI이다.
   - Client는 URI를 이용해서 자원을 지정하고 해당 자원의 상태(정보)에 대한 조작을 Server에 요청한다.

2. 행위(Verb) : HTTP Method

   - HTTP 프로토콜의 Method를 사용한다.
   - HTTP 프로토콜은 GET, POST, PUT, DELETE와 같은 메소드를 제공한다.

3. 표현(Represntation of Resource)
   - Client가 자원의 상태(정보)에 대한 조작을 요청하면 Server는 이에 적절한 응답(Representation)을 보낸다.
   - REST에서 하나의 자원은 JSON, XML, TEXT, RSS 등 여러 형태의 Representation으로 나타내어 질 수 있다.
   - JSON 혹은 XML를 통해 데이터를 주고 받는 것이 일반적이다.

## REST 특징

1. Server-Client(서버-클라이언트 구조)

   - 자원이 있는 쪽이 Server, 자원을 요청하는 쪽이 Client가 된다.
     - REST Server: API를 제공하고 비즈니스 로직 처리 및 저장을 책임진다.
     - Client: 사용자 인증이나 context(세션, 로그인 정보) 등을 직접 관리하고 책임진다.
   - 서로 간 의존성이 줄어든다.

2. Stateless(무상태)

   - HTTP 프로토콜은 Stateless Protocol 이므로 REST 역시 무상태성을 갖는다.
   - Client의 context를 Server에 저장하지 않는다.
     - 즉, 세션과 쿠키와 같은 context 정보를 신경쓰지 않아도 되므로 구현이 단순해진다.
   - Server는 각각의 요청을 완전히 별개의 것으로 인식하고 처리한다.
     - 각 API 서버는 Client의 요청만을 단순 처리한다.
     - 즉, 이전 요청이 다음 요청의 처리에 연관되어서는 안된다.
     - 물론 이전 요청이 DB를 수정하여 DB에 의해 바뀌는 것은 허용한다.
     - Server의 처리 방식에 일관성을 부여하고 부담이 줄어들며, 서비스의 자유도가 높아진다.

3. Cacheable(캐시 처리 가능)

   - 웹 표준 HTTP 프로토콜을 그대로 사용하므로 웹에서 사용하는 기존의 인프라를 그대로 활용할 수 있다.
     - 즉, HTTP가 가진 가장 강력한 특징 중 하나인 캐싱 기능을 적용할 수 있다.
     - HTTP 프로토콜 표준에서 사용하는 Last-Modified 태그나 E-Tag를 이용하면 캐싱 구현이 가능하다. (??)
   - 대량의 요청을 효율적으로 처리하기 위해 캐시가 요구된다.
   - 캐시 사용을 통해 응답시간이 빨라지고 REST Server 트랜잭션이 발생하지 않기 때문에 전체 응답시간, 성능, 서버의 자원 이용률을 향상시킬 수 있다.

4. Layered System(계층화)

   - Client는 REST API Server만 호출한다.
   - REST Server는 다중 계층으로 구성될 수 있다.
     - API Server는 순수 비즈니스 로직을 수행하고 그 앞단에 보안, 로드밸런싱, 암호화, 사용자 인증 등을 추가하여 구조상의 유연성을 줄 수 있다.
     - 또한 로드밸런싱, 공유 캐시 등을 통해 확장성과 보안성을 향상시킬 수 있다.
   - PROXY, 게이트웨이 같은 네트워크 기반의 중간 매체를 사용할 수 있다.

5. Code-On-Demand(optional)

   - Server로부터 스크립트를 받아서 Client에서 실행한다.
   - 반드시 충족할 필요는 없다.

6. Uniform Interface(인터페이스 일관성)
   - URI로 지정한 Resource에 대한 조작을 통일되고 한정적인 인터페이스로 수행한다.
   - HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용이 가능하다.
     - 특정 언어나 기술에 종속되지 않는다.

# REST API

Roy Fielding이라는 사람이 만든 HTTP 요청 시스템(GET,POST,PUT,DELETE). 이 사람이 만든 논문에서 REST 원칙을 소개하였는데 이것이 거의 정론처럼 받아들여진 API 구성 규약같은 것.

## REST API의 정의

REST 기반으로 서비스 API를 구현한 것이다.

최근 OpenAPI(누구나 사용할 수 있도록 공개된 API: 구글 맵, 공공 데이터 등), 마이크로 서비스(하나의 큰 애플리케이션을 여러 개의 작은 애플리케이션으로 쪼개어 변경과 조합이 가능하도록 만든 아키텍처) 등을 제공하는 업체 대부분은 REST API를 제공한다.

## REST API의 특징

- 사내 시스템들도 REST 기반으로 시스템을 분산해 확장성과 재사용성을 높여 유지보수 및 운용을 편리하게 할 수 있다.

- REST는 HTTP 표준을 기반으로 구현하므로, HTTP를 지원하는 프로그램 언어로 클라이언트, 서버를 구현할 수 있다.

- 즉, REST API를 제작하면 델파이 클라이언트 뿐 아니라, 자바, C#, 웹 등을 이용해 클라이언트를 제작할 수 있다.

## REST API 간단 원칙 6개

1. `Uniform interface` (중요)

   - URL을 작성할 때 간결하고 형식이 일관적이어야 함.(하나의 자료는 하나의 URL로)
   - URL이 예측가능 해야함(URL 하나를 알면 둘을 알 수 있어야 함)
   - 요청과 응답은 정보가 충분히 들어있어야 함

2. Client-Server 역할 구분이 명확해야함.

   - 브라우저는 요청만 할 뿐이고
   - 서버는 응답만 할 뿐임을 명시해야함.

3. Stateless

   - 요청 1과 요청 2는 의존성이 없이 독립적이어야 함.

4. Cacheable

   - 서버에서 보내주는 정보들은 캐싱이 가능해야 함.
   - 캐싱을 위한 버전관리를 잘해야 함.
     (크롬같은 브라우저가 잘해주는 부분이라 중요하지 않음)

5. Layered System

6. Code on Demand

## 좋은 REST API 예시

좋은 REST API 예시는

www.example.com/product/33214
instargram.com/explore/tags/jpop/
facebook.com/natgeo/photos/

좋은 REST API 이름을 지을 때 다음과 같은 원칙을 지키는 것이 좋다.

- URL을 가급적 명사로 작성하기

- 하위문서를 나타낼 때처럼 `/` 기호 사용으로 세분화하여 구분짓기

- 띄어쓰기는 가급적 대시(-) 사용하기

- 자료 하나당 하나의 URL 사용하기.

## REST API 설계 기본 규칙

1. URI는 정보의 자원을 표현해야 한다.

- resource는 동사보다는 명사를, 대문자보다는 소문자를 사용한다.
- resource의 도큐먼트 이름으로는 단수 명사를 사용해야 한다.
- resource의 컬렉션 이름으로는 복수 명사를 사용해야 한다.
- resource의 스토어 이름으로는 복수 명사를 사용해야 한다.
  - Ex) GET /Member/1 -> GET /members/1

2. 자원에 대한 행위는 HTTP Method(GET, PUT, POST, DELETE 등)로 표현한다.

- URI에 HTTP Method가 들어가면 안된다.
  - Ex) GET /members/delete/1 -> DELETE /members/1
- URI에 행위에 대한 동사 표현이 들어가면 안된다.(즉, CRUD 기능을 나타내는 것은 URI에 사용하지 않는다.)
  - Ex) GET /members/show/1 -> GET /members/1
  - Ex) GET /members/insert/2 -> POST /members/2
- 경로 부분 중 변하는 부분은 유일한 값으로 대체한다.(즉, :id는 하나의 특정 resource를 나타내는 고유값이다.)
  - Ex) student를 생성하는 route: POST /students
  - Ex) id=12인 student를 삭제하는 route: DELETE /students/12

## REST API 설계 규칙

1. 슬래시 구분자(/ )는 계층 관계를 나타내는데 사용한다.

   - Ex) http://restapi.example.com/houses/apartments

2. URI 마지막 문자로 슬래시(/ )를 포함하지 않는다.

- URI에 포함되는 모든 글자는 리소스의 유일한 식별자로 사용되어야 하며 URI가 다르다는 것은 리소스가 다르다는 것이고, 역으로 리소스가 다르면 URI도 달라져야 한다.
- REST API는 분명한 URI를 만들어 통신을 해야 하기 때문에 혼동을 주지 않도록 URI 경로의 마지막에는 슬래시(/)를 사용하지 않는다.
  - Ex) http://restapi.example.com/houses/apartments/ (X)

3. 하이픈(- )은 URI 가독성을 높이는데 사용

- 불가피하게 긴 URI경로를 사용하게 된다면 하이픈을 사용해 가독성을 높인다.

4. 밑줄(\_ )은 URI에 사용하지 않는다.

- 밑줄은 보기 어렵거나 밑줄 때문에 문자가 가려지기도 하므로 가독성을 위해 밑줄은 사용하지 않는다.

5. URI 경로에는 소문자가 적합하다.

- URI 경로에 대문자 사용은 피하도록 한다.
- RFC 3986(URI 문법 형식)은 URI 스키마와 호스트를 제외하고는 대소문자를 구별하도록 규정하기 때문 `(???)`

6. 파일확장자는 URI에 포함하지 않는다.

- REST API에서는 메시지 바디 내용의 포맷을 나타내기 위한 파일 확장자를 URI 안에 포함시키지 않는다.
- Accept header를 사용한다.
  - Ex) http://restapi.example.com/members/soccer/345/photo.jpg (X)
  - Ex) GET / members/soccer/345/photo HTTP/1.1 Host: restapi.example.com Accept: image/jpg (O)

7. 리소스 간에는 연관 관계가 있는 경우

- /리소스명/리소스 ID/관계가 있는 다른 리소스명
  - Ex) GET : /users/{userid}/devices (일반적으로 소유 ‘has’의 관계를 표현할 때)

## REST API 설계 예시

<img src="https://gmlwjd9405.github.io/images/network/restapi-example.png">

# 응답상태코드

1xx : 전송 프로토콜 수준의 정보 교환

2xx : 클라어인트 요청이 성공적으로 수행됨

3xx : 클라이언트는 요청을 완료하기 위해 추가적인 행동을 취해야 함

4xx : 클라이언트의 잘못된 요청

5xx : 서버쪽 오류로 인한 상태코드

# RESTful의 개념

## RESTful이란?

RESTful은 일반적으로 REST라는 아키텍처를 구현하는 웹 서비스를 나타내기 위해 사용되는 용어이다. ‘REST API’를 제공하는 웹 서비스를 ‘RESTful’하다고 할 수 있다.

RESTful은 REST를 REST답게 쓰기 위한 방법으로, 누군가가 공식적으로 발표한 것이 아니다. 즉, REST 원리를 따르는 시스템은 RESTful이란 용어로 지칭된다.

## RESTful의 목적

이해하기 쉽고 사용하기 쉬운 REST API를 만드는 것이다.

RESTful한 API를 구현하는 근본적인 목적이 성능 향상에 있는 것이 아니라 일관적인 컨벤션을 통한 API의 이해도 및 호환성을 높이는 것이 주 동기라서 성능이 중요한 상황에서는 굳이 RESTful한 API를 구현할 필요는 없다.

## RESTful 하지 못한 경우

- CRUD 기능을 모두 POST로만 처리하는 API

- route에 resource, id 외의 정보가 들어가는 경우(/students/updateName)

등이 해당된다.

# URI , URL, URN

URI (Uniform Resource Identifier) 란 인터넷 자원을 나타내는 고유 식별자 이다.

URi가 가장 포괄적인 개념이고 , URL과 URN으로 나뉜다.

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FAkL2o%2FbtqJptEQJmu%2FomyDDiWIRr99BFKeVIpTt0%2Fimg.png">

## URL (Uniformed Resource Locator)

- 프로토콜을 포함
- 해당 자원의 위치, Path를 의미
- 일반적으로 사이트 도메인을 자주 의미함.
- 웹 상 뿐만 아니라 컴퓨터 네트워크상의 자원은 모두 나타낼 수 있다

## URN (Uniformed Resource Name)

- 프로토콜을 포함 X
- 해당 자원의 이름을 의미
- 독립적인 자원 지시자
- Page 이후 부분까지 포함

## 2줄 요약

1. `URI` 는 네트워크 상 자원을 가리키는 일종의 고유 식별자(ID) 이다.

2. URL, URN 은 `URI` 에 포함되는 개념이며 `URL`은 자원의 위치, `URN` 은 자원의 이름을 의미한다.

# 데이터 베이스

데이터베이스는 전통이 매우 깊다.

과거엔 계층형, 네트워크 이런 데이터베이스들이 있었고 최근들어 Graph 이런 데이터베이스까지도 등장했다.

하지만 현재 실제 웹서비스 개발시 이용하는 데이터베이스는 대부분 `관계형 데이터베이스`, `NoSQL 데이터베이스` 이 둘 중 하나로 분류한다.

## 관계형 데이터 베이스

<img src=> // 데이터베이스 사진들어갈 부분

80년대 부터 흥하기 시작해서 아직까지도 사용하고 있는 데이터베이스의 표준 같은 데이터베이스이다.

관계형 데이터베이스는 짧게 요약하자면

엑셀처럼 행과 열로 데이터를 저장할 수 있는 데이터베이스를 뜻한다.

엑셀의 시트처럼생긴 테이블이라고 부르는 공간을 하나 생성한 다음 행과 열에 맞춰 데이터를 쭉 저장하는 방식을 가진다.

### 관계형 데이터 베이스의 특징

- 거의 모든 곳에 사용할 수 있어 범용적이다.

- 구조화된 데이터를 저장하기 가장 좋다.

- 보통 SQL이라는 언어를 이용해 데이터를 출력 입력한다.

- "이 열엔 숫자가 들어옵니다~"라고 스키마를 미리 정의하기 때문에 관리가 쉽다.

- 구조화된 데이터 덕분에 원하는 데이터 뽑기도 쉽다.

- 트랜잭션, 롤백 등의 기능을 이용해 데이터의 무결성을 보존하기 쉽기 때문에 금융, 거래 서비스에 필수적이다.

---

## NoSQL 데이터베이스

SQL문없이도 사용할 수 있는 데이터베이스라고 보면 된다.

대부분 테이블에 국한되지 않고 자유로운 형식으로 데이터를 쉽게 분산저장할 수 있다.

<img src=> // 데이터베이스 사진들어갈 부분

### 종류

종류는 매우 여러가지가 있다.

- Key-value 모델 : Object, JSON 자료형 형식으로 데이터를 쉽게쉽게 저장, 출력이 가능하다. 가장 심플함

- Document 모델 : 테이블 대신 Collection이라는 문서 기반으로 데이터를 분류하고 저장한다. 테이블보다는 훨씬 유연하다.
  (우리가 사용하고 있는 MongoDB도 Key-value, Document 모델 저장방식을 차용하고 있다)

- Graph 모델 : 데이터를 노드의 형태로 저장하고 노드간의 흐름 또는 관계를 저장할 수 있다.

- Wide-column 모델 : 한 행마다 각각 다른 수, 다른 종류의 열을 가질 수 있다. (스키마가 자유로움)

### 특징

1. Scaling이 쉽다는 장점이 있다.

찰나의 순간에 대량의 데이터를 저장해야한다면 어떻게할까?

기존 올드한 관계형 데이터베이스는 확장이 매우 어렵다. 보통 scale up 이라는 방법으로 서버의 성능을 키워야한다.

하지만 대부분의 NoSQL 데이터베이스는 scale out이라는 방법으로 데이터를 분산저장하는 걸 기본적으로 지원한다.

확정 걱정할 필요없이 쉽게 쉽게 데이터 입출력에만 신경쓸 수 있는 것이다.

그래서 대량의 데이터를 빠르게 입출력해야한다면 NoSQL이 제격이다.

(그러나 관계형 데이터베이스도 요즘은 분산저장 대충 잘한다고 한다..)

2. 대부분 다루기가 쉽다.

SQL 이라는 언어를 새로 배우지 않아도 데이터를 쉽게 입출력할 수 있다.

자바스크립트 object{} 자료형 다루듯이 데이터를 입출력할 수 있으니 사용자에게 매우 편리하다.

그리고 우리가 서버에서 쓰던 프로그래밍 언어로 DB를 다룰 수 있다는 장점이 있습니다. MongoDB가 가장 대표적인 예이다.

3. 대부분 스키마 정의 없이도 쉽게 쓸 수 있다. (이 열의 데이터는 정수입니다~ 라고 표현하는 짓거리 안해도 됨)

장점이자 단점일 수 있다. 그래서 MongoDB에선 스키마를 미리 정의하기 위한 Mongoose같은 라이브러리를 추가해서 사용하기도 한다.

4.  NoSQL 데이터베이스는 기본적으로 SQL에서의 JOIN 연산을 적용하는게 기본적으로 어렵다.

서버 단에서 JOIN 연산을 쉽게 처리해주는 라이브러리를 이용한다.

---

# DOM

## DOM이란?

MDN에서 말하는 DOM의 정의란 문서 객체 모델(The Document Object Model, 이하 DOM) 은 HTML, XML 문서의 프로그래밍 interface 이다.

DOM은 문서의 구조화된 표현(structured representation)을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공하여 그들이 문서 구조, 스타일, 내용 등을 변경할 수 있게 돕는다.

또한 DOM 은 구조화된 nodes와 property 와 method 를 갖고 있는 objects로 문서를 표현한다. 이들은 웹 페이지를 스크립트 또는 프로그래밍 언어들에서 사용될 수 있게 연결시켜주는 역할을 담당한다.

그러나 위의 설명들만으론 아리송한 부분이 많다.

> 내가 작성한 HTML 코드는 DOM인가?

아니다. 하지만 그렇게 작성한 코드가 브라우저에 의해 파싱이 되면 DOM이 된다.

> 그렇다면 페이지의 View Source가 DOM인가?

이또한 아니다. View Source는 페이지를 이루고 있는 html을 보여줄 뿐이며, 이는 즉 내가 작성한 html을 의미한다.

> DevTools에서 보이는 코드가 DOM인가?

맞다. 브라우저에서 지원하는 개발자 툴에서 보이는 것이 바로 DOM이라고 한다.

개발자 툴에서 시각적으로 표현한 DOM이 내가 작성한 HTML 코드와 동일할 수는 있지만, 대부분의 경우 달라지게 되며 DevTool에서는 이러한 변경 사항이 적용되어 표시된다.

# 크로스 브라우징

세상에는 크롬, 사파리, 인터넷 익스플로어, 오페라, 파이어폭스, 웨일 등등 많은 브라우저들이 존재한다.

이렇게 많은 브라우저들의 동작 방식은 W3C라는 국제 웹 표준화 기구에서 제공하는 스펙(가이드라인)을 따라서 동작하게 된다.

그러나 표준화 기구에서 제공하지 않는 스펙에 대한 아주 디테일한 내용들은 각자의 상황에 맞게, 각자의 스타일에 맞게 구현하게 되어있다. 

**그래서 개발자들은 자신이 짠 한줄의 코드가 모든 브라우저에서 동일하게, 그리고 올바르게 동작할 것이라 생각하면 안된다.**

예를 들어 과거 netscape라는 브라우저에서는 이벤트 등록을 아래의 메서드로 했다고 한다.
```js
addEventListner
```
그러나 IE는 아래와 같다
```IE
attachEvent
```

이게 바로 `크로스 브라우징 이슈`이다. (모바일 브라우저들까지 생각해야한다..)

# 파편화

`파편화`란, 기기의 앱 구동 환경이 제각각 분열되어 있는 것을 이야기하는데, 크게 OS 측면의 파편화와, 하드웨어 측면의 파편화로 나눌 수 있다.

