# JavaScript 문법류 요약, 정리파트

자바스크립트를 공부하면서 실제 사용되는 Event나 메소드등을 정리해두려고 만든 문서입니다.

# addEventListener

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

# some()

some() 메서드는 배열 안의 어떤 요소라도 주어진 판별 함수를 통과하는지 테스트한다. 그러나 빈 배열에서 호출하면 무조건 false를 반환한다.

```js
const array = [1, 2, 3, 4, 5];

// checks whether an element is even
const even = (element) => element % 2 === 0;

console.log(array.some(even));
// expected output: true
```

## 구문

```js
arr.some(callback[, thisArg])
```

## 매개변수

- callback
  각 요소를 시험할 함수. 다음 세 가지 인수를 받습니다.
- currentValue
  처리할 현재 요소.
- index Optional
  처리할 현재 요소의 인덱스.
- array Optional
  some을 호출한 배열.
- thisArg Optional
  callback을 실행할 때 this로 사용하는 값.

## 반환 값

callback이 어떤 배열 요소라도 대해 참인(truthy) 값을 반환하는 경우 true, 그 외엔 false.

## some()이란?

some은 callback이 참(불린으로 변환했을 때 true가 되는 값)을 반환하는 요소를 찾을 때까지 배열에 있는 각 요소에 대해 한 번씩 callback 함수를 실행한다. 해당하는 요소를 발견한 경우 some은 즉시 true를 반환한다. 그렇지 않으면, 즉 모든 값에서 거짓을 반환하면 false를 반환한다. 그렇지 않으면, 즉 모든 값에서 거짓을 반환하면 false를 반환한다. 삭제했거나 값을 할당한 적이 없는 인덱스에서는 호출하지 않는다.

thisArg 매개변수를 some에 제공한 경우 callback의 this로 사용된다. 또한 some은 호출한 배열을 변형하지 않는다.

some이 처리하는 요소의 범위는 callback의 첫 호출 전에 설정된다. some 호출 이후로 배열에 추가하는 요소는 callback이 방문하지 않는다. 배열에 원래 있었지만 아직 방문하지 않은 요소가 callback에 의해 변경된 경우, 그 인덱스를 방문하는 시점의 값을 사용한다.

# Document.querySelector()

Document.querySelector()는 제공한 선택자 또는 선택자 뭉치와 일치하는 문서 내 첫 번째 Element를 반환한다. 일치하는 요소가 없으면 null을 반환한다.

탐색은 깊이우선(depth-first) 전위(pre-order)순회로, 문서의 첫 번째 요소부터 시작해 자식 노드의 수를 기준으로 순회한다.

## 구문

```js
document.querySelector(selectors);
```

## 매개변수

하나 이상의 선택자를 포함한 DOMString. 유효한 CSS 선택자여야만 하며 아닐 경우 SYNTAX_ERR 예외가 발생한다.

## 반환값

제공한 CSS 선택자를 만족하는 첫 번째 Element 객체. 결과가 없다면 null.

선택자를 만족하는 모든 요소의 목록이 필요하다면 querySelectorAll()을 대신 사용해야 한다.(뒤에 따로 정리할 메소드)

## 예제

> 예제 1 // 클래스를 만족하는 첫 번째 요소 검색
> 아래 예제는 문서에서 "myclass"라는 클래스를 사용하는 첫 번째 요소를 반환한다.

```js
var el = document.querySelector(".myclass");
```

> 예제 2 // 좀 더 복잡한 선택자

아래 예제처럼 정말 강력한 선택자도 사용할 수 . 예제의 결과는 클래스가 "user-panel main"인 `<div>(<div class="user-panel main">)` 안의, 이름이 "login"인 `<input>` 중 첫 번째 요소입니다.

```js
var el = document.querySelector("div.user-panel.main input[name=login]");
```

# Sort(), localeCompare()

[Sort() MDN 링크](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort "Sort")

sort() 메서드는 배열의 요소를 적절한 위치에 정렬한 후 그 배열을 반환한다.

기본 정렬 순서는 문자열의 유니코드 포인트를 따른다.

## 구문

```js
arr.sort([compareFunction]);
```

## 설명

compareFunction이 제공되지 않으면 요소를 문자열로 변환하고 유니코드 포인트 순서로 문자열을 비교하여 정렬한다.

compareFunction이 제공되면 배열 요소는 compare 함수의 반환 값에 따라 정렬된다.

- compareFunction이 (a, b) < 0 인 경우 a , b 순으로 정렬

- ompareFunction이 (a, b) > 0 인 경우 b , a 순으로 정렬

- compareFunction이 0을 반환하면 a, b를 변경x.

## 예시

```js
function compare(a, b) {
  if (a < b) return -1; // a b 순 정렬
  if (a > b) return 1; // b a 순 정렬
  if (a == b) return 0; // 그대로 ...
}
```

> 오름차순 정렬

```js
function compareNumbers(a, b) {
  return a - b;
}
```

> 내림차순 정렬

```js
function compareNumbers(a, b) {
  return b - a;
}
```

# localeCompare()

[localeCompare MDN 링크](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare "localeCompare MDN 링크")

localeCompare 메서드는 참조 문자열이 정렬 순서에서 앞 또는 뒤에 오는지 또는 주어진 문자열과 같은지를 숫자로 반환한다.

## 구문

```js
referenceStr.localeCompare(compareString[, locales[, options]])
```

## 설명

referenceStr이 compareString보다 앞에 있으면 -1, 뒤에 있으면 1, 같으면 0 반환

```js
"a".localeCompare("b"); // -1 ,
"b".localeCompare("a"); // 1
"c".localeCompare("c"); // 0
```

위에서 언급한 sort()와 묶어서 판단의 기준으로 사용한다고 생각하자.(다른 느낌일 경우 수정 필요)

# FormData()

FormData 인터페이스는 form 필드와 그 값을 나타내는 일련의 key/value 쌍을 쉽게 생성할 수 있는 방법을 제공한다.

또한 FromData란 ajax로 폼 전송을 가능하게 해주는 FormData 객체라고도 할 수 있다.

## 생성자

```js
FormData();
```

새로운 FormData 객체를 생성합니다.

## 구문

```js
var formData = new FormData(form);
```

## 매개변수

form -> Optional
HTML `<form>` 요소 — 지정된 경우 FormData 객체는 form의 현재 key/value인 딕셔너리의 형태로 데이터가 저장된다.

key/value는 submit한 각 요소의 name property와 value값을 사용한다.

## 예제

빈 FormData 객체를 만들어보자.

```js
var formData = new FormData(); // 현재 비어있음
```

FormData.append을 사용하여 key/value 쌍을 추가할 수 있다.

```js
formData.append("username", "Chris");
```

또는 FormData 객체를 만들 때 선택적으로 form argument를 지정할 수 있는데, 지정된 양식대로 value를 미리 채우는 것이다.

```js
<form id="myForm" name="myForm">
  <div>
    <label for="username">Enter name:</label>
    <input type="text" id="username" name="username">
  </div>
  <div>
    <label for="useracc">Enter account number:</label>
    <input type="text" id="useracc" name="useracc">
  </div>
  <div>
    <label for="userfile">Upload file:</label>
    <input type="file" id="userfile" name="userfile">
  </div>
<input type="submit" value="Submit!">
</form>

<script>
var myForm = document.getElementById('myForm');
formData = new FormData(myForm);
</script>
```

# Require()

Node.js에서 require()는 어떻게 작동하는지 알아보자.

localDB 사용프로젝트에서 굉장히 많이 사용되는 메소드인데 node.js에서는 모듈을 불러오기 위해 require()함수를 사용한다.

간단한 예를 통해 기능을 자세히 알아보자.

exam1.js와 exam2.js 두 파일이 있다고 가정해 보자.

```js
//exam1.js
const a = 3333;
```

그리고

```js
//exam2.js
console.log(a);
```

이 상황에서 exam2.js를 실행시키면 exam2.js의 스코프에 변수 a는 정의되있지 않은 undefined이기 때문에 에러가 발생한다.

