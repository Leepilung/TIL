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
