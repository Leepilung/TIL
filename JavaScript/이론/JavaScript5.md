# 이터레이터와 제너레이터

이번에는 새로 도입된 ES6에서 새로 도입된 이터레이터와 제너레이터에 대해 살펴보자.

그리고 이런 지식을 바탕으로 향상된 컬렉션 구조를 자세히 살펴보자.

# For ..of 루프

For..of 루프는 이터러블 및 이터레이터 구조와 함께 ES6에 도입됐다. 이 새로운 루프 구조는 기존의 for ...in과 for...each 루프 구조를 대체한다.

for...of 루프는 반복 프로토콜을 지원하기 때문에 배열, 문자열, 맵, 세트 등과 같은 내장 객체 및 반복 가능한 사용자정의 객체에서 사용할 수 있다.

```js
const iter = ["a", "b"];
for (const i of iter) {
  console.log(i);
}
a;
b;
```

for...of 루프는 이터러블과 함께 동작하며 배열과 같은 내장 객체는 이터러블이다. 루프 변수를 정의할 때 var 대신 const를 사용했다. const를 사용하면 새로운 바인딩과 저장공간으로 새로운 변수가 만들어지기 때문에 좋은 방법이다.

블록 내에서 루프 변수의 값을 수정하지 않으려면 var 선언에 대해 for...of 루프와 함께 const를 사용해야 한다.

다른 컬렉션도 for..of 루프를 지원한다. 예를 들어 문자열은 유니코드 문장의 시퀀스이므로 for...of 루프는 잘 동작한다.

```js
for (let c of "String") {
  console.log(c);
}
S;
t;
r;
i;
n;
g;
```

for...in과 for...of 루프의 차이점은 for...in 루프는 객체의 모든 열거 가능한 속성을 반복한다는 것이다. 반면에 For...of 루프는 특정 목적을 가지고 있다. 객체가 이터러블 프로토콜을 정의하는 방법에 따라 반복 동작을 수행한다.

# 이터레이터와 이터러블

ES6는 데이터를 반복하는 새로운 매커니즘을 도입했다. ES6는 반복 구조를 개선시켰다.이 개선에는 두 가지 주요 개념, 즉 이터레이터와 이터러블이 포함된다.

## 이터레이터

자바스크립트 이러테이터는 next() 메소드를 제공하는 객체다. 이 메소드는 두 개의 속성(done과 value)을 가진 객체 형태로 컬렉션의 다음 항목을 반환한다. 다음 예제에서는 next() 메소드를 통해 배열의 이터레이터를 반환한다.

```js
// 배열을 받아 이터레이터를 반환

function iter(array) {
  var nextId = 0;
  return {
    next: function () {
      if (nextId < array.length) {
        return { value: array[nextId++], done: false };
      } else {
        return { done: true };
      }
    },
  };
}

var it = iter(["Hello", "Iterators"]);
console.log(it.next().value); // Hello
console.log(it.next().value); // Iterators
console.log(it.next().done); // true
```

위의 예제에서, 배열의 요소가 있는 동안 반복하면서 value와 done을 반환한다. 배열에서 반환할 요소가 없어지면 done을 true로 반환하여 반복이 더 이상 값을 갖지 않음을 나타낸다. 이터레이터에서 요소는 next() 메소드를 반복적으로 사용해 접근한다.

## 이터러블

이터러블은 반복 동작 또는 내부 반복을 정의하는 객체다. 이런 객체 ES6에서 도입된 for...of에서 사용될 수 있다. 배열과 문자열 같은 내장 유형은 디폴트 반복 동작을 정의하고 있다. 이터러블 객체의 경우, @@iterator 메소드를 구현해야 한다. 즉, 객체는 'Symbol.iterator'를 키로 갖는 속성을 가져야 한다.

객체는 키가 'Symbol.iterator'인 메소드를 구현하면 이터러블이 된다. 이 메소드는 next()메소드를 통해 이터레이터를 반환해야 한다. 다음 예제를 통해 이를 명확히 하자.

```js
// 이터러블 객체
// 1. 키가 'Symbol.iterator'인 메소드를 가지고 있는가?
// 2. 이 메소드는 'next' 메소드를 통해 이터레이터를 반환한다.
let iter = {
  0: "Hello",
  1: "World of",
  2: "Iterators",
  length: 3,
  [Symbol.iterator]() {
    let index = 0;
    return {
      next: () => {
        let value = this[index];
        let done = index >= this.length;
        index++;
        return { value, done };
      },
    };
  },
};
for (let i of iter) {
  console.log(i);
}
("Hello");
("World");
("Iterators");
```

