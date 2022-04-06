# Front-end

프론트엔드 전반적인 내용, 리액트, 자바스크립트에 관한 면접을 베이스로 면접 내용을 진행하자.

# 브라우저의 렌더링 원리

브라우저가 화면에 나타나는 요소를 렌더링 할 때에는 웹킷(Webkit)이나 게코(Gecko)등과 같은 `렌더링 엔진`을 사용한다. 렌더링 엔진이 HTML, CSS, JavaScript로 렌더링할 때 CRP(Critical Rendering Path)라는 프로세스를 사용하며 다음의 단계가 이뤄진다.

1. HTML 파일 파싱 후, DOM(Document Object Model) 트리 구축 (Parsing)

2. CSS 파일 파싱 후, CSSOM(CSS Object Model) 트리 구축 (Parsing)

3. Javascript 실행

    ! 주의 사항 : 이 때 HTML 중간에 스크립트가 있다면 스크립트가 해석 및 실행되는 동안 HTML 파싱이 중단된다.

4. DOM과 CSSOM을 조합하여 렌더링 트리(Rendering Tree) 구축 (Style)

    ! 주의 사항 : `visibility: hidden`은 요소가 공간을 차지하고, 보이지만 않기 때문에 Render Tree에 포함이 되지만, `display: none` 의 경우 Render Tree에서 제외된다.

5. 렌더링 트리(Rendering Tree)에서 각 노드의 위치와 크기를 계산한다.(Layout)

6. 계산된 값을 이용하여 각 노드를 화면상의 실제 픽셀로 변환, 레이어를 만든다.(Paint)

# CSR && SSR

CSR(Client Side Rendering)과 SSR(Server Side Rendering)은 대척 관계에 있는 방식인만큼 장단점이 서로 엇갈려 있다.
따라서 서로의 장단을 정확하게 알고, 적재적소에 필요한 방식으로 구현하는 것이 중요하다.

-   SSR 단계
    <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdGCZHY%2FbtrcOfdcohI%2FDKF2Cr2HHW5X8vNSaexEpK%2Fimg.png">

-   CSR 단계
    <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbkJ0my%2FbtrcOM9GT1V%2FaKDCRhm77MfHF8ushplGi0%2Fimg.png">

## 차이점

1. 웹페이지의 로딩 시간은 크게 2개로 나눌 수 있다.
    - 웹페이지 로딩은 크게 첫 페이지를 로딩하는 것.
    - 나머지를 로딩하는 것

CSR의 경우 HTML, CSS, 모든 스크립트를 한번에 불러온다. 반면 SSR은 필요한 부분의 HTML과 스크립트만 불러온다. 고로 평균적인 속도는 SSR이 더 빠르다.

그러나 나머지 로딩 시간(즉, 첫 페이지를 로딩한 후의 로딩 시간)의 경우에는 CSR은 이미 첫 페이지 로딩시 나머지 부분을 구성하는 코드를 전부 가져오기 때문에 빠르다.

반면, SSR은 첫페이지를 로딩한 과정을 정확하게 다시 실행하기 때문에 비교적 더 느리다.

## 사용 권장 예시

-   SSR의 경우

1. 네트워크가 느릴 경우에 사용
2. SEO(Search Engine Optimization : 검색 엔진 최적화)가 필요할 경우
3. 최초 로딩이 빨라야하는 사이트를 개발 하는 경우
4. 메인 스크립트가 크고 로딩이 매우 느릴 때
5. 웹 사이트가 상호작용이 별로 없을 때

-   CSR 사용의 경우

1. 네트워크가 빠를 때
2. 서버의 성능이 좋지 않을 때
3. 사용자에게 보여줘야 하는 데이터의 양이 많을 때(로딩 창 사용 쌉가능)
4. 메인 스크립트가 가벼울 때
5. SEO 를 고려하지 않을 때
6. 웹 어플리케이션과 사용자와 상호작용이 많을 때