```js
node exam2.js
ReferenceError: a is not defined
```

이러한 문제를 해결하기위한 방안이 require함수를 사용하는 것이다. exam1.js
를 exam2.js로 가지고 오면 된다.

```js
//exam2.js

const exam = require("./exam1.js"); // exam1과 exam2는 같은디렉토리에 있다고 가정한다.
console.log(exam.a);
```

그러나 여기서도 다음과 같은 undefined문제가 발생한다.

```js
node exam2.js
ReferenceError: a is not defined
```

이는 export가 없기 때문에 발생하는 문제이다.

```js
// exam1.js
const a = 3333;
exports.a = a;
```

이 이후 싱핼해보면 문제없이 원하는 값이 나온다.

```js
node exam2.js
3333
```

> Require()함수는 module.exports를 리턴한다.

Require()함수의 소스코드는 복잡하다.

그러나 공식문서를 요약하면 다음과 같은 모양새로 구성되어있다고 한다.

```js
var require = function(src){                 //line 1
    var fileAsStr = readFile(src)            //line 2
    var module.exports = {}                  //line 3
    eval(fileAsStr)                          //line 4
    return module.exports                    //line 5
}
```

- line 1에서는 src의 인자를 받아온다.

예를 들어 다음과 같이 사용하면

```js
const exam1 = require("exam1");
```

'exam1'을 인자로 받아온다는 것이다.

- line 2에서는 소스 파일을 읽어서 fileAsStr에 저장한다.

- line 3에서는 module.exports라는 빈 해시를 만들어 둔다.

- line 4에서는 fileAsStr을 eval한다. 이 과정은 사실상 src를 복붙한다고 생각하면 좋다.

line4부분이 굉장히 중요하다고 생각하기 때문에 좀 더 자세히 설명해보자.

예시로

```js
const exam1 = require("/exam1.js");
```

과 같이 사용하면 이는 곧 require()의 src 인자로 './exam1.js'를 넣는 다는 의미이고 위의 require()의 line 4는

```js
eval(fileAsStr); //line 4
```

에서 다음과 같이 강조한 부분처럼 바뀌는 것이다.

```js
var require = function(src){                 //line 1
    var fileAsStr = readFile(src)            //line 2
    var module.exports = {}                  //line 3
    `const a = 3333
    exports.a = a;`
    return module.exports                    //line 5
}
```

결국 exports 해시의 a라는 key에 3333이라는 값이 들어가게 되는 셈이다.

마지막으로 line5에서 require는 해당 exports 해시를 아웃풋으로 내보낸다.

따라서 exam2.js는 원래 다음과 같은 모양의 파일이지만

```js
// eaxm2.js
const eaxm1 = require("./eaxm1.js"); //eaxm1.js, eaxm2.js는 같은 디렉토리이다
console.log(eaxm1.a);
```

런타임에서는 사실 다음과 같은 모습이 되는 것이다.

```js
// exam2.js

const exam1 = { a: 3333 };
console.log(exam1.a);
```

exam1에서 exports에 들어간 (key,value) 값들이 require()함수의 아웃풋으로 나오게 되는 것이다.

# exports() , module.exports

위에서 exports는 exam1.js함수의 특정값을 exam2.js로 넘겨주고싶을 때 등장했다.

우선 위에서도 언급했듯, require함수의 구조는 다음과 같다.

```js
var require = function(src){                 //line 1
    var fileAsStr = readFile(src)            //line 2
    var module.exports = {}                  //line 3
    eval(fileAsStr)                          //line 4
    return module.exports                    //line 5
}
```

그리고 line4의 eval 단계가 일종의 코드 복사 붙여넣기의 단계와 같다고 보면 된다.

```js
var require = function(src){                 //line 1
    var fileAsStr = readFile(src)            //line 2
    var module.exports = {}                  //line 3
    `const a = 3333
    exports.a = a;`
    return module.exports                    //line 5
}
```

여기서 중요한 부분은 `exports`와 `module.exports`는 `같은 대상을 지칭하는 서로 다른 두 명칭`이라는 부분이다.

위의 require의 과정을 살펴보면

1. line 3에서 module.exports의 변수명으로 빈 해시를 만들었고

2. line 4.2에서 exports에 <key: value>로서 <a : 10>을 넣은 것이며 이는 곧,

3. module.exports에 <key: value>로서 <a : 10>을 넣은 것과 같다.

그렇다면 `exports`와 `module.exports`는 무슨 차이인가? 궁금해진다.

허나 `exports`와 `module.exports`의 차이는

단순히 `exports`는 `module.exports`를 참조할 뿐이라고 한다. 짧은 alias(별명)에 불과하다는 것이다.

공식문서에서 `module.exports`와 `exports`는 같은 객체를 바라보고 있으며, `exports`는 `module.exports`의 shortcut이라고 한다.

그렇다면 `exports`는 `module.exports` 개념적 차이는 없지만 용도는 나뉘기 때문에 어떻게 사용할지가 중요한 부분이다.

용도는 크게 2가지로 나뉜다고 볼 수 있따.

> 1. exported value/function를 담는 컨테이너로 쓰기

우선 첫번째로 아주 일반적인 케이스로, exam1.js에서 exam2.js의 함수와 값들을 읽어오고 싶어하는 경우이다.

이는 express-test에서 사용한 바와 같이

```js
// express-test 개인프로젝트
// connection.js파일
module.exports = new DBConnection();
```

별도로 connection.js라는 문서에서 DBConnection이라는 클래스와 내부 함수를 구성해놓고 module.exports로 다른 파일(index.js)에서 불러와서 사용한다.

```js
// express-test 개인프로젝트
// index.js
const connection = require("./db/connection"); // 모듈로 불러오는 부분

// 불러온 파일의 함수를 현재 파일에서 사용하여 서버에 연걸하는 부분
connection.connect().then(() => {
  app.listen(8080, () => {
    console.log("listenning on http://localhost:" + 8080);
  });
});
```

> 2.  constructor function으로 사용하는 방법

express를 활용한 localDB 프로젝트에서 가장 먼저 사용한 구문을 예로 살펴보자.

```js
// express-test 개인프로젝트
// index.js
const express = require("express");
const app = express();
```

단순히 값을 가져오는 것이 아니라, exporess의 객체를 생성하는 식이다.

앞의 목적 1에서는 속성(Property)가 담긴 객체가 require()의 아웃풋이 되도록 exports 한 것이다.

목적 2에서는 객체가 아웃풋으로 나오도록 exports하는 방법이라는 차이가 있다.

# windows.onload()

javaScript는 html 내의 요소들을 움직일수 있는 dom 객체를 조작하는 방식으로 주로 사용한다.

위로부터 차례차례 읽어들이는 프로그래밍 본연의 작동 방식과, 실행 이전에 에러 체크를 하지 않고 실행을 하는 인터프리터 언어적 특성으로 인해,

자바스크립트는 작성 위치에 따라 오작동을 일으키기도 한다.

하나의 예로써

```html
<script>
  var a = document.getElementById("hel");
  a.style.color = "blue";
</script>

<p id="hel">hello</p>
```

과 같이 사용하면 원칙상으로 자바스크립트의 var a = document.getElementById( 'hel' ); 이 html 내부의 id가 hel이란 태그가 생성되기도 전에 실행되므로 문제가 발생한다.

물론 script 태그 부분을 뒤로 빼서 사용하면 문제가 해결되기는 하지만 html 문서가 길어지면 가독성도 떨어지는 문제아닌 문제점이 생기게 된다.

그렇기에 자바스크립트가 문서가 준비된 상황 이후에 발동하도록만 한다면 문서 앞에 선언해도 상관 없어지게 된다.

바로 이런 것을 해주는 것이 window.onload 메소드이다.

express-test에서 사용하는것 처럼 다른 파일을 require로 불러오면 html문서보다 먼저 출력되는 경우가 생기기 때문에

window.onload라는 메서드를 오버라이딩(재정의) 해주면 되는데, 해당 함수 내의 코드 스크립트는 웹브라우저 내의 모든 요소가 준비가 되어야 실행이 되도록 할수 있다.