이 예제를 더 작은 조각으로 나눠 보자. 우리는 지금 이터러블 객체를 생성하고 있다. 이미 익숙한 객체 리터럴 구문을 사용해 iter 객체를 생성한다. 이 객체의 특별한 것 중 하나는 [Symbol.iterator] 메소드다.

이 메소드 정의는 계산된 속성과 앞 장에서 이미 설명한 ES6 단축형 메소드 정의 구문을 조합해 사용한다. 이 객체에는 [Symbol.iterator] 메소드가 포함돼 있으므로 이 객체는 반복 가능하거나 또는 이터러블 프로토콜을 따른다. 또한 이 메서드는 next() 메소드를 통해 반복 동작을 정의하는 이터레이터 객체를 반환한다. 이제 이 객체는 for...of 루프와 함께 사용할 수 있다.

# 제너레이터

이터레이터와 이터러블과 밀접하게 연관된 제너레이터(generator)는 ES6의 기능 중 가장 많이 언급되고 있는 기능 중 하나이다. 제너레이터 함수는 제너레이터 객체를 반환한다. 이 용어는 처음에 다소 혼란스럽게 들릴 수 있다.

함수를 작성하면 함수의 동작을 이해할 수 있다. 함수는 한줄 한줄 실행되고, 마지막 줄이 실행되면 종료된다. 함수가 선형적으로 실행되면 함수에 따른 나머지 코드도 따라서 실행된다. 그러나 멀티 스레딩이 지원되는 언어에서, 이런 실행 흐름은 중단될 수 있고, 완료된 작업이 부분적으로 서로 다른 스레드, 프로세스 또는 채널 간 공유될 수 있다. 자바스크립트는 단일 스레드이므로 지금은 다중 스레드와 관련된 문제를 처리할 필요가 없다.

그러나 제너레이터 함수는 일시 중지됐다가 다시 시작할 수 있다. 여기서 중요한 부분은 제너레이터 함수 자체가 일시 중지를 선택하는 것이며 외부 코드에 의해서는 일시 중지될 수 없다는 점이다. 실행 중에 함수 yield 키워드를 사용해 일시 중지시킨다. 제너레이터 함수가 일시 중지되면, 함수 외부의 코드에 의해서만 다시 시작할 수 있다.

필요한 만큼 여러 번 제너레이터 함수를 일시 중지했다가 다시 시작할 수 있다. 제너레이터 함수에서 인기있는 패턴은 무한 루프를 작성하고 필요할 때 일시 중지시켰다가 다시 시작하는 것이다.

이해해야 할 또 다른 중요한 부분은 제너레이터 함수가 양방향 메시지 전달을 허용한다는 점이다. yield 키워드를 사용해 함수를 일시 중지할 때마다 메시지가 제너레이터 함수에서 전송되고, 함수가 다시 시작되면 제너레이터 함수로 메시지가 다시 전달된다.

예제를 통해 알아보자.

```js
function* generatorFunc() {
  console.log('1'); //---------> A
  yield; // ------------> B
  console.log('2'); // ------------> C
}
const generatorObj = generatorFunc();
console.log(generatorObj.next());
1
Object { value: undefined, done: false }
```

아주 간단한 제너레이터 함수 예라고 한다. 이해가 필요한 부분이 꽤있지만 말이다.

우선 function 키워드 바로 다음에 별표(\*)가 있음을 알 수 있다. 이것은 함수가 제너레이터 함수임을 나타내는 구문이다. 함수 이름 바로 앞에 별표를 두는 것도 괜찮다. 다음 두 코드는 모두 유효한 선언이다.

```js
function* f() {}
function* f() {}
```

함수 내에서 진짜 마술은 yield 키워드에서 일어난다고 보면 된다. yield 키워드를 만나면, 함수가 일시 중지된다. 더 진행하기 전에 함수가 어떻게 호출되는지 알아보자.

```js
function* generatorFunc() {
  console.log('1'); //---------> A
  yield; // ------------> B
  console.log('2'); // ------------> C
}
const generatorObj = generatorFunc();
generatorObj.next();
1
Object { value: undefined, done: false }
```

제너레이터 함수를 호출하면, 일반 함수처럼 실행되지 않고 제너레이터 객체를 반환한다. 이 제너레이터 객체를 사용해 제너레이터 함수의 실행을 제어할 수 있다. 제너레이터 객체의 next() 메소드는 함수의 실행을 다시 시작한다.

