# JavaScript 문법류 요약, 정리파트

자바스크립트를 공부하면서 실제 사용되는 Event나 메소드등을 정리해두려고 만든 문서입니다.

## addEventListener

특정 이벤트가 발생했을 시, 특정 함수를 실행할 수 있게 해주는 기능.

자주 쓰이는 이벤트 목록들

- change : 변동이 있을 때 발생
- click : 클릭 시 발생
- focus : 포커스를 얻었을 때 발생
- keydown : 키를 눌렀을 때 발생
- keyup : 키에서 손을 땟을 때 발생
- load : 로드가 완료 되었을 때 발생
- mousedown : 마우스를 클릭 했을 때 발생
- mouseout : 마우스가 특정 객체 밖으로 나갔을 때 발생
- mouseover : 마우스가 특정 객체 위로 올려졌을 때 발생
- mousemove : 마우스가 움직였을 때 발생
- mouseup : 마우스에서 손을 땟을 때 발생
- select : ption 태그 등에서 선택을 햇을 때 발생

```js
Ex)
element.addEventListener('click', doSomething, false);
```

예시로 1번째 인자('click')는 `이벤트명`을 의미한다.
2번째 인자(doSomething)는 `콜백 함수로, 이벤트가 발생`되면 실행된다.
3번째 인자(false)는 `useCapture` 라고 불리는 부울린 값으로, 이벤트 버블링이나 캡쳐링을 사용할것인지 나타낸다.

```js
element.addEventListener("click", doSomething, {
  capture: false,

  once: true,

  passive: false,
});
```

3번째 인자는 각기 다른 3개의 속성으로 한정되어있다.

- capture - 부울린. 위에 언급된 useCapture 와 동일한 인자.
- once - 부울린. true 면 이벤트가 딱 한번만 발생됨.
- passive - 부울린. true 면 콜백 함수내부에 preventDefault() 가 있다 하더라도 실행되지 않음.

https://developer.mozilla.org/ko/docs/Web/API/EventTarget/addEventListener

# .attr()과 .prop()

## .attr()과 .prop()의 차이점

- .attr()은 HTML의 속성을 취급한다
- .prop()는 JavaScript 프로퍼티를 취급한다.

> 여기서 attr에서 언급한 속성이란?

    속성은 HTML 요소에 대한 추가 정보를 전달하며 name="value"쌍으로 제공된다. HTML 요소의 속성을 설정하고 소스 코드를 작성하는 동안 HTML 요소를 정의 할 수 있다.

간단한 예를 들자면

```html
<input id="hanq" type="text" value="java" />
```

여기서 "type", "value", "id"는 입력 요소의 속성이다.

> 반대로 프로퍼티란?

    프로퍼티는 HTML DOM 트리의 특성을 나타낸다.  브라우저가 사용자의 HTML 코드를 파싱하면 해당 DOM 노드가 생성되어 객체가되므로 프로퍼티가 있다. 위의 예제의 경우 브라우저가 입력을 렌더링하면 align, alt, autofocus, baseURI 등의 다른 속성이 추가된다.

    attr()은 요소의 현재 상태의 원래 값을 제공하므로 javascript / jquery를 통해 수정 된 요소의 값을 가져 오는 데에는 prop()를 사용한다.

.prop()는 지정한 선택자를 가진 첫번째 요소의 속성값을 가져오거나 속성값을 추가한다. HTML 입장에서의 속성(attribute)가 아닌 JavaSCript 입장에서의 속성(property)이다.

예제 모음

> prop1

```js
.prop( propertyName )
// 속성값을 가져온다
```

> prop2

```js
.prop( propertyName, value )
// 속성값을 추가한다.
```

> Style

```css
<input style="font:arial;"/>
```

- .attr('style') = 일치된 요소에 대해 인라인 스타일을 반환한다. ("font:arial;")
- .prop('style') = 스타일 선언 객체를 반환한다.(CSSStyleDeclaration)

> Value

```js
<input value="hello" type="text" />;

$("input").prop("value", "i changed the value");
```

- .attr('value') = 'hello' 반환
- .prop('value') - 'i changed the value' 반환