# JSON.stringfy()

JSON.stringify() 메서드는 JavaScript 값이나 객체를 JSON 문자열로 변환한다.

선택적으로, replacer를 함수로 전달할 경우 변환 전 값을 변형할 수 있고, 배열로 전달할 경우 지정한 속성만 결과에 포함한다.

## 구문

```js
JSON.stringify(value[, replacer[, space]])
```

## 매개변수

- value
  json 문자열로 변환할 값

- replacer -> Optional
  문자열화 동작 방식을 변경하는 함수, 혹은 json 문자열에 포함될 값 객체의 속성등을 선택하기 위한

- space -> Optional

가독성을 위해 json 문자열 출력에 공백을 삽입하는데 사용되는 string 또는 Number 객체.

만약 이 매개변수가 Number라면, 공백으로 사용되는 스페이스(space)의 수를 나타낸다. 그러나 수가 10보다 크면 10으로 제한된다. 1보다 작은 값일 경우에는 사용되지 않는 것으로 간주한다.

## 반환값

주어진 값과 대응하는 JSON 문자열을 반환한다.

## 설명

위에서도 말했듯 JSON.stringify()는 값을 JSON 표기법으로 변환한다.

- 배열이 아닌 객체의 속성들은 어떤 특정한 순서에 따라 문자열화 될 것이라고 보장되지 않는다. 같은 객체의 문자열화에 있어서 속성의 순서에 의존하지 않는다.

- Boolean, Number, String 객체들은 문자열화 될 때 전통적인 변환 의미에 따라 연관된 기본형(primitive) 값으로 변환된다.

- undefined, 함수, 심볼(symbol)은 변환될 때 생략되거나(객체 안에 있을 경우) null 로 변환된다(배열 안에 있을 경우).

- 심볼을 키로 가지는 속성들은 replacer 함수를 사용하더라도 완전히 무시된다.

- 열거 불가능한 속성들은 무시된다.

### 반환값 예시

```js
JSON.stringify({}); // '{}'
JSON.stringify(true); // 'true'
JSON.stringify("foo"); // '"foo"'
JSON.stringify([1, "false", false]); // '[1,"false",false]'
JSON.stringify({ x: 5 }); // '{"x":5}'

JSON.stringify(new Date(2006, 0, 2, 15, 4, 5));
// '"2006-01-02T15:04:05.000Z"'

JSON.stringify({ x: 5, y: 6 });
// '{"x":5,"y":6}' or '{"y":6,"x":5}'
JSON.stringify([new Number(1), new String("false"), new Boolean(false)]);
// '[1,"false",false]'

// Symbols:
JSON.stringify({ x: undefined, y: Object, z: Symbol("") });
// '{}'
JSON.stringify({ [Symbol("foo")]: "foo" });
// '{}'
JSON.stringify({ [Symbol.for("foo")]: "foo" }, [Symbol.for("foo")]);
// '{}'
JSON.stringify({ [Symbol.for("foo")]: "foo" }, function (k, v) {
  if (typeof k === "symbol") {
    return "a symbol";
  }
});
// '{}'

// Non-enumerable properties:
JSON.stringify(
  Object.create(null, {
    x: { value: "x", enumerable: false },
    y: { value: "y", enumerable: true },
  }),
);
// '{"y":"y"}'
```

## 예제

```js
console.log(JSON.stringify({ x: 5, y: 6 }));
// expected output: "{"x":5,"y":6}"

console.log(
  JSON.stringify([new Number(3), new String("false"), new Boolean(false)]),
);
// expected output: "[3,"false",false]"

console.log(JSON.stringify({ x: [10, undefined, function () {}, Symbol("")] }));
// expected output: "{"x":[10,null,null,null]}"

console.log(JSON.stringify(new Date(2006, 0, 2, 15, 4, 5)));
// expected output: ""2006-01-02T15:04:05.000Z""
```

> 함수를 사용한 경우의 예제

```js
function replacer(key, value) {
  if (typeof value === "string") {
    return undefined;
  }
  return value;
}

var foo = {
  foundation: "Mozilla",
  model: "box",
  week: 45,
  transport: "car",
  month: 7,
};
var jsonString = JSON.stringify(foo, replacer);
```

이 경우 JSON 문자열 결과는 {"week":45,"month":7} 이다.

> 배열을 사용한 경우에 대한 예제

replacer 가 배열인 경우, 그 배열의 값은 JSON 문자열의 결과에 포함되는 속성의 이름을 나타낸다

```js
JSON.stringify(foo, ["week", "month"]);
// '{"week":45,"month":7}', 단지 "week" 와 "month" 속성을 포함한다
```

> space 매개 변수

space 매개변수는 최종 문자열의 간격을 제어한다. 숫자일 경우 최대 10자 만큼의 공백 문자 크기로 들여쓰기되며, 문자열인 경우 해당 문자열 또는 처음 10자 만큼 들여쓰기 된다.

```js
JSON.stringify({ a: 2 }, null, " ");
// '{
//  "a": 2
// }'
```

'\t'를 사용하면 일반적으로 들여쓰기 된 코드스타일과 유사하다.

```js
JSON.stringify({ uno: 1, dos: 2 }, null, "\t");
// returns the string:
// '{
//     "uno": 1,
//     "dos": 2
// }'
```

# Promise

프로미스는 자바스크립트 비동기 처리에 사용되는 객체이다.

동시에 자바스크립트에서 비동기 동작을 다루는 하나의 패턴이며, 어떤 일의 진행 상태를 나타내는 객체로, 진행 "상태"와 "값"이라는 속성을 가지고 있는 것을 말하기도 한다.

자바스크립트의 `비동기 처리`란 '특정 코드의 실행이 완료될 때까지 기다리지 않고 다음 코드를 먼저 수행하는 자바크스립트의 특성'을 의미한다.

Promise는 주로 서버에섣 받아온 데이터를 화면에 표시할 때 사용한다. 웹 애플리케이션을 구현할 때 서버에서 데이터를 요청하고 받아오기 위하여 다음과 같은 API를 사용한다.

```JS
$.get('url 주소/products/1', function(response) {
  // ...
});
```

위의 API가 실행되면 서버에 '데이터를 하나 보내시오' 라는 요청을 보낸다. 그러나 여기서 데이터를 받아오기도 전에 마치 데이터를 다 받아온 것 마냥 화면에 데이터를 표시하려고 하면 오류가 발생하거나 빈 화면이 뜨게된다.

간단한 예를 통해 알아보자.

다음 예제는 J쿼리를 이용한 ajax 통신코드이다.

```js
function getData(callbackFunc) {
  $.get("url 주소/products/1", function (response) {
    callbackFunc(response); // 서버에서 받은 데이터 response를 callbackFunc() 함수에 넘겨줌
  });
}

getData(function (tableData) {
  console.log(tableData); // $.get()의 response 값이 tableData에 전달됨
});
```

위 코드는 J쿼리의 ajax 통신 API를 이용하여 지정 url에서 1번 products 데이터를 받아오는 코드이다. 비동기 처리를 위해 콜백 함수를 사용한 모습이다.

위 코드에 프로미스를 적용하면 다음과 같은 모습이 된다.

```js
function getData(callback) {
  // new Promise() 추가
  return new Promise(function (resolve, reject) {
    $.get("url 주소/products/1", function (response) {
      // 데이터를 받으면 resolve() 호출
      resolve(response);
    });
  });
}

// getData()의 실행이 끝나면 호출되는 then()
getData().then(function (tableData) {
  // resolve()의 결과 값이 여기로 전달됨
  console.log(tableData); // $.get()의 reponse 값이 tableData에 전달됨
});
```

콜백 함수로 처리하던 구조에서 new Promise(), resolve(), then()등의 프로미스 API를 사용한 구조로 바뀌었다.

new Promise()야 Promise라는 함수의 생성자이므로 그러려니 하고 넘어갈 수 있지만 resolve와 then은 맹 생소한 개념이므로 둘의 역할에 대해 알아보자.

## 프로미스의 3가지 상태(state)