next()를 처음 호출하면 함수의 첫 번째 줄('A'로 표시)까지 실행이 진행되고, yield 키워드를 만나면 일시 중지된다. next() 함수를 다시 호출하면 실행이 중지된 지점에서 다음 줄로 실행이 재개된다.

```js
function* generatorFunc() {
  console.log('1'); //---------> A
  yield; // ------------> B
  console.log('2'); // ------------> C
}
console.log(generatorObj.next());
2
Object { value: undefined, done: true }
```

함수 본문 전체가 실행되면, 제너레이터 객체에서 next()를 호출해도 아무 효과가 없다. 앞에서 제너레이터 함수는 양방향 메시지 전달을 허용한다고 했다. 어떻게 동작할까? 앞의 예에서 제너레이터 함수를 다시 시작할때마다 done과 value의 두값을 가진 객체를 받는다. 에제의 경우, 값(value)로 undefined를 받았다. 이는 yield 키워드로 어떤 값도 반환하지 않기 때문이다. yield 키워드를 사용하여 값을 반환하면 호출하는 함수가 이를 받는다.

```js
function* logger() {
  console.log("start");
  console.log(yield);
  console.log(yield);
  console.log(yield);
  return "end";
}

var genObj = logger();
// next의 첫 번째 호출은 함수의 시작부터 첫 번째 yield문까지 진행된다.

console.log(genObj.next());
//start , Object { value: undefined, done: false } 출력

console.log(genObj.next("Save"));
// Save , Object { value: undefined, done: false } 출력

console.log(genObj.next("Our"));
// Our , Object { value: undefined, done: false } 출력

console.log(genObj.next("Souls"));
// Souls , Object { value: "end", done: true } 출력
```

이 예제의 실행 흐름을 단계별로 추적해 보자. 제너레이터 함수는 세 개의 일시 중지(yield)를 가지고 있다. 다음과 같은 줄을 작성하여 제너레이터 객체를 생성할 수 있다.

```js
var genObj = logger();
```

next 메소드를 호출해 제너레이터 함수의 실행을 시작한다. 이 메소드는 첫 번째 yield까지 실행을 시작한다. 첫 번째 호출에서 next()메소드에 값을 전달하지 않았다.

이 next() 메소드의 목적은 제너레이터 함수를 시작하는 것이다. next() 메소드를 다시 호출하면서, 이번에는 "Save" 값을 매개변수로 전달한다. 이 값은 실행이 다시 시작될 때 yield에 의해 수신되며 콘솔에 값이 출력되는 것을 볼 수 있다.

```js
Save , Object { value: undefined, done: false }
```

next() 메소드를 두 개의 다른 값으로 다시 호출하면 출력은 앞의 코드와 비슷하다. 마지막으로 next() 메소드를 호출하면, 실행이 끝나고 제너레이터 함수는 호출하 코드에 end 값을 반환한다.
실행이 끝나면 done은 true로 설정되고, value에는 함수에서 반환된 값, 즉 end가 지정된다.

```js
Souls , Object { value: "end", done: true }
```

첫 번째 next() 메소드의 목적은 제너레이터 함수의 실행을 시작하는 것이다. 이 함순는 첫 번째 yield 키워드로 이동하므로 첫 번째 next() 메소드에 전달된 값은 무시된다.

지금까지의 논의에서, 제너레이터 객체가 이터레이터 규약을 준수한다는 것을 알 수 있다. 그렇다면 예제를 통해 이를 한번 확인해 보자.

```js
function* logger() {
  yield "a";
  yield "b";
}

var genObj = logger();
// 제너레이터 객체는 제너레이터 함수를 사용하여 작성된다.

console.log(typeof genObj[Symbol.iterator] === "function"); // true 출력
// 이터러블

console.log(typeof genObj.next === "function"); // true 출력
// 이터레이터 (next() 메소드를 가짐)

function* logger() {
  yield "a";
  yield "b";
}

var genObj = logger();
// 제너레이터 객체는 제너레이터 함수를 사용하여 작성된다.

console.log(typeof genObj[Symbol.iterator] === "function"); // true 출력
// 이터러블

console.log(typeof genObj.next === "function"); // true 출력
// 이터레이터 (next() 메소드를 가짐)
```

위의 예제는 제너레이터 함수가 이터러블 규약을 준수함을 확인시켜 준다.

## 제너레이터 반복

제너레이터는 이터레이터며 이터러블을 지원하는 모든 ES6 구조와 마찬가지로 제너레이터를 반복하는 데 사용할 수 있다.

첫 번째 방법은 for ...of 루프를 사용하는 것이다.

