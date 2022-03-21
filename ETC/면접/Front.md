# Front-end

프론트엔드 전반적인 내용, 리액트, 자바스크립트에 관한 면접을 베이스로 면접 내용을 진행하자.

# 브라우저의 렌더링 원리

브라우저가 화면에 나타나는 요소를 렌더링 할 때에는 웹킷(Webkit)이나 게코(Gecko)등과 같은 `렌더링 엔진`을 사용한다. 렌더링 엔진이 HTML, CSS, JavaScript로 렌더링할 때 CRP(Critical Rendering Path)라는 프로세스를 사용하며 다음의 단계가 이뤄진다.

1. HTML 파싱 후, DOM(Document Object Model) 트리 구축
2. CSS 파싱 후, CSSOM(CSS Object Model) 트리 구축
3. Javascript 실행

    ! 주의 사항 : 이 때 HTML 중간에 스크립트가 있다면 스크립트가 해석 및 실행되는 동안 HTML 파싱이 중단된다.

4. DOM과 CSSOM을 조합하여 렌더트리(Render Tree) 구축

    ! 주의 사항 : display : none 속성과 같이 화면에서 보이지도 않고 공간을 차지하지 않는 것들은 렌더트리로 구축되지 않는다.

# JavaScript

# JavaScript의 동작원리에 대해서

Javascript의 동작원리를 간단하게 설명하면 다음과 같이 설명할 수 있다.

1. 싱글스레드 기반으로 동작하는 자바스크립트
2. 이벤트 루프를 기반으로 하는 싱글 스레드 Node.js

## Javascript Engined?

JavaScript를 해석하는 JavaScript Engine과 웹 브라우저에 화면을 그리는 Rendering Engine은 서로 다르다.

Rendering Engine은 HTML, CSS로 작성된 마크업 관련된 코드들을 콘텐츠로서 웹 페이지에 말글대로 'rendering'하는 역할을 한다.

JavaScript Engine은 JavaScript로 작성한 코드를 해석하고 실행하는 인터프리터에 해당한다.

때문에 구글에서 개발한 V8을 비롯한 대부분의 자바스크립트 엔진은 크게 세 영역으로 나뉜다.

Call Stack, Task Queue(=Event Queue), Heap

그리고 추가적으로 'Event loop'라는 녀석이 존재하여 Task queue에 들어가는 task를 관리하게 된다.
<img src="https://t1.daumcdn.net/cfile/tistory/225AF03B58E4956C26">

콜스택 이후부턴 이 블로그 내용으로 마저 정리하기. https://asfirstalways.tistory.com/362

# 호이스팅(Hoisting)이란?

hoist란 단어의 사전적 정의는 끌어올리기 라는 뜻이다. 그리고 자바스크립트에서 끌어올려지는 것은 변수이다.

`var` keyword로 선언한 모든 변수 선언은 호이스트 된다. 한마디로 호이스트란 변수의 정의가 그버뮈에 따라 선언과 할당으로 분리되는 것을 의미한다.

즉 변수가 함수 내에서 정의된 경우, 선언이 함수의 최상단으로, 함수 바깥에서 정의된 경우에는 전역 컨텍스트의 최상위로 변경된다.

`할당`은 그 다음 런타임 과정에서 이뤄지기 때문에 할당 구문은 호이스팅 되지 않는다.

-   여기서 중요한 점

함수 표현식(Funtion Expression)

var 변수이름 = function 함수이름(매개변수) {로직}의 형태는 데이터 구조로 할당되기 때문에 런타임 과정에서 처리되어 호이스팅이 불가능하다.

함수 리터럴에 의한 표현이 이에 해당된다.

# 클로저(Closure)란?

클로저(Closure)는 `두 개의 함수로 만들어진 환경`으로 이뤄져 독립적인 변수를 가리키는 함수이다. 또한 클로저 안에 정의된 함수는 만들어진 환경을 ‘기억한다’.

여기서 `환경`이라 함은 클로저가 생성될 때 그 `범위`에 있던 여러 지역 변수들이 포함된 context를 의미한다.

이 클로저를 통해서 자바스크립트에는 없는 비공개(private) 속성,메소드를 만드는 은닉화를 할 수 있으며, 콜백 함수등을 사용할 때 발생할 수 있는 에러를 해결하는데도 유용하다.

# this에 대해서

자바스크립트에서 모든 함수는 실행될 때마다 함수 내부에 this라는 객체가 추가된다. arguments라는 유사 배열 객체와 함께 함수 내부로 암묵적으로 전달된다.

자바스크립트의 경우 함수 호출 방식에 의해 this에 바인딩할 어떤 객체가 동적으로 결정된다.

다시 말해, 함수를 선언할 때 this에 바인딩할 객체가 정적으로 결정되는 것이 아니고, 함수를 호출할 때 함수가 어떻게 호출되었는지에 따라 this에 바인딩할 객체가 동적으로 결정된다.

# 이벤트 버블링 - Event Bubbling

이벤트 버를링은 특정 화면 요소에서 이벤트가 발생했을 때 해당 이벤트가 더 상위의 화면 요소들로 전달되어 가는 특성을 의미한다.

<img src="https://joshua1988.github.io/images/posts/web/javascript/event/event-bubble.png">

-   상위의 화면 요소란?

    HTML 요소는 기본적으로 트리 구조를 갖는다. 여기서는 트리 구조상 한단꼐 위의 요소를 상위 요소라 한다. body 태그는 최상위 요소라고 부른다.

# 이벤트 캡쳐 - Event Capture

이벤트 캡쳐는 버블링과 반대 방향으로 진행되는 이벤트 전파 방식이다.

<img src="https://joshua1988.github.io/images/posts/web/javascript/event/event-capture.png">

코드로 구현하면 다음과 같게 된다.

```html
<body>
    <div class="one">
        <div class="two">
            <div class="three"></div>
        </div>
    </div>
</body>
```

```js
var divs = document.querySelectorAll("div");
divs.forEach(function (div) {
    div.addEventListener("click", logEvent, {
        capture: true, // default 값은 false입니다.
    });
});

function logEvent(event) {
    console.log(event.currentTarget.className);
}
```

# 화살표 함수의 this

일반 함수는 함수를 선언할 때 this에 바인딩할 객체가 정적으로 결정되지 않고, 동적으로 되지만

화살표 함수는 함수를 선언할 때 this에 바인딩할 객체가 정적으로 결정된다. 화살표 함수의 this는 언제나 상위 스코프의 this를 가리키게 된다.

---

# React

React는 Facebook에서 만든 JavaScript 라이브러리이다.

# React의 사용 이유

배우기가 쉽다. 구문이 간편하고 바닐라 자바스크립트에 비해 동적인 웹 애플리케이션 구현이 쉬웠음.

높은 수준의 유연성과 응답성, 하위 데이터 바인딩등이 굉장히 간단했다.

# Redux가 무엇인가?

React를 사용하여 개발을 하다보면 애플리케이션의 규모가 커지는데 구조가 복잡해지면서 컴포넌트의 상태관리또한 복잡해지게 되는데 이를 방지 하기 위헤 사용하는 상태관리 라이브러이이다.

---

# CSS

# TypeScript에 대해서 사용해봤는가? 어떻게 생각하는가?

정적 타이핑과 동적 타이핑의 관점에서 다소 의견이 분분하고 나또한 사용하진 않은 입장으로써 뭐가 더 나은지는 감히 말하기 힘들다.

허나 정적 타입을 지원함으로써 코드 안정성이 올라가는 측면은 짧은 소견으로도 동의하는 바.