프로미스를 사용할 때 알아야 하는 가장 기본적인 개념이 바로 프로미스의 상태(state)이다. 여기서 말하는 상태란 프로미스의 처리과정을 의미한다.

프로미스는 new Promise()로 프로미스를 생성하고 종료될 때 까지 총 3가지의 상태를 갖는다.

- Pending(대기) : 비동기 처리 로직이 아직 완료되지 않은 상태

- Fulfilled(이행) : 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태

- Rejected(실패) : 비동기 처리가 실패하거나 오류가 발생한 상태

### Pending(대기)

먼저 다음과 같이 new Promise() 메소드를 호출하면 대기(Pending)상태가 된다.

```js
new Promise();
```

new Promise() 메소드를 호출할 때 콜백함수를 선언할 수 있고, 콜백 함수의 인자는 resolve와 reject 2개이다.

```js
new Promise(function (resolve, reject) {
  // 콜백함수 사용한 기본 포맷
});
```

### Fulfilled(이행)

여기서 콜백 함수의 인자 resolve를 다음과 같이 실행하면 이행(Fulfilled) 상태가 된다.

```js
new Promise(function (resolve, reject) {
  resolve();
});
```

그리고 이행 상태가 되면 then()을 이용하여 처리 결과 값을 받을 수 있다.

```js
function getData() {
  return new Promise(function (resolve, reject) {
    var data = 100;
    resolve(data);
  });
}

// resolve()의 결과 값 data를 then의 콜백함수 매개변수가 받음.
// 이 예제에선 resolveData가 그 값을 받음.
getData().then(function (resolvedData) {
  console.log(resolvedData); // 100
});
```

### Rejected(실패)

new Promise()로 프로미스 객체를 생성하면 콜백 함수 인자로 resolve와 reject를 사용할 수 있다고 위에서 말했었다. 여기서 reject를 아래와 같이 호출하면 실패(Rejected) 상태가 된다.

```js
new Promise(function (resolve, reject) {
  reject();
});
```

그리고 실패 상태가 되면 실패한 이유(실패 처리의 결과 값)을 catch()로 받을 수 있다.

```js
function getData() {
  return new Promise(function (resolve, reject) {
    reject(new Error("Request is failed"));
  });
}

// reject()의 결과 값 Error를 err에 받음
getData()
  .then()
  .catch(function (err) {
    console.log(err); // Error: Request is failed
  });
```

<img src=https://mdn.mozillademos.org/files/8633/promises.png>
프로미스의 처리 흐름 - 출저 : MDN

## 프로미스 간단 예제

```js
function getData() {
  return new Promise(function (resolve, reject) {
    $.get("url 주소/products/1", function (response) {
      if (response) {
        resolve(response);
      }
      reject(new Error("Request is failed"));
    });
  });
}

// 위 $.get() 호출 결과에 따라 'response' 또는 'Error' 출력
getData()
  .then(function (data) {
    console.log(data); // response 값 출력
  })
  .catch(function (err) {
    console.error(err); // Error 출력
  });
```

위 코드는 서버에서 제대로 응답을 받아오면 resolve() 메소드를 호출하고, 응답이 없으면 reject() 메소드를 호출하는 예제이다. 호출된 메소드에 따라 then()이나 catch()로 분기하여 응답 결과 또는 오류를 출력한다.

## 여러 개의 프로미스 연결하기 (Promise Chaining)

프로미스의 또 다른 특징은 여러 개의 프로미스를 연결하여 사용할 수 있다는 점이다.

앞 예제에서 then() 메서드를 호출하고 나면 새로운 프로미스 객체가 반환된다. 따라서, 아래와 같이 코딩이 가능하다.

```js
function getData() {
  return new Promise({
    // ...
  });
}

// then() 으로 여러 개의 프로미스를 연결한 형식
getData()
  .then(function (data) {
    // ...
  })
  .then(function () {
    // ...
  })
  .then(function () {
    // ...
  });
```

그러면 이제 위의 형식을 참고하여 실제로 위의 형식을 사용하는 예제를 통해 살펴보자. 비동기 처리에서 가장흔하게 사용되는 setTimeout() API를 사용해보자.

```js
new Promise(function (resolve, reject) {
  setTimeout(function () {
    resolve(1);
  }, 2000);
})
  .then(function (result) {
    console.log(result); // 1
    return result + 10;
  })
  .then(function (result) {
    console.log(result); // 11
    return result + 20;
  })
  .then(function (result) {
    console.log(result); // 31
  });
```

위 예제 코드는 프로미스 객체를 하나 생성하고 setTimeout() 메소드를 활용해 2초 후에 resolve()를 호출하는 예제이다.

resolve()가 호출되면 프로미스가 대기 상태에서 이행 상태로 넘어가기 때문에 첫 번째 .then() 로직으로 넘어간다.

첫 번째 .then()에서는 이행된 결과 값 1을 받아서 10을 더한 후 그 다음 .then()으로 넘긴다.

두 번째 .then()에서도 마찬가지로 바로 이전 프로미스의 결과 값 11을 받아서 20을 더하고 다음 .then으로 넘겨준다.

그러면 마지막 .then()에서 최종 결과값 31을 출력한다.

# Dataset 메소드

`dataset` 메소드는 HTML 표준에 정의된 기능이다.

DOM요소에 값을 저장, JS 코드로 값을 읽어들일 수 있다.

dataset 자체는 읽기 전용 속성이라 dataset 자체로는 별도로 재설정 불가.

해당 내용을 변경하려면, dataset 소속의 keyname에 접근해 변경해야 함.

## html 사용법

data 속성 이름 짓는 법은 data-를 시작으로 `data-이름을-지정하면-된다`의 형태로 이름을 지으면 된다.

크게 두가지 유형이 있다.

- dash-style 형태 : HTML 요소의 속성으로 사용 시 형태.
  ex) data-abc-def
- camelCase 형태 : JS dataset 속성의 key로 사용 시 형태.
  ex) abcDef

ex1)

```html
// 예시 1
<p data-user-name>{state.userName}</p>
```

ex2)

```js
// 실제소 사용한 예시 2
<button data-role="edit" data-id="${_id}">수정</button>
<button data-role="delete" data-id="${_id}">삭제</button>
```

## dash-style → camelCase 변환 규칙

1. data- 접두어 제거.

2. ASCII 소문자 (a ~ z)앞 모든 대시(U+002D)는 삭제되고, 해당 소문자는 대문자로 변환되어 camelCase 형태로 바뀜.

- 다른 대시들 포함해 다른 기호는 안 바뀜.

## js 사용법

data-user-name 데이터 세트를 읽어들인다면, data-는 제거되며, userName과 같이 카멜케이스로 변경하여 읽는다.

```js
data- 뒤에 가능 : 소문자 영문, 점(.), 하이픈(-), 로우데시(_), 콜론(:)
data- 뒤에 사용 불가능 : 대문자 영문
html에서 data-abc-def 라는 이름의 속성은 JS에서 `abcDef` key에 응답
```

## dataset 실사용 구문

```js
var_name = element.dataset.keyname;
element.dataset.keyname = string;

var_name = element.dataset["keyname"];
element.dataset["keyname"] = string;
```

> 구문 설명

- element : HTML 태그 요소

- dataset : 해당 THML 태그의 data-\* 속성의 키/값 모음

- keyname : 특정 data 키. ※ camelCasedName (낙타 대문자) 형태여야 함.

# Fetch

자바스크립트를 사용하면 필요할 때 서버에 네트워크 요청을 보내고 새로운 정보를 받아오는 일을 할 수 있는 메소드이다.

XMLHttpRequest와 비슷하지만 fetch는 Promise를 기반으로 구성되어 있어서 더 간편하게 사용할 수 있다는 차이점이 있다.

네트워크 요청은 다음과 같은 경우에 이뤄진다.

- 주문 전송
- 사용자 정보 읽기
- 서버에서 최신 변경분 가져오기
- 등등

이 모든 것들은 페이지 새로 고침 없이 가능하다.