```js
function* logger() {
  yield "a";
  yield "b";
}

for (const i of logger()) {
  console.log(i);
}
a;
b;
```

여기선 제너레이터 객체를 생성하지 않는다. For...of 루프는 이터러블을 지원하고 제너레이터는 자연스럽게 이 루프에 들어간다.

스프레드연산자를 사용해 이터러블을 배열로 바꿀 수 있다. 다음 예제를 보자.

```js
function* logger() {
  yield "a";
  yield "b";
}

const arr = [...logger()];
console.log(arr);
Array[("a", "b")];
```

마지막으로 다음과 같이 제너레이터에 디스트럭처링 구문을 사용할 수 있다.

```js
function* logger() {
  yield 'a'
  yield 'b'
}

const [x,y] = logger()
console.log(x,y)
a b
```

제너레이터는 비동기 프로그래밍에서 중요한 역할을 한다. 또한 제너레이터는 협업 멀티 태스킹 함수를 작성하는 데에도 도움이 된다.

# 컬렉션

ES6는 Map과 WeakMap, Set, WeakSet의 네 가지 데이터 구조를 도입했다. 자바스크립트는 파이썬, 루비등과 비교해서 해시(hash)나 맵(map) 데이터 구조 또는 딕셔너리(dictionary)를 지원하는 표준 라이브러리가 빈약하다.

문자열 키를 객체와 매핑해 Map의 동작을 구현하는 몇 가지 해킹 방법이 개발됐으나 이런 해킹에는 부작용이 생겼다. 따라서 이런 데이터 구조에 대한 언어 지원이 절실히 요구돼었기 때문에 ES6에서는 표준 딕셔너리 데이터 구조를 지원한다.

## 맵(Map)

Map은 임의의 값을 key로 허용한다. keys는 값에 매핑된다. 맵을 사용하면 값에 빠르게 접근할 수 있따.

```js
const m = new Map(); // 빈 맵을 생성
m.set("first", 1); // 키와 관련된 값 설정
console.log(m.get("first")); // 키를 사용해 값을 가져온다
1;
```

생성자(constructor)를 사용하여 빈 Map을 생성한다. set() 메소드를 사용해 Map에 키와 연관된 값의 항목을 추가하고 기존 항목을 동일한 키로 겹쳐 쓸 수 있다. 이와 반대되는 메소드인 get()은 키와 연관된 값을 가져오고, 맵에 해당 항목이 없으면 undefined를 가져온다.

다음과 같이 맵에서 사용할 수 있는 다른 헬퍼 메소드도 있다.

```js
console.log(m.has("first")); // 키가 있는지 검사한다
// true 출력
m.delete("first");
console.log(m.has("first")); // false 출력

m.set("foo", 1);
m.set("bar", 0);

// Map { foo → 1, bar → 0 } 출력

console.log(m.size); // 2 출력
m.clear(); // 전체 맵을 지운다.
console.log(m.size); // 0 출력
```

다음 이터러블 [키,값] 쌍을 이용하여 Map을 생성할 수 있다.

```js
const m2 = new Map([
  [1, "one"],
  [2, "two"],
  [3, "three"],
]);
```

그리고 다음과 같이 구문에 set() 메소드를 연결할 수 있다.

```js
const m3 = new Map().set(1, "one").set(2, "two").set(3, "three");
```

모든 값을 키로 사용할 수 있다. 객체의 경우, 문자열만 키가 될 수 있지만, 컬렉션의 경우 이 제한이 없어졌다. 객체를 키로 사용할 수도 있지만 그다지 사용되는 방법은 아니다.

```js
const obj = {};
const m2 = new Map([
  [1, "one"],
  ["two", "two"],
  [obj, "three"],
]);

console.log(m2.has(obj));
true;
```

## 맵 반복

기억해야할 중요한 점 중 하나는 맵에서 순서가 중요하다는 점이다. 맵은 요소가 추가된 순서가 유지된다.

Map을 반복할 때는 keys, values, entries, 이렇게 세 가지 이터러블을 사용할 수 있다.

keys() 메소드는 다음과 같이 Map의 키에 대한 이터러블을 반환한다.

```js
const m = new Map([
  [1, "one"],
  [2, "two"],
  [3, "three"],
]);

for (const k of m.keys()) {
  console.log(k);
}
1;
2;
3;
```

마찬가지로 values() 메소드는 다음 예제와 같이, Map의 값에 대한 이터러블을 반환한다.

```js
const m = new Map([
  [1, "one"],
  [2, "two"],
  [3, "three"],
]);

for (const v of m.values()) {
  console.log(v);
}
one;
two;
three;
```

