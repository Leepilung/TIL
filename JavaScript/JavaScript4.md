# JavaScript 4

## 내장 객체

앞에서 Object() 생성자 함수를 살펴봤다. 객체 리터럴 표기법을 사용해 객체를 생성하고 해당 constructor 속성에 접근할 때 반환된다. Object()는 내장된 생성자 중 하나다.

내장 객체는 세 그룹으로 나눌 수 있다.

- 데이터 랩퍼 객체 : Object, Array, Function, Boolean, Number, String등이 있다. 이들 객체는 자바스크립트에서 각각의 데이터 유형에 해당된다. Undefined와 null을 제외하고는 typeof 값에 대한 데이터 래퍼 객체가 있다.

- 유틸리티객체 : Math, Date, RegExp등이 있으며 편리하게 사용할 수 있다.

- 오류 객체 : 일반적인 Error 객체뿐만 아니라 예기치 않은 상황이 발생할 때 프로그램이 동작 상태를 복구하는데 도움디 되는 여러 특정 객체가 포함된다.

# Object

Object는 모든 자바스크립트 객체들의 부모다. 즉 생성한 모든 객체는 여기서 상속됐음을 의미한다. 새로운 빈 객체를 생성하려면, 리터럴 표기법이나 Object() 생성자 함수를 사용한다.

```js
var o = {};
var o = new Object();
```

위의 두 줄은 동일하다. 위에서 언급했듯이 빈 객체는 이미 여러 상속된 메소드와 속성을 가지고 있기 때문에 바로 사용이 가능하다. 여기서 빈 객체라는 것은 `{ }` 같은 객체로, 자동으로 받은 것 이외의 자체 속성을 가지지 않는 객체를 의미한다.

- o.constructor 속성은 생성자 함수의 참조를 반환한다.
- o.toString()은 객체를 표현하는 문자열을 반환하는 메소드다.
- o.valueOf()은 객체의 단일 값 표현을 반환한다. 이것은 종종 객체 자체로 취급된다.

메소드들의 실제 동작을 살펴보자. 우선 객체를 생성한다.

```
var a = new Object();
```

그 다음 toString()을 호출하면 객체의 문자열 표현식이 반환된다.

```js
a.toString();
("[object Object]");
```

toString() 메소드는 객체가 문자열 컨텍스트에서 사용될 때 자바스크립트에 의해 내부적으로 호출된다. 예를 들어 alert()는 문자열에서만 동작하므로 alert()함수를 호출할 때 객체를 전달하면, toString() 메소드가 자동으로 호출된다.

그렇기 때문에 다음 두 줄의 결과는 동일하다.

```js
alert(a); // [object Object]
alert(a.toString()); // [object Object]
```

문자열 컨텍스트의 또 다른 유형은 문자열 연결이다. 객체를 문자열과 연결하려고 하면 객체의 toString() 메소드가 먼저 호출된다.

```js
"An obejct" + o;
("An obejct[object Object]");
```

valueof() 메소드는 모든 객체가 제공하는 메소드 중 하나다. 생성자가 Object()인 단순 객체인 경우, valueof() 메소드는 객체 자체를 반환한다.

```js
o.valueOf() === o;
true;
```

요약하면 다음과 같다.

- var o = {}; 또는 var o = new Object();로 객체를 생성할 수 있다.
- 아무리 복잡한 객체더라도 Object 객체를 상속하므로 toString() 같은 메소드와 constructor 같은 속성을 제공한다.

## Array

Array()는 배열을 생성할 때 사용할 수 있는 내장 함수다.

```js
var a = new Array();
```

이것은 배열 리터럴 표기법과 동일하다.

```js
var a = [];
```

배열이 어떻게 생성됐던 평소와 같이 요소를 추가할 수 있다.

```js
var a = [];
a[0] = 1;
a[1] = 2;
a;
Array[(1, 2)];
```

Array() 생성자를 사용할 때, 새로운 배열의 요소에 할당될 값을 전달할 수도 있다.

```js
var a = new Array(1, 2, 3, "four");
a;
Array(4)[(1, 2, 3, "four")];
```

예외의 경우가 있는데 바로 생성자에 하나의 숫자를 전달할 때다. 이 경우, 숫자는 배열의 길이로 간주된다.

```js
var a2 = new Array(5);
a2;
Array(5) [ <5 empty slots> ]
```

생성자를 사용해 배열을 생성했으므로, 배열은 객체가 되는가? -> 맞다.
Typeof 연산자를 이용하면 확인할 수 있다.

```js
typeof [1, 2, 3];
("object");
```

배열은 객체이므로 부모 객체의 속성과 메소드를 상속받을 수 있다.

