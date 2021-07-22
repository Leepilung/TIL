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
