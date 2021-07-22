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