```js
var a = [1,2,3, 'four'];
a.toString();
"1,2,3,four"
a.valueOf();
Array(4) [ 1, 2, 3, "four" ]
a.constructor();
Array []
```

배열은 객체이지만, 다음과 같은 이유로 특별한 유형이다.

- 속성의 이름은 0부터 시작하는 숫자를 사용하여 자동 지정된다.
- 배열의 요소 개수를 담고 있는 length 속성이 있다.
- 부모 객체에서 상속된 메소드 이외에 더 많은 내장 메소드를 가지고 있다.

빈 배열 a와 빈 객체 o를 생성하는 것으로 시작하여 배열과 객체의 차이점을 살펴보겠다.

```js
var a = [],
  o = {};

a.length;
0;
typeof o.length;
("undefined");
```

배열과 객체 모두 숫자 및 비숫자 속성을 추가할 수 있다.

```js
a[0] = 1;
o[0] = 1;
a.prop = 2;
o.prop = 2;
```

length 속성은 숫자 속성의 수를 항상 최신 상태로 유지하지만, 숫자가 아닌 속성은 무시한다.

```js
a.length;
1;
```

length 속성은 사용자가 설정할 수도 있다. 배열의 현재 항목 수보다 큰 값으로 설정하면 추가 요소를 위한 공간이 마련된다. 또한 이러한 존재하지 않는 공간에 접근하려고 하면 undefined 값이 반환된다.

```js
a.length =5;
5
a;
[1,undefined x 4]
```

반면 length 속성을 더 작은 값으로 설정하면 뒤에 있는 요소가 제거된다.

```js
a.length = 2;
2
a;
[1, undefined x 1]
```

## 몇 가지 배열 메소드

배열 객체는 부모 객체에서 상속된 메소드 외에도 sort(), join() , slice() 등과 같이 배열 작업을 위한 특별한 메소드를 가지고 있다.

우선 `push()` 메소드는 배열의 끝에 새로운 요소를 추가한다. `pop()` 메소드는 마지막 요소를 제거한다. a.push('new') 메소드는 a[a.length] = 'new'와 같이 동작하고, a.pop()은 a.length--와 같이 동작한다.

`push()`메소드는 변경된 배열의 길이를 반환하고, `pop()`은 제거된 요소를 반환한다.

```js
var a = [3, 5, 1, 7, "test"];
a.push("new");
6;
a;
Array(6)[(3, 5, 1, 7, "test", "new")];
a.pop();
("new");
a;
Array(5)[(3, 5, 1, 7, "test")];
```

`sort()` 메소드는 배열을 정렬하고 이를 반환한다.

```js
var b = a.sort();
b;
Array(5)[(1, 3, 5, 7, "test")];
a === b;
true;
```

`join()` 메소드는 join()에 전달된 문자열 매개변수를 함께 묶어 배열의 모든 요소 값을 포함하는 문자열을 반환한다.

```js
a.join(" is not ");
("1 is not 3 is not 5 is not 7 is not test");
```

`slice()`메소드는 소스 배열을 수정하지 않고 배열의 일부분을 반환한다. slice()의 첫번째 매개변수는 시작 인덱스이고, 두 번째 매개변수는 끝 인덱스이다.

시작 인덱스의 요소는 포함되지만, 끝은 포함되지 않는다.

```js
b = a.slice(1, 3);
Array[(3, 5)];
b = a.slice(0, 1);
Array[1];
b = a.slice(0, 2);
Array[(1, 3)];
```

슬라이스가 끝난 후에도, 소스 배열은 변하지 않는다.

```js
a;
Array(5)[(1, 3, 5, 7, "test")];
```

slice() 메소드는 소스 배열을 수정한다. 슬라이스를 제거하여 반환하고, 선택적으로 간격을 새로운 요소로 채울 수 있다.

처음 두 매개변수는 제거할 슬라이스의 시작 인덱스와 길이를 정의한다. 그 뒤 매개변수들은 채울 새 값을 전달한다.

```js
b = a.splice(1, 2, 100, 101, 102);
Array[(3, 5)];
a;
Array(7)[(1, 100, 101, 102, 102, 7, "test")];
```

물론 간격을 채우는 것은 선택사항이므로 다음과 같이 건너 뛸 수 있다.

```js
a.splice(1, 3);
Array(3)[(100, 101, 102)];
a;
Array(3)[(1, 7, "test")];
```

## Array.form

Array.form()은 유사 배열 객체(array-like object)나 반복 가능한 객체(iterable object)를 얕게 복사해 새로운Array 객체를 만든다.

```js
console.log(Array.from("foo"));
// expected output: Array ["f", "o", "o"]

console.log(Array.from([1, 2, 3], (x) => x + x));
// expected output: Array [2, 4, 6]
```

## Array.of