AJAX(Asynchronous JavaScript And XML, 비동기적 JavaScript와 XML)는 서버에서 추가 정보를 비동기적으로 가져올 수 있게 해주는 포괄적인 기술을 나타내는 용어인데 이 AJAX를 통해서도 해결이 가능하지만

지금 정리하는 fetch() 메소드를 활용해서도 가능하다.

> 기본 문법

fetch()의 기본 문법은 다음과 같은 형태를 가진다.

```js
fetch(url)
  .then((res) => {
    console.log(res);
  })
  .catch((error) => {
    console.log(error);
  });
```

기본적인 구조와 동작은 Promise 객체와 동일하다.

첫번째 파라미터로 요청을 보낼 url을 입력해 주고 응답을 받아서 추가적인 작업 또한 해줄 수 있다.

then에서 응답 객체 res를 받고, catch에서 에러 요청이 발생했을 때, 에러를 받는다.

> 매개변수

Fetch의 두 번째 파라미터로 요청에 대한 추가적인 데이터를 입력할 수 있다.

```js
fetch(url, {
  method: "post",
  headers: {
    "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
  },
  body: "foo=bar&lorem=ipsum",
}) // url 다음에 오는 파라미터가 option 부분에 해당함.
  .then((res) => {
    console.log(res);
  })
  .catch((error) => console.log(error));
```

- method : HTTP method와 동일하며 요청 방식을 나타낸다. (GET, POST, PUT, DELETE 등)

- headers : 요청 헤더에 대한 정보를 나타낸다.

- body : 요청을 보내는 데이터를 나타낸다. 여러 가지 자료형을 대입할 수 있다.

fetch 파라미터로 직접 입력하기도 하지만 주로 객체 변수에 저장해서 대입하는 방식으로도 사용한다.

```js
let obj = {
    method: 'post',
    headers: {
      "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
    },
    body: 'foo=bar&lorem=ipsum'
}
fetch(url, obj) // 객체 변수 obj를 옵션부분에 넣은 형태.
.then(...)
```

## 응용 예제

> POST 요청 보내고 응답받기

```js
fetch(url, {
  method: 'POST',
  body: JSON.stringify({ name: "hello!" })
})
.then(res => {
  if (res.status === 200) {
    res.text().then(text => console.log(text)
  }
  else {
    console.log(res.statusText)
  }
})
.catch(err => console.log(err))
```

POST로 body안에 데이터를 넣고, 요청을 보내주면 응답 객체 res를 받게 되는데 res 안에는 응답에 관한 정보가 존재한다.

`status`는 요청이 성공인지 실패인지를 판별할 수 있게 해주는 요소이다.

또 응답에 대한 내용은 `res.text()`를 통해 확인할 수 있다.

text() 외에도 arrayBuffer, blob, json, formData 등의 메서드를 사용하여 값을 볼 수도 있다.

GET, PUT, DELETE 요청도 같은 방식으로 보낼 수 있다.

단, GET, DELETE 요청은 url 파라미터 하나만 입력하여 사용한다.

---

response 에는 프로미스를 기반으로 하는 다양한 메소드가 있다. 이 메서드들을 사용하면 다양한 형태의 응답 본문을 처리할 수 있다.

- response.text() – 응답을 읽고 텍스트를 반환한다.
- response.json() – 응답을 JSON 형태로 파싱한다.
- response.formData() – 응답을 FormData 객체 형태로 반환한다.
- response.blob() – 응답을 Blob(타입이 있는 바이너리 데이터) 형태로 반환합니다.
- response.arrayBuffer() – 응답을 ArrayBuffer(바이너리 데이터를 로우 레벨 형식으로 표현한 것) 형태로 반환합니다.

# Map , Reduce

## Map

> 문법

```js
배열.map((요소, 인덱스, 배열) => {
  return 요소;
});
```

map의 기본 원리는 반복문을 돌며 배열 안의 요소들을 1대1로 짝지어 주는 것이다.

어떻게 짝지어줄 것인가 정의한 함수를 메서드의 인자로 넣어주면 된다.

> 예시

```js
const oneTwoThree = [1, 2, 3];
let result = oneTwoTㅈhree.map((v) => {
  console.log(v);
  return v;
});

// 콘솔에는 1, 2, 3이 찍힘
oneTwoThree; // [1, 2, 3]
result; // [1, 2, 3]
oneTwoThree === result; // false
```

반복문으로 요소를 순회(1, 2, 3 순서로)하면서 각 요소를 어떻게 짝지어줄지 알려준다고 보면 된다.

함수가 그냥 return v를 하기 때문에 같은 값을 그대로 짝짓는다.

여기서 중요한 부분은 map을 실행하는 배열(oneTwoThree)과 결과로 나오는 배열(result)이 다른 객체라는 것이다. 기존 배열을 수정하지 않고 새로운 배열을 만들어낸다.

단, 배열 안에 객체가 들어있는 경우, 객체는 공유된다고 한다.

> 예시 2

```js
result = oneTwoThree.map((v) => {
  return v + 1;
});
result; // [2, 3, 4]
```

규칙적인 배열만 반환할 수 있는게 아니라, 함수 안에 적어준대로 반환할 수 있기 때문에 자유도가 높다.

> 예시 3

```js
result = oneTwoThree.map((v) => {
  if (v % 2) {
    return "홀수";
  }
  return "짝수";
});
result; // ['홀수', '짝수', '홀수']
```

정리하자면, map은 `배열을 1대1로 짝짓되 기존 객체를 수정하지 않는 메서드`이다.

## reduce

> 문법

```js
배열.reduce((누적값, 현잿값, 인덱스, 요소) => {
  return 결과;
}, 초깃값);
```

파라미터가 이전값이 아니라 `누적값`이라는 것에 주의해야 한다. 누적값이기 때문에 다양하게 활용할 수 있다.

> 덧셈 예시

```js
// oneTwoThree = [1,2,3]
result = oneTwoThree.reduce((acc, cur, i) => {
  console.log(acc, cur, i);
  return acc + cur;
}, 0);
// 0 1 0  -> 누적값(초기값 : 0)  현재값 1(인덱스 1), 현재값 1의 인덱스는 0
// 1 2 1  -> 누적값(초기값 0 + 이전 현재값 1더해서 1), 현재값 2 , 현재값 2의 인덱스는 1
// 3 3 2  -> 누적값(이전 누적값 1에 현재값 2더해서 3), 현재값 3, 현재값 3의 인덱스는 2
result; // 6
```

acc(누적값)이 초깃값인 0부터 시작해서 return하는대로 누적되는 것을 볼 수 있다.

초깃값을 적어주지 않으면 자동으로 초깃값이 0번째 인덱스의 값이 된다.

> 덧셈 예시2

```js
result = oneTwoThree.reduce((acc, cur, i) => {
  console.log(acc, cur, i);
  return acc + cur;
});
// 1 2 1
// 3 3 2
result; // 6
```

> reduce map 예제

```js
result = oneTwoThree.reduce((acc, cur) => {
  acc.push(cur % 2 ? "홀수" : "짝수");
  return acc;
}, []);
result; // ['홀수', '짝수', '홀수']
```

초깃값을 배열로 만들고, 배열에 값들을 push하면 map과 같아진다.

이를 응용하여 조건부로 push를 하면 filter와 같아진다.

> 홀수 필터링 예제

```js
result = oneTwoThree.reduce((acc, cur) => {
  if (cur % 2) acc.push(cur);
  return acc;
}, []);
result; // [1, 3]
```

sort, every, some, find, findIndex, includes도 다 reduce로 구현 가능하다.

> reduce 비동기 프로그래밍 예시

```js
const promiseFactory = (time) => {
  return new Promise((resolve, reject) => {
    console.log(time);
    setTimeout(resolve, time);
  });
};
[1000, 2000, 3000, 4000].reduce((acc, cur) => {
  return acc.then(() => promiseFactory(cur));
}, Promise.resolve());
// 바로 1000
// 1초 후 2000
// 2초 후 3000
// 3초 후 4000
```

초깃값을 Promise.resolve()로 한 후에, return된 프로미스에 then을 붙여 다음 누적값으로 넘기면 프로미스가 순차적으로 실행됨을 보장할 수 있다고 한다.