# SPA(Single Page Application) 이란?

## 배경

SPA를 설명하려면 과거의 웹 사이트에 대해 설명할 필요가 있다.

과거 웹사이트는 지금보다 문서 하나에 전달되는 파일의 용량이 적었다. 어떤 요소를 한번 클릭하면 완전히 새로운 페이지를 서버에서 전송해 주곤 했다.

그러나 현대에 이르러 한 페이지에 해당하는 페이지 용량이 커졌고, 매번 새로운 페이지를 전달하는게 버거워졌다.

## 그래서 `SPA`란?

이러한 문제를 해결하기 위해 등장한 것이 SPA. 어떤 웹사이트의 전체 페이지를 하나의 페이지에 담아 동적으로 화면을 바꿔가며 표현하는 것이 SAP이다.

뭔가를 클릭하거나 스크롤하면, 상호작용하기 위한 최소한의 요소만 변경이 일어난다.

'페이지 변경이 일어난다고 보여지는 것' 또한 최초 로드된 자바스크립트를 통해 미리 브라우저에 올라간 템플릿만 교체되는 것이다.

## SPA 프레임워크가 하는 일

SPA 프레임워크로 유명한 Angular, React, Vue가 하는 일은 세부적인 구현 개념은 전부 다르지만, 그 목적은 모두 SPA를 쉽고 확장성 있게 구현하는 것을 목표로 Virtual DOM이라는 개념을 사용해 SPA를 구현한다.

SPA의 문제점은 자바스크립트로 인한 DOM 조작이 빈번하게 일어나 브라우저의 성능을 저하신킨다는 것이다.

Virtual DOM을 사용하는 프레임워크들은 실제 DOM 트리를 흉내 낸 가상의 객체 트리로 html 정보를 저장하고 있다가, 이 트리에 변경이 발생하면 모든 변화를 모아 단 한번 브라우저를 호출해 화면을 갱신하는 방법을 사용한다. 이렇게 하면 브라우저와의 불필요한 상호작용을 최소화하면서 인터렉티브한 웹 사이트를 만드는 것이 가능하다.

# JavaScript

# JavaScript의 동작원리에 대해서

Javascript의 동작원리를 간단하게 설명하면 다음과 같이 설명할 수 있다.

1. 싱글스레드 기반으로 동작하는 자바스크립트
2. 이벤트 루프를 기반으로 하는 싱글 스레드 Node.js

## Javascript Engine?

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

`var` keyword로 선언한 모든 변수 선언은 호이스트 된다. 한마디로 호이스트란 변수의 정의가 그 범위에 따라 선언과 할당으로 분리되는 것을 의미한다.

즉 변수가 함수 내에서 정의된 경우, 선언이 함수의 최상단으로, 함수 바깥에서 정의된 경우에는 전역 컨텍스트의 최상위로 변경된다.

`할당`은 그 다음 런타임 과정에서 이뤄지기 때문에 할당 구문은 호이스팅 되지 않는다.

-   여기서 중요한 점

## 함수 표현식(Funtion Expression)

var 변수이름 = function 함수이름(매개변수) {로직}의 형태는 데이터 구조로 할당되기 때문에 런타임 과정에서 처리되어 호이스팅이 불가능하다.

함수 리터럴에 의한 표현이 이에 해당된다.

# 클로저(Closure)란?

클로저(Closure)의 정의는 `외부 함수에 접근할 수 있는 내부 함수 혹은 이러한 원리`를 의미한다.

즉 내부함수가 외부함수의 변수등에 접근할 수 있는 것을 가르킨다. 그러나 그 반대는 실현이 불가능하다는 개념이다.

또한 클로저 안에 정의된 함수는 만들어진 환경을 ‘기억한다’. 여기서 `환경`이라 함은 클로저가 생성될 때 그 `범위`에 있던 여러 지역 변수들이 포함된 context를 의미한다.

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

# 상태 관리 라이브러리란 ?

