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