entries() 메소드는 다음 코드에서 볼 수 있듯, [키, 값] 쌍의 형식으로 Map의 항목을 반환한다.

```js
const m = new Map ([
  [ 1 , 'one' ],
  [ 2, 'two' ],
  [ 3 , 'three' ],
]);

for (const entry of m.entries()) {
  console.log(entry[0], entry[1]);
}
1 one
2 two
3 three
```

위의 예제는 더 간결하게 만들 수 있다.

```js
const m = new Map ([
  [ 1 , 'one' ],
  [ 2, 'two' ],
  [ 3 , 'three' ],
]);

for (const [key, value] of m.entries()) {
  console.log(key, value);
}
1 one
2 two
3 three
```

더 더욱 간단하게도 가능하다.

```js
const m = new Map ([
  [ 1 , 'one' ],
  [ 2, 'two' ],
  [ 3 , 'three' ],
]);

for (const [key, value] of m) {
  console.log(key, value);
}
1 one
2 two
3 three
```

## 맵을 배열로 변환

스프레드 연산자(...)는 Map을 배열로 변환하려는 경우 편리하다.

```js
const m = new Map([
  [1, "one"],
  [2, "two"],
  [3, "three"],
]);

const keys = [...m.keys()];
console.log(keys)[(1, 2, 3)];
```

맵은 이터러블이므로, 스프레드 연산자를 사용하여 전체 Map을 배열로변환할 수 있다.

```js
const m = new Map([
  [1, "one"],
  [2, "two"],
  [3, "three"],
]);

const arr = [...m];
console.log(arr);

Array(3)[[1, "one"][(2, "two")][(3, "three")]];
```

## 세트

Set은 값의 모음이다. 세트에서 값을 추가하고 제거할 수 있다. 배열과 비슷해 보이지만, 세트는 같은 값을 두번 허용하지 않는다. set의 값은 어떤 유형도 가능하다.

배열과는 얼마나 다를까? Set은 멤버쉽 테스트를 신속하게 수행할 수 있도록 설계됐다. 이 작업을 수행하는 데 있어서 배열은 상대적으로 느리다. Set 동작은 Map 동작과 비슷하다.

```js
const s = new Set();
s.add("first");
s.has("first"); // true
s.delete("first"); // ture
s.has("first"); // false
```

맵과 마찬가지로 이터레이터를 통해 Set을 생성할 수 있다.

```js
const colors = new Set(["red", "white", "blue"]);
```

Set에 값을 추가할 때, 값이 이미 존재하면 아무 일도 일어나지 않는다. 마찬가지로 Set에서 값을 삭제할 때, 값이 존재하지 않으면 아무 일도 일어나지 않는다.

# WeakMap과 WeekSet

Weakmap과 WeakSet은 Map과 Set과 비슷하지만 제한된 API를 가진다. 그리고 각각 비슷하게 동작한다.하지만 몇 가지 차이점이 있다.

- WeakMap은 new와 has(), get(), set(), delete() 메소드만 지원한다.
- WeakSet은 new와 has(), add(), and delete()만 지원한다.
- WeakMap의 키는 반드시 객체여야 한다.
- WeakSet의 값은 반드시 객체여야 한다.
- WeakMap을 반복할 수는 없다. 값에 접근할 수 있는 유일한 방법은 키를 사용하는 것이다.
- WeakSet을 반복할 수 없다.
- WeakMap이나 WeakSet을 지울 수 없다.

WeakMap을 먼저 이해해 보자. Map과 WeakMap의 차이점은 WeakMap 자체가 가비지 컬렉션(garbage collection)을 허용한다는 것이다. WeakMap의 키는 약하게 유지된다. WeakMap 키는 가비지 컬렉터가 참조 카운트를 수행할 때 캉운트되지 않으며, 가능한 경우에 가비지 처리된다.

WeakMap은 맵에 보관중인 객체의 수명주기에 대해 어떤 제어도 하지 못할 때 유용하다.
WeakMap을 사용할 때, 수명주기가 길더라도 객체가 메모리를 점유하지 않기 때문에 메모리 누출에 대해 걱정할 필요가 없다.

WeakSet에도 동일한 구현 세부사항이 적용된다. 그러나 WeakSet을 반복할 수 없으므로, WeakSet의 유즈 케이스는 많지 않다.

또한 ES6 컬렉션에 새롭게 추가된 Maps와 Sets, WeakMaps, WeakSets들은 모두 추가 이터레이터 메소드인 .entries()와 .values(), .keys()를 가진다.
