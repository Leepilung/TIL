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
