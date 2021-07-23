# JavaScript 6

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