하지만 value를 getter/setting 하기에는 .val() 메서드가 낫다.

> 체크박스

<input id="hanq" type="checkbox" checked /> 체크박스를 클릭해주세요

<script>
var $checkbox = $('#hanq');

$($checkbox).on('change', function() {
  alert($checkbox.attr('checked'));
  // checked속성의 값을 표시 → "checked"
  alert($checkbox.prop('checked'));
  // checked프로파티값을 표시 → true / false
});
</script>

```js
alert($checkbox.attr("checked"));
// checked속성의 값을 표시 → "checked"
alert($checkbox.prop("checked"));
// checked프로파티값을 표시 → true / false
```

다음과 같이 작동한다.

> 특징

- attr() - HTML attribute 값이 모두 String 으로 넘어온다.
- prop() - 자바스크립트의 프로퍼티 값이 넘어오기 때문에 boolean, date, function 등도 가져올 수 있다
- .prop()는 .attr() 보다 약 2.5 배 빠르다

# reduce()

reduce() 메서드는 배열의 각 요소에 대해 주어진 리듀서(reducer) 함수를 실행하고, 하나의 결과값을 반환한다.

```js
const array1 = [1, 2, 3, 4];
const reducer = (accumulator, currentValue) => accumulator + currentValue;

// 1 + 2 + 3 + 4
console.log(array1.reduce(reducer));
// expected output: 10

// 5 + 1 + 2 + 3 + 4
console.log(array1.reduce(reducer, 5));
// expected output: 15
```

리듀서 함수는 네 개의 인수를 가진다.

1. 누산기 = accumulator (acc)
2. 현재 값 (cur)
3. 현재 인덱스 (idx)
4. 원본 배열 (src)
   리듀서 함수의 반환 값은 누산기에 할당되고, 누산기는 순회 중 유지되므로 결국 최종 결과는 하나의 값이 된다.

> 구문

```js
arr.reduce(callback[, initialValue])
```

## 매개변수

- `callback`
  배열의 각 요소에 대해 실행할 함수가 들어간다. 다음 네 가지의 인수를 받는다.

  1. accumulator
     누산기(accmulator)는 콜백의 반환값을 누적한다. 콜백의 이전 반환값 또는, 콜백의 첫 번째 호출이면서 initialValue를 제공한 경우에는 initialValue의 값이된다.
  2. currentValue
     처리할 현재 요소.
  3. currentIndex Optional
     처리할 현재 요소의 인덱스. initialValue를 제공한 경우 0, 아니면 1부터 시작한다.
  4. array Optional
     callback의 최초 호출에서 첫 번째 인수에 제공하는 값. 초기값을 제공하지 않으면 배열의 첫 번째 요소를 사용한다. 빈 배열에서 초기값 없이 reduce()를 호출하면 오류가 발생한다.

## 반환 값

누적된 계산의 결과 값 하나만을 반환한다.

## 설명

reduce()는 빈 요소를 제외하고 배열 내에 존재하는 각 요소에 대해 callback 함수를 한 번씩 실행하는데, 콜백 함수는 다음의 네 인수를 받는다.

- accumulator
- currentValue
- currentIndex
- array

콜백의 최초 호출 때 accumulator와 currentValue는 다음 두 가지 값 중 하나를 가질 수 있다. 만약 reduce() 함수 호출에서 initialValue를 제공한 경우, accumulator는 initialValue와 같고 currentValue는 배열의 첫 번째 값과 같다.

initialValue를 제공하지 않았다면, accumulator는 배열의 첫 번째 값과 같고 currentValue는 두 번째와 같다.

- 참고로 initialValue를 제공하지 않으면, reduce()는 인덱스 1부터 시작해 콜백 함수를 실행하고 첫 번째 인덱스는 건너 뛴다. initialValue를 제공하면 인덱스 0에서 시작한다.

배열이 비어있는데 initialValue도 제공하지 않으면 TypeError가 발생한다. 배열의 요소가 (위치와 관계없이) 하나 뿐이면서 initialValue를 제공되지 않은 경우, 또는 initialValue는 주어졌으나 배열이 빈 경우엔 그 단독 값을 callback 호출 없이 반환한다.