`반복되는 모든 것에는 reduce를 쓸 수 있다.`

## reduce 추가적인 개인 테스트 결과 정리

테스트 환경 -> Firefox 콘솔창

> test 1

```js
test = [1, 2, 3, 4];
test.reduce((acc, cur, index) => {
  console.log(acc, cur, index);
  if (cur % 2) {
    return acc + cur;
  } else {
    return acc;
  }
});
```

위와 같은 경우 acc 초기값 미설정하면 아예 배열의 첫번째 인자를 acc의 값으로 사용함. -> cur값은 2부터시작함(인덱스가 0이 아닌 1부터 시작 아예 첫번째 인자값을 빼와서 부여하는듯)

> test 2

```js
test = [1, 2, 3, 4];
a = test.reduce((acc, cur, index) => {
  console.log(acc, cur, index);
  return acc;
});

console.log("a :", a); // a는 1출력.
```

위와 같은 경우 reduce 메소드의 최종 반환값은 별도의 식이 없고 acc를 반환하기 때문에 acc값이 최종값.

> test 3

```js
test = { a: 1, b: 2, c: 3, d: 4 };
test2 = Object.entries(test); // test2 : Array(4) [ (2) […], (2) […], (2) […], (2) […] ]

a = test2.reduce((acc, [cur1, cur2], index, array) => {
  console.log(acc, cur1, cur2, index, array); //acc : Object {  } cur1 : a cur2 : 1 index : 0  array : Array(4) [ (2) […], (2) […], (2) […], (2) […] ]
  if (cur1 == "a") {
    console.log("으아");
  }
  return acc;
}, {});

console.log("a :", a);
```

> test 4

```js
name = "케케케";
nationalLanguage = 550;
english = 55;
math = 55;
student = { name, nationalLanguage, english, math };

test = Object.entries(student);
console.log(test); // Array(4) [ (2) […], (2) […], (2) […], (2) […] ]

test.reduce((acc, [cur1, cur2], index) => {
  console.log(acc, cur1, cur2, index); // Object {  } / name / 케케케 / 0 순으로 출력됨.
  if (cur1 == "math" || cur1 == "english") {
    // 조건문 해당되면 acc만 출력
    return acc; // 누산기(acc)에 입력값이나 별도함수 없어서 초기값 그대로 부여됨(한마디로 생략)
  }
}, {});

// 순서대로 출력되는 console.log 값
// 각각 acc, cur1, cur2, index 값
// undefined nationalLanguage 550 1
// undefined english 55 2
// undefined math 55 3
```

> test 5

문법 검증.

1. acc.status -> acc 초기값 자체가 빈객체 -> 그 다음엔 if문 조건 바꿔야만 acc값 갱신됨.

```js
name = "케케케";
nationalLanguage = 550;
english = 55;
math = 55;
const student = { name, nationalLanguage, english, math };
console.log("student : ", student); // student :  Object { name: "케케케", nationalLanguage: 550, english: 55, math: 55 } 출력

const VALIDATION_STATUS = {
  TYPE_ERROR: "TYPE_ERROR",
  OUT_OF_RANGE: "OUT_OF_RANGE",
  EMPTY: "EMPTY",
  VALID: "VALID",
};

const VALIDATION_MESSAGE = {
  [VALIDATION_STATUS.OUT_OF_RANGE]: (field) =>
    `${field}값이 범위를 벗어났습니다. 올바른 값을 입력해주세요. (1~100)`,
  [VALIDATION_STATUS.TYPE_ERROR]: (field) =>
    `${field}의 형식이 올바르지 않습니다.`,
  [VALIDATION_STATUS.EMPTY]: (field) => `${field}값이 없습니다.`,
};

const checkValidName = (name) => {
  if (!name) {
    return VALIDATION_STATUS.EMPTY;
  }
  return typeof name === "string"
    ? VALIDATION_STATUS.VALID
    : VALIDATION_STATUS.TYPE_ERROR;
};

const checkValidScore = (score) => {
  if (!score) {
    return VALIDATION_STATUS.EMPTY;
  }
  if (typeof score !== "number") {
    return VALIDATION_STATUS.TYPE_ERROR;
  }
  return score < 0 || score > 100
    ? VALIDATION_STATUS.OUT_OF_RANGE
    : VALIDATION_STATUS.VALID;
};

// 여기 위까지 함수동작 이상없음. CheckValidStudent 부분에서 에러 발생함(테스트 환경 Firefox 동일)
//

const checkValidStudent = ({ name, ...scores }) => {
  if (checkValidName(name) !== VALIDATION_STATUS.VALID) {
    return { status: checkValidName(name), field: "name" };
  }

  console.log("scroes : ", scores); // scroes : Object { nationalLanguage: 550, english: 55, math: 55 } 출력
  console.log("Obsject.entrise : ", Object.entries(scores)); // Obsject.entrise : Array(3) [ (2) […], (2) […], (2) […] ] 출력

  return Object.entries(scores).reduce((acc, [field, score]) => {
    // reduce -> 순번대로 진행됨.
    const status = checkValidScore(score); // score값이 함수 설정 범위 밖이면 해당 에러문구 출력.
    console.log("status :", status); // 여기부턴 차례대로 (reduce 메소드) 돌아가면서 배열 순회
    console.log("field : ", field);
    console.log("score : ", score);

    if (status == VALIDATION_STATUS.VALID) {
      // acc.status == 유효값일땐 acc.status가 VALID 출력됨.
      console.log("acc : ", acc, "acc.status", acc.status); // acc.status는 값자체가 없음. acc 초기값이 빈 객체이면 그냥 빈객체만 반환함. acc.status 판별자체도 불가능함. 이 부분을 유효값 예외처리로 바꾸기.
      return acc;
    }

    return {
      // status가 VALID가 아니면 실행
      status,
      ...(status !== VALIDATION_STATUS.VALID && { field }), // 이 구문을 아직도 이해못했음. 스프레드연산자가 어떤방식으로 동작하는지.. 요약하면 ...( True && {field} )인셈인데 출력되는 값은 결국 field값(name or nationalLanguage 같은) 출력됨.
    };
  }, {});
};

const { status, field } = checkValidStudent(student);
console.log("결과값 : ", status, field);
// name이 "" 빈값이면 ValidName 체크했을때 -> status : EMPTY // field : name 이 출력됨. 이거 참조해서 문법 수정하기.
```

> test 6

-> 자꾸 하나가안됨.

```js
name = "케케케";
nationalLanguage = 100;
english = 55;
math = 55;
const student = { name, nationalLanguage, english, math };
console.log("student : ", student);

const VALIDATION_STATUS = {
  TYPE_ERROR: "TYPE_ERROR",
  OUT_OF_RANGE: "OUT_OF_RANGE",
  EMPTY: "EMPTY",
  VALID: "VALID",
};

const VALIDATION_MESSAGE = {
  [VALIDATION_STATUS.OUT_OF_RANGE]: (field) =>
    `${field}값이 범위를 벗어났습니다. 올바른 값을 입력해주세요. (1~100)`,
  [VALIDATION_STATUS.TYPE_ERROR]: (field) =>
    `${field}의 형식이 올바르지 않습니다.`,
  [VALIDATION_STATUS.EMPTY]: (field) => `${field}값이 없습니다.`,
};

const checkValidName = (name) => {
  if (!name) {
    return VALIDATION_STATUS.EMPTY;
  }
  return typeof name === "string"
    ? VALIDATION_STATUS.VALID
    : VALIDATION_STATUS.TYPE_ERROR;
};

const checkValidScore = (score) => {
  if (!score) {
    return VALIDATION_STATUS.EMPTY;
  }
  if (typeof score !== "number") {
    return VALIDATION_STATUS.TYPE_ERROR;
  }
  return score < 0 || score > 100
    ? VALIDATION_STATUS.OUT_OF_RANGE
    : VALIDATION_STATUS.VALID;
};

const checkValidStudent = ({ name, ...scores }) => {
  if (checkValidName(name) !== VALIDATION_STATUS.VALID) {
    return { status: checkValidName(name), field: "name" };
  }

  console.log("scroes : ", scores);
  console.log("Obsject.entrise : ", Object.entries(scores));

  return Object.entries(scores).reduce((acc, [field, score]) => {
    const status = checkValidScore(score);
    console.log("시작acc :", acc);
    console.log("status :", status);
    console.log("field : ", field);
    console.log("score : ", score);

    if (acc.status !== VALIDATION_STATUS.VALID) {
      // stauts가 VALID면 acc반환해서 스킵.
      if (status !== VALIDATION_STATUS.VALID) {
        return { status, ...(status !== VALIDATION_STATUS.VALID && { field }) };
      } else {
        return acc;
      }
    }
  }, {});
};

const { status, field } = checkValidStudent(student);
console.log("결과값 : ", status, field);
// name이 "" 빈값이면 status : EMPTY // field : name 이 출력됨.
```