Array() 생성자를 사용해 배열을 생성하면 문제가 발생한다. 생성자는 인수의 수와 유형에 따라 다르게 동작한다.

Array()생성자에 단일 숫자 값을 전달하면, 인수 값이 length 값으로 할당된 배열의 요소가 정의되지 않은 배열이 생성된다.

```js
let arr = new Array(2);
console.log(arr); // [undefined, undefined]
console.log(arr.length); // 2
```

또한 숫자가 아닌 값을 하나만 전달하면 배열의 유일한 항목이 된다.

```js
let arr = new Array("2");
console.log(arr); // ['2']
console.log(arr.length); // 1
```

따라서 배열을 생성할때 혼란을 피하기 위한 더 좋은 방법이 Array.of이다.

Array.of()와 Array 생성자의 차이는 정수형 인자의 처리 방법에 있다.

```js
Array.of(7); // [7]
Array.of(1, 2, 3); // [1, 2, 3]

Array(7); // [ , , , , , , ]
Array(1, 2, 3); // [1, 2, 3]
```

Array.of는 숫자와 유형에 상관없이 인수로 배열을 생성한다는 것을 기억하자.

## Array.prototype 메소드

배열 반복과 배열의 요소 검색에 도움이 되는 메소드들이 있다.

- Array.prototype.entires()
- Array.prototype.values()
- Array.prototype.keys()

위 3개의 메소드는 모두 이터레이터를 반환한다. 이 이터레이터는 Array.form()을 사용해 배열을 생성하는데 사용할 수 있으며 반복을 위한 for 루프에서 사용할 수 있다.

```js
let arr = ["a", "b", "c"];
for (const index of arr.keys()) {
  console.log(index); // 0, 1, 2 출력
}

for (const value of arr.values()) {
  console.log(value); // a, b, c 출력
}

for (const [index, value] of arr.entries()) {
  console.log(index, value); // 0 a, 1 b, 2 c 출력
}
```

그리고 배열안을 검색하는 새로운 메소드도 있다.

- Array.prototype.find
- Array.prototype.findindex

이 메소드는 모두 두 개의 인수를 허용한다. 첫 번째는 callback 함수이고 두 번째는 선택사항인 this 키워드다.
callback은 배열요소, 해당 요소의 인덱스 및 배열의 세 개의 인수를 받는다. 요소가 조건과 일치하면 callback은 true를 반환한다.

```js
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(numbers.find((n) => n > 5)); // 6
console.log(numbers.findIndex((n) => n > 5)); // 5
```

# Function

함수는 객체이다. Function()이라는 내장 생성자 함수가 있으며 이는 함수를 생성하는 대체 방법으로 사용될 수 있다.
다음은 함수를 정의하는 예제들이다.

```js
function sum(a, b) {
  // 함수 선언
  return a + b;
}
sum(1, 2);
3;
var sum = function (a, b) {
  // 함수 표현식
  return a + b;
};
sum(1, 3);
4;

var sum = new Function("a", "b", "return a + b;");
sum(1, 4);
5;
```

Function() 생성자를 사용할 때는 먼저 매개변수 이름을 문자열로 전달한 다음 함수 본문의 소스 코드를 문자열로 전달한다. 그러나 이 소스 코드 평가는 eval() 함수와 동일한 단점을 지니고 있어 가능하면 피ㅏ하는 것이 좋다.

## 함수 객체의 속성

함수는 Function() 생성자 함수에 대한 참조를 가진 constructor 속성이 있다.

```js
function myfunc(a) {
  return a;
}
myfunc.constructor;
function Function()
```

함수는 또한 length 속성을 가진다. 이 속성은 함수가 원하는 공식 매개변수의 수를 가진다.

```js
function myfunc(a, b, c) {
  return true;
}

myfunc.length;
3;
```

## prototype 속성 사용하기

함수 객체에서 가장 널리 사용되는 속성 중 하나는 prototype 속성이다. 나중에 다시 다룰 내용이기 때문에 가볍게만 알아보자면

- function 객체의 prototype 속성은 다른 객체를 가리킨다.
- 이 function을 생성자로 사용할 때만 이점이 빛을 발한다.
- 이 function으로 생성된 모든 객체는 prototype 속성에 대한 참조를 유지하며 해당 속성을 자체 속성으로 사용할 수 있다.

prototype 속성을 보여주는 간단한 예제를 살펴보자. name 속성 이름과 say() 메소드를 가진 간단한 객체를 사용할 것이다.

```js
var ninja = {
  name : 'Ninja'
  say : function () {
    return 'I am a ' + this.name;
  }
};
```

함수를 생성하면 (본문이 없는 함수더라도), 새로운 객체를 가리키는 prototype 속성이 자동으로 생김을 확인할 수 있다.

```js
function F() {}

typeof F.prototype;
("object");
```