## 작동 예제

> 예제 1

```js
[0, 1, 2, 3, 4].reduce(function (
  accumulator,
  currentValue,
  currentIndex,
  array,
) {
  return accumulator + currentValue;
});
```

다음과 같은 예제가 있다고 하면 콜백은 총 4번 호출된다. 각 호출의 인수와 반환값은 다음과 같다.

|  callback  | accumulator | currentValue | currentIndex |      array      | 반환 값 |
| :--------: | :---------: | :----------: | :----------: | :-------------: | :-----: |
| 1번째 호출 |      0      |      1       |      1       | [0, 1, 2, 3, 4] |    1    |
| 2번째 호출 |      1      |      2       |      2       | [0, 1, 2, 3, 4] |    3    |
| 3번째 호출 |      3      |      3       |      3       | [0, 1, 2, 3, 4] |    6    |
| 4번째 호출 |      6      |      4       |      4       | [0, 1, 2, 3, 4] |   10    |

reduce()가 반환하는 값으로는 마지막 콜백 호출의 반환값(10)을 사용한다.

완전한 함수 대신에 화살표 함수를 제공할 수도 있다. 아래 코드는 위의 코드와 같은 결과를 반환한다.

```js
[0, 1, 2, 3, 4].reduce((prev, curr) => prev + curr);
```

> 예제 2

reduce()의 두 번째 인수로 초기값을 제공하는 경우, 결과는 다음과 같다.

```js
[0, 1, 2, 3, 4].reduce(function (
  accumulator,
  currentValue,
  currentIndex,
  array,
) {
  return accumulator + currentValue;
},
10);
```

|            | accumulator | currentValue | currentIndex |      array      | 반환 값 |
| :--------: | :---------: | :----------: | :----------: | :-------------: | :-----: |
| 1번째 호출 |     10      |      0       |      0       | [0, 1, 2, 3, 4] |   10    |
| 2번째 호출 |     10      |      1       |      1       | [0, 1, 2, 3, 4] |   11    |
| 3번째 호출 |     11      |      2       |      2       | [0, 1, 2, 3, 4] |   13    |
| 4번째 호출 |     13      |      3       |      3       | [0, 1, 2, 3, 4] |   16    |
| 5번째 호출 |     16      |      4       |      4       | [0, 1, 2, 3, 4] |   20    |

이 때 reduce()가 결과로 반환하는 값은 20이다.

> 예제 3

- 배열의 모든 값 합산

```js
var sum = [0, 1, 2, 3].reduce(function (accumulator, currentValue) {
  return accumulator + currentValue;
}, 0);
// sum is 6
```

화살표 함수로도 작성할 수 있다.

```js
var total = [0, 1, 2, 3].reduce(
  (accumulator, currentValue) => accumulator + currentValue,
  0,
);
```

> 예제 4

- 객체 배열에서의 값 합산
  객체로 이루어진 배열에 들어 있는 값을 합산하기 위해서는 반드시 초기값을 주어 각 항목이 여러분의 함수를 거치도록 해야 한다.

```js
var initialValue = 0;
var sum = [{ x: 1 }, { x: 2 }, { x: 3 }].reduce(function (
  accumulator,
  currentValue,
) {
  return accumulator + currentValue.x;
},
initialValue);

console.log(sum); // logs 6
```

화살표 함수(arrow function)로도 작성할 수 있다

```js
var initialValue = 0;
var sum = [{ x: 1 }, { x: 2 }, { x: 3 }].reduce(
  (accumulator, currentValue) => accumulator + currentValue.x,
  initialValue,
);

console.log(sum); // logs 6
```

> 예제 5

- 중첩 배열 펼치기

```js
var flattened = [
  [0, 1],
  [2, 3],
  [4, 5],
].reduce(function (accumulator, currentValue) {
  return accumulator.concat(currentValue);
}, []);
// 펼친 결과: [0, 1, 2, 3, 4, 5]
```

화살표 함수로 작성시 다음과 같다.

```js
var flattened = [
  [0, 1],
  [2, 3],
  [4, 5],
].reduce((accumulator, currentValue) => accumulator.concat(currentValue), []);
```