리액트는 단방향 바인딩을 지원하기 때문에 부모에서 자식으로만 state를 props로 전달할 수 있고, 자식의 props를 부모에게 직접 전달할 수는 없다.

자식에서 부모의 상태를 바꾸려면 해당 상태를 컨트롤하는 함수를 props로 넘겨주어야 한다.

하지만 이것이 반복되다 보면 엄청난 `props drilling`이 발생하게 된다는 문제가 있다. 프로젝트의 규모가 커질수록 props의 뎁스가 증가하게 되고, 이는 불필요한 리렌더링을 유발할 수도 있다.

리덕스가 나오기 이전, 리액트를 포함한 대부분의 프로젝트는 `MVC 아키텍쳐(Model-View-Controller)`가 많이 사용되었다. 컨트롤러가 여러 모델을 제어하고, 모델과 뷰가 서로 바라보는 구조로, 모델가 뷰가 양방향으로 영향을 미쳐 프로젝트 규모가 커질 수록 상태관리가 복잡하고 어렵다.

<img src="https://media.vlpt.us/images/danmin20/post/9b658196-ee2e-466f-9d45-2bcb943b7614/image.png">

이러한 문제를 해결하기 위해 페이스북이 내놓은 새로운 아키텍쳐가 `Flux 아키텍쳐`이다.

데이터의 흐름이 단방향으로 흐르는 구조이다.

<img src="https://media.vlpt.us/images/danmin20/post/28783b5d-fe8c-4a5f-9834-358ffea74922/image.png">

# Redux가 무엇인가?

페이스북이 개발한 Flux 아키텍쳐의 대표적인 라이브러리이다.

## 장점

-   Redux는 오직 하나의 스토어만을 가지며, 하나의 객체 트리를 가지기 때문에 개발 확장성 및 디버깅에 강점이 있다.
-   스토어 내부의 상태는 action 객체에 의해서만 변경될 수 있다. 모든 상태 변화들이 하나의 store에 집중되어 있고, 단방향성이 기 때문에 항상 예측 가능한 결과를 낳게 된다.

## 단점

-   보수적인 접근 방식으로 인해 높은 러닝 커브를 지니고 있다.(배우기 어려움)
-   큰 보일러 플레이트를 가진다.(보일러 플레이트 코드의 사용이 좀더 어렵다로 이해하면 될듯.)

# Recoil

페이스북에서 내놓은 새로운 상태관리 라이브러리.

리코일은 아톰과 셀렉터로 이루어져 있ㄹ다.
아톰은 상태의 단위로, 유니크한 키값으로 구분된다. 해당 아톰을 구독하고 있으면 해당 컴포넌트들만 선택적으로 리렌더링된다.

다만 아직 버전이 낮아 안정성 측면에서 낮고, DevTool이 미흡하다고 한다.

# Context API

리액트가 자체적으로 가지고 있다. 정적인 데이터 위주로 처리하거나 업데이트가 빈번하지 않을 떄 적합하다.

Provider-Consumer의 구조로 상태를 주고 받는데, Provider 하위의 모든 Consumer는 Provider의 속성이 변경될 때마다 리렌더링 된다는 단점이 존재한다.

## useMemo나 useReducer와 함께 사용하면 좋은 코드 작성이 가능할 것 같다.

# CSS

# TypeScript에 대해서 사용해봤는가? 어떻게 생각하는가?

정적 타이핑과 동적 타이핑의 관점에서 다소 의견이 분분하고 나또한 사용하진 않은 입장으로써 뭐가 더 나은지는 감히 말하기 힘들다.

허나 정적 타입을 지원함으로써 코드 안정성이 올라가는 측면은 짧은 소견으로도 동의하는 바.


----------------------------------

비전공자로서의 선입견등이 존재.

CS기초에 대해서 얼마나 아는지

전공자로서 더 뛰어나다는걸 보여줘야된다.

나만의 메리트가 확실해야함.->나만의무기로는 부족함