> test 7

case문 사용 -> not equal 기호 사용불가. -> 공부해보기 당장은 머리 과부화되서 안돌아감.

```js
name = "케케케";
nationalLanguage = 555;
english = 555;
math = 55;
const student = { name, nationalLanguage, english, math };
console.log("student : ", student);

const VALIDATION_STATUS = {
  TYPE_ERROR: "TYPE_ERROR",
  OUT_OF_RANGE: "OUT_OF_RANGE",
  EMPTY: "EMPTY",
  VALID: "VALID",
};

const VALIDATION_MESSAGE = {
  [VALIDATION_STATUS.OUT_OF_RANGE]: (field) =>
    `${field}값이 범위를 벗어났습니다. 올바른 값을 입력해주세요. (1~100)`,
  [VALIDATION_STATUS.TYPE_ERROR]: (field) =>
    `${field}의 형식이 올바르지 않습니다.`,
  [VALIDATION_STATUS.EMPTY]: (field) => `${field}값이 없습니다.`,
};

const checkValidName = (name) => {
  if (!name) {
    return VALIDATION_STATUS.EMPTY;
  }
  return typeof name === "string"
    ? VALIDATION_STATUS.VALID
    : VALIDATION_STATUS.TYPE_ERROR;
};

const checkValidScore = (score) => {
  if (!score) {
    return VALIDATION_STATUS.EMPTY;
  }
  if (typeof score !== "number") {
    return VALIDATION_STATUS.TYPE_ERROR;
  }
  return score < 0 || score > 100
    ? VALIDATION_STATUS.OUT_OF_RANGE
    : VALIDATION_STATUS.VALID;
};

const checkValidStudent = ({ name, ...scores }) => {
  if (checkValidName(name) !== VALIDATION_STATUS.VALID) {
    return { status: checkValidName(name), field: "name" };
  }

  console.log("scroes : ", scores);
  console.log("Obsject.entrise : ", Object.entries(scores));

  return Object.entries(scores).reduce((acc, [field, score]) => {
    const status = checkValidScore(score);
    console.log("시작acc :", acc);
    console.log("status :", status);
    console.log("field : ", field);
    console.log("score : ", score);

    switch (
      acc // stauts가 VALID면 acc반환해서 스킵.
    ) {
      case 0:
        if (status !== VALIDATION_STATUS.VALID) {
          return {
            status,
            ...(status !== VALIDATION_STATUS.VALID && { field }),
          };
        }
      default:
        return acc;
        console.log("acc가 0이 아닙니다.");
        break;
    }
  }, 0);
};

const { status, field } = checkValidStudent(student);
console.log("결과값 : ", status, field);
// name이 "" 빈값이면 status : EMPTY // field : name 이 출력됨.
```

> test 8

```js
name = "케케케";
nationalLanguage = 55;
english = 55;
math = 55;
const student = { name, nationalLanguage, english, math };
console.log("student : ", student);

const VALIDATION_STATUS = {
  TYPE_ERROR: "TYPE_ERROR",
  OUT_OF_RANGE: "OUT_OF_RANGE",
  EMPTY: "EMPTY",
  VALID: "VALID",
};

const VALIDATION_MESSAGE = {
  [VALIDATION_STATUS.OUT_OF_RANGE]: (field) =>
    `${field}값이 범위를 벗어났습니다. 올바른 값을 입력해주세요. (1~100)`,
  [VALIDATION_STATUS.TYPE_ERROR]: (field) =>
    `${field}의 형식이 올바르지 않습니다.`,
  [VALIDATION_STATUS.EMPTY]: (field) => `${field}값이 없습니다.`,
};

const checkValidName = (name) => {
  if (!name) {
    return VALIDATION_STATUS.EMPTY;
  }
  return typeof name === "string"
    ? VALIDATION_STATUS.VALID
    : VALIDATION_STATUS.TYPE_ERROR;
};

const checkValidScore = (score) => {
  if (!score) {
    return VALIDATION_STATUS.EMPTY;
  }
  if (typeof score !== "number") {
    return VALIDATION_STATUS.TYPE_ERROR;
  }
  return score < 0 || score > 100
    ? VALIDATION_STATUS.OUT_OF_RANGE
    : VALIDATION_STATUS.VALID;
};

const checkValidStudent = ({ name, ...scores }) => {
  if (checkValidName(name) !== VALIDATION_STATUS.VALID) {
    return { status: checkValidName(name), field: "name" };
  }

  console.log("scroes : ", scores);
  console.log("Obsject.entrise : ", Object.entries(scores));

  return Object.entries(scores).reduce((acc, [field, score]) => {
    const status = checkValidScore(score);
    console.log("시작acc :", acc);
    console.log("status :", status);
    console.log("field : ", field);
    console.log("score : ", score);

    if (status == VALIDATION_STATUS.VALID) {
      if (acc === 0) {
        return {
          status,
          ...(status !== VALIDATION_STATUS.VALID && { field }),
        };
      } else {
        console.log("acc : ", acc, "acc.status", acc.status);
        return acc;
      }
    }

    return {
      status,
      ...(status !== VALIDATION_STATUS.VALID && { field }),
    };
  }, 0);
};
const { status, field } = checkValidStudent(student);
console.log("결과값 : ", status, field);
// name이 "" 빈값이면 status : EMPTY // field : name 이 출력됨.
```

테스트 전부 성공. 기존에 짰던 로직 -> 오류는 잡는데 정상입력을 처리를 못헀음.

너무 오래붙들어서 과부화됐던듯. 이렇게 오래걸릴건 아녔던거같은데 아무튼 해결함.

오류처리도 잘되고 정상입력 처리도 잘됨.

reduce에서 acc 초기값을 설정하되 반환값을 별도로 설정안하면 초기값만 처음 출력하고 다음 배열 순회할땐 acc값 자체가 undefined 된다. 유의해야할 부분

# async / await

async functions 그리고 await 키워드는 ECMAScript2017에 추가되다. 이 기능들은 기본적으로 비동기 코드를 쓰고 Promise를 더 읽기 더 쉽도록 만들어준다.

비동기 함수를 async 함수로 만들기 위하여 function()앞에 async 키워드를 추가한다. async function()은 await 키워드가 비동기 코드를 호출할 수 있게 해주는 함수이다.

> 예제

```js
function hello() {
  return "Hello";
}
hello();
("Hello");
```

위의 함수는 단순히 Hello만을 출력한다. 그러나 여기 앞에 async를 추가한면

> 예제

```js
async function hello() { return "Hello" };
hello();
Promise { <state>: "fulfilled", <value>: "Hello" }
```

코드가 promise를 반환한다. `async` 키워드를 사용하면 반환받는 값은 Promise가 된다.

다음과 같은 형태로 사용해도 같은 결과 값을 갖는다.

> 예제

```js
let hello = async function() { return "Hello" };
hello();
Promise { <state>: "fulfilled", <value>: "Hello" }
```

화살표 함수로 사용한다면 다음과 같다.

```js
let hello = async () => { return "Hello" };
hello();
Promise { <state>: "fulfilled", <value>: "Hello" }
```

async는실제로 fulfil Promise가 반환되기 때문에 반환된 값을 사용하기 위해선 .then() 블럭을 사용해야 한다.