prototype 속성은 수정이 흥미롭다. 속성을 추가하거나 디폴트 객체를 다른 객체로 변경할 수 있다. prototype에 ninja를 지정해 보자.

```js
F.prototype = ninja;
```

이제 F() 함수를 constuctor 함수로 사용하면 F.prototype의 속성을 자신의 속성처럼 접근할 수 있는 새로운 객체 baby_ninja를 생성하여 실행시켜보면 다음과 같은 결과를 가진다.

```js
var baby_ninja = new F();
baby_ninja.name;
("Ninja");
baby_ninja.say();
("I am a Ninja");
```

## 함수 객체의 메소드

최상위 부모 객체의 자손인 Function 객체는 toString()같은 디폴트 메소드를 가져온다. 함수에서 호출될 때 toString() 메소드는 함수의 소스 코드를 반환한다.

```js
function myfunc(a, b, c) {
  return a + b + c;
}
myfunc.toString();
"function myfunc(a, b, c) {
  return a + b + c;
}"
```

내장 함수의 소스 코드를 들여다보면 함수 본문 대신 [native code] 문자열이 반환된다.

```js
parseInt.toString();
"function parseInt() {
    [native code]
}"
```

보다시피 toString()을 사용하면 개발자가 정의한 메소드와 내가 정의한 메소드를 구별할 수 있다.

## call & apply

함수 객체는 `call()`과 `apply()` 메소드를 가진다. 이런 메소드를 사용하면 함수를 호출할 때 인수를 전달할 수 있다.

또한 이 메소드를 사용하면 다른 객체의 메소드를 빌려서 자신의 메소드인 것처럼 호출할 수 있다. 코드를 재사용하는 쉽고 좋은 방법이다.\

예들 들어 say() 메소드를 포함한 some_obj 객체가 있다고 가정해 보자.

```js
var some_obj = {
  name: "Ninja",
  say: function (who) {
    return "Haya " + who + ", I am " + this.name;
  },
};
```

say() 메소드를 호출해 자신의 name속성에 접근할 수 있다. 이 메소드는 내부적으로 this.name을 사용하는 것이다.

```js
some_obj.say("Dude");
("Haya Dude, I am Ninja");
```

이제 name속성만 갖는 간단한 객체 my_obj를 생성해 보자.

```js
var my_obj = { name: "Scripting Guru" };
```

my_obj는 some_obj 객체의 say() 메소드가 너무 좋아 자신의 메소드처럼 호출하고 싶다고 가정해보자. 이럴땐 say() 함수 객체의 call() 메소드를 사용하면 가능하다.

```js
some_obj.say.call(my_obj, "Jude");
("Haya Jude, I am Scripting Guru");
```

잘 동작하지만 동작 방법을 자세히 살펴볼 필요가 있다. my_obj 객체와 Jude 문자열 두 매개변수를 전달하여 say()함수 객체의 call() 메소드를 호출했다.

결과는 say().가 호출될 때, this값에 대한 참조가 my_obj를 가르킨다는 것이다. 이렇게 하면 this.name이 Ninja가 아닌 my_obj의 Scripting guru를 반환한다.

call() 메소드를 호출할 때, 더 많은 매개변수를 전달하려면 이들을 추가하면 된다.

```js
some_obj.say.call(my_obj, "a", "b", "c");
("Haya a, I am Scripting Guru");
```

call()에 첫 번째 매개변수로 객체를 전달하지 않거나 null을 전달하면, 전역 객체로 가정한다.

apply() 메소드는 call()과 같은 방식으로 동작하지만, 다른 객체의 메소드로 전달할 모든 매개변수가 배열로 전달된다는 차이점이 있다.

```js
some_obj.someMethod.apply(my_obj, ["a", "b", "c"]);
some_obj.someMethod.call(my_obj, "a", "b", "c");
```

위의 두 줄은 서로 동일하다.

## 인수 객체 재검토

앞에서 함수에 전달된 모든 매개변수의 값을 포함하고 있는 arguments에 접근하는 방법을 알아봤다.

```js
function f() {
  return arguments;
}
f(1,2,3);
Arguments { 0: 1, 1: 2, 2: 3, … }
```

arguments는 배열처럼 보이지만, 실제로는 배열과 비슷한 객체이다. 인덱스된 요소와 length 속성을 포함하고 있으므로 배열과 유사하다. 그러나 유사성은 여기까지다. 인수는 sort() 또는 slice() 같은 배열 메소드를 제공하지 않는다.

그러나 arguments를 배열로 변환할 수 있으며, 배열의 모든 이점을 활용할 수 있다.

```js
function f() {
  var args = [].slice.call(arguments);
  return args.reverse();
}

f(1, 2, 3, 4);
Array(4)[(4, 3, 2, 1)];
```