> 예제

```js
hello().then((value) => console.log(value)); // 콘솔창에 hello 출력
```

짧게 표현하면 다음과 같이 표현도 가능하다.

```js
hello().then(console.log);
```

정리하면, `async` 를 함수와 같이 사용하면 결과를 직접 반환하는게 아니라 Promise를 반환하게 한다.

또한 동기식 함수는 await사용을 위한 지원과 함께 실행되는 잠재적인 `오버헤드`를 피할 수 있다.

## 오버헤드란 ?

`오버헤드`란 프로그램의 실행흐름에서 나타나는 현상중 하나이다.

예를 들어 , 프로그램의 실행흐름 도중에 동떨어진 위치의 코드를 실행시켜야 할 때, 추가적으로 시간,메모리,자원이 사용되는 현상이다.

이러한 현상은 특히 프로그래밍 시에 외부 함수를 사용할 때 나타난다.

실행 흐름이 도중에 끊겨버리고 , 함수를 사용하기 위해 스택메모리를 할당한다.

이 때 매개변수가 있다면 대입연산까지도 일어난다. 이 외에도 함수를 호출하기 위해 많은 과정을 진행하게 된다.

이 때 예상하지 못하는 자원들이 소모되는 현상이 바로 `오버헤드 현상`이다.

## 비동기 키워드

비동기 함수를 `await 키워드`와 함께 쓰면 그 장점이 확실히 보인다.

이것은 어떠한 Promise기반 함수 앞에 놓을 수 있다.

그리고 우리 코드의 Promise가 fulfil될 때 까지 잠시 중단하고, 결과를 반환한다.. 그리고 실행을 기다리는 다른 코드들을 중지시키지 않고 그대로 실행되게 한다.

`await 키워드`는 웹 API를 포함하여 Promise를 반환하는 함수를 호출할 때 사용할 수 있다.

> await 간단 예제

```js
async function hello() {
  return (greeting = await Promise.resolve("Hello"));
}

hello().then(alert); // alert로 Hello 출력
hello().then(console.log); // console.log로 Hello 출력
```

> Fetch() 예제

```js
// 변환전
fetch("coffee.jpg")
  .then((response) => response.blob())
  .then((myBlob) => {
    let objectURL = URL.createObjectURL(myBlob);
    let image = document.createElement("img");
    image.src = objectURL;
    document.body.appendChild(image);
  })
  .catch((e) => {
    console.log(
      "There has been a problem with your fetch operation: " + e.message,
    );
  });
```

위 예제를 async/await를 사용해서 바꾸면 다음과 같이 변경된다.

```js
// async/await 사용하여 변경
async function myFetch() {
  let response = await fetch("coffee.jpg");
  let myBlob = await response.blob();

  let objectURL = URL.createObjectURL(myBlob);
  let image = document.createElement("img");
  image.src = objectURL;
  document.body.appendChild(image);
}

myFetch().catch((e) => {
  console.log(
    "There has been a problem with your fetch operation: " + e.message,
  );
});
```

바꾸고 나니 더 이해하기 쉬워졌다. — 더 이상의 .then() 블럭은 찾아 볼 수 없다.

`async 키워드`가 함수를 Promise로 바꾸었기, 이제 promise 와 `await`의 하이브리드 접근방식을 사용하기 위해 코드를 리팩토링 할 수 있으며, 두 번째 .then()블럭을 함수 내부의 블럭으로 가져와 더 유연하게 만들 수 있다.

```js
// 리팩토링

async function myFetch() {
  let response = await fetch("coffee.jpg");
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return await response.blob();
}

myFetch()
  .then((blob) => {
    let objectURL = URL.createObjectURL(blob);
    let image = document.createElement("img");
    image.src = objectURL;
    document.body.appendChild(image);
  })
  .catch((e) => console.log(e));
```

## 어떻게 동작하는가 ?

함수 안에 코드를 작성했고, function 키워드 앞에 async 키워드를 썼다는 것을 알 수 있다. 반드시 이렇게 사용해야 한다.

비동기 코드를 실행할 블럭을 정의하려면 비동기 함수를 생성해야 한다. `await`는 `async function` 안에서만 쓸 수 있다.

예제로 사용한 myFetch() 함수 내에 코드가 이전의 Promise버전과 매우 유사하지만, 다른점이 있다.

.then()블럭을 사용하여 작업을 이어가는 대신 메서드 호출 전에 `await 키워드`를 사용하여 반환된 결과를 변수에 할당한다.

`await 키워드`는 JavaScript 런타임이 이 라인에서 비동기 코드를 일시 중지하여 비동기 함수 호출이 결과를 반환할 때 까지 기다리게 한다.

그러나 외부의 다른 동기 코드는 실행될 수 있도록 한다. 작업이 완료되면 코드는 계속 이어져서 실행된다.

예를들면 아래와 같다.

```js
let response = await fetch("coffee.jpg");
```

fulfilled된 fetch() Promise에서 반환된 응답은 해당 응답이 사용할 수 있게 되면 `response 변수`에 할당된다.

그리고 `parser`는 해당 응답이 발생할 때 까지 이 라인에서 일시 중지된다. response가 사용 가능하게 되면, `parser`는 다음 라인으로 이동하게 되고 그 라인에서 `Blob` 을 생성하게 된다.

이 라인도 Promise기반 비동기 메서드를 호출하므로, 여기서도 `await` 을 사용한다. 비동기 작업 결과가 반환되면, myFetch() 함수가 그 결과를 반환한다.

myFetch() 함수를 호출하면, Promise를 반환하므로, 따라서 화면에 Blob을 표시해주는 .then() 코드 블럭 체이닝 할 수 있다.

이렇게하면 .then() 블럭이 줄어들고 대부분이 동기 코드처럼 보이기 때문에 정말 직관적이게 된다.

완벽하게 이해한 부분은 아니지만 이러한 방식으로 처리 된다는 것만을 기억하자.

# Blob

너무 낯선 개념이라 추후에 추가로 활용할 떄 더 자세히 정리할 필요가 있는 부분.

Blob 객체는 파일류의 불변하는 미가공 데이터를 나타낸다.

텍스트와 이진 데이터의 형태로 읽을 수 있다.

Blob은 JavaScript 네이티브 형태가 아닌 데이터도 표현할 수 있다.

`Blob`을 생성하려면 Blob() 생성자를 사용하면 된다.

## 생성자

- `Blob()`

매개변수로 제공한 배열의 모든 데이터를 합친 데이터를 담은 새로운 Blob 객체를 반환한다.

## 속성

- Blob.size (Read only)
  Blob 객체가 담은 데이터의 바이트 단위의 사이즈이다..
- Blob.type (Read only)
  Blob 객체가 담은 데이터의 MIME 유형을 나타내는 문자열이다. 유형을 알 수 없는 경우 빈 문자열을 반환한다.

## 메서드

- Blob.arrayBuffer()
  Blob의 전체 내용을 이진 데이터로 담은 ArrayBuffer로 이행하는 Promise를 반환합니다

- Blob.slice()
  메서드를 호출한 블롭의 바이트를 주어진 시작 바이트와 끝 바이트 범위에서 복제해 새로운 Blob 객체를 생성하고 반환합니다.

- Blob.stream()
  Blob의 콘텐츠를 읽을 수 있는 ReadableStream을 반환합니다.

- Blob.text()
  Blob의 전체 내용을 UTF-8 텍스트로 담은 USVString으로 이행하는 Promise를 반환합니다.

> 예제

블롭 생성 예제는 다음과 같다.

```js
const obj = { hello: "world" };
const blob = new Blob([JSON.stringify(obj, null, 2)], {
  type: "application/json",
});
```

## 형식 배열의 콘텐츠를 나타내는 URL 생성하기

다음 코드는 JavaScript [TypedArray](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)를 생성한 후, 그 데이터를 담은 Blob 객체도 만든다. 그 후, [URL.createObjectURL()](https://developer.mozilla.org/ko/docs/Web/API/URL/createObjectURL)을 호출해 블롭을 URL로 변환한다.
