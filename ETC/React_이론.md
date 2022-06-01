# React 이론 정리

복습용으로 최대한 축약하여 이해하는데 있어 어색함이나 부족함 없게끔 정리하는 것이 목표.

# 🚩 React란?

리액트는 자바스크립트 라이브러리로 사용자 인터페이스(User Interface)를 만드는데 사용하고 오직 `뷰(View)`만을 신경 쓰는 라이브러리이다.

리액트 프로젝트에서 특정 부분이 어떻게 생길지 정하는 선언체가 있는데, 이를 `컴포넌트(component)`라고 한다.

컴포넌트(component)는 재사용이 가능한 AIP로 수많은 기능을 내장하며, 해당 컴포넌트의 생김새와 작동 방식을 정의한다.

이어서 사용자 화면에 뷰(View)를 보여 주는 것을 `렌더링(rendering)`이라고 부르는데 리액트에는 초기 렌더링과 리렌더링 두 개념으로 나뉜다.

## 📕 초기 렌더링

어떠한 UI 관련 프레임워크나 라이브러리던 맨 처음에 어떻게 보일지를 정하는 초기 렌더링은 필요한데 리액트에서는 이 역할을 render 함수가 담당한다.

```js
render() {...}
```

이 함수는 컴포넌트가 어떻게 생겼는지를 정의하며 뷰가 어떻게 생겼고, 어떻게 작동하는지에 대한 정보를 지닌 객체를 반환한다.

이 함수(render())를 실행하면 내부의 컴포넌트들을 렌더링 하게되고 최상위 컴포넌트의 렌더링 작업이 끝나면 지닌 정보를 이용해 HTML 마크업을 만들고, 이를 실제 페이지의 DOM 요소 안에 주입한다.

<img src="https://thebook.io/img/080203/037.jpg">

그다음 문자열 형태의 HTML 코드를 생성한 후 특정 DOM에 해당 내용을 주입하면 이벤트가 적용된다.

## 📗 리 렌더링

리액트에서 업데이트에 해당하는 리 렌더링(or 업데이트)는 데이터의 변화가 있을 때 변화에 맞춰 뷰를 변형시키는 것이 아니라 새로운 요소로 갈아 끼우는 것이다.

이 작업또한 `render()` 함수가 맡는다. 컴포넌트는 데이터를 업데이트했을 때 단순히 업데이트한 값을 수정하는 것이 아닌, 새로운 데이터로 render 함수를 다시 호출하고 그 데이터르 지닌 뷰를 다시 생성하는 것이다.

그러나 이렇게 render 함수가 새로운 뷰에 대한 반환 결과를 곧바로 DOM에 반영하지 않고 `이전`의 render() 함수가 만들었던 컴포넌트 정보와 `현재` render() 함수가 만든 컴포넌트 정보를 비교한다.

<img src="https://thebook.io/img/080203/038.jpg">

이후 자바스크립트를 사용하여 두 가지 뷰를 최소한의 연산으로 비교한 후, 둘의 차이를 알아내 최소한의 연산으로 DOM 트리를 업데이트한다.

<img src="https://thebook.io/img/080203/038_2.jpg">

방식 자체는 루트 노드부터 전체 컴포넌트를 다시 렌더링하는 것처럼 보이지만, 최적의 자원을 사용하여 수행하는 방식인 것이다.

# 📚 리액트의 특징

리액트의 주요 특징 중 하나는 Virtual DOM을 사용한다는 것이다. 그러나 이를 알기 위해선 우선 DOM에 대해 알 필요가 있다.(정리가 안되어 있음)

## ❓ DOM 이란?

DOM = Document Object Model의 약어로 객체로 문서 구조를 표현하는 방법이며 XML, HTML등의 방식으로 작성한다.

웹 브라우저는 DOM을 활용하여 객체에 자바스크립트와 CSS를 적용한다. `DOM`은 트리 형태라서 특정 노드를 찾거나 수정하거나 제거하거나 원하는 곳에 삽입할 수 있다.

<img src="https://thebook.io/img/080203/039.jpg">

DOM API는 수많은 플랫폼과 웹 브라우저에서 사용하지만, 한가지 치명적인 문제가 있는데 동적인 UI에 최적화 되어있지 않다는 것이다.

HTML은 그 자체적으로는 정적이며 자바스크립트를 활용하여야 동적으로 만들 수 있다.

예를 들어 페이스북 같은 경우 포스트 한 개가 표현하는 `<div>`요소는 100개 가량 됟나. 이렇게 규모가 큰 웹 어플리케이션에서 DOM에 직접 접근해 변화를 주면 나중에는 느려지는 성능 이슈가 발생할 수 밖에 없다.

그러나 DOM 자체는 매우 빠르다. DOM 자체를 읽고 쓸 때의 성능은 자바스크립트 객체를 처리할 때의 성능과 비교하여 크게 다르지 않다.

다만 웹 브라우저 단에서 DOM에 변화가 일어날 때 웹 브라우저가 CSS를 다시 연산하고, 레이아웃을 구성하고, 페이지를 리페인트 하기 때문에 이 과정에서 시간이 허비된다.

> 해결법

HTML 마크업을 시각적인 형태로 변환하는 것은 웹 브라우저의 주 역할이고, 이를 처리할 때 컴퓨터 자원을 사용하는 것은 어쩔 수 없다.

때문에 DOM을 조작할 때마다 엔진이 웹 페이지를 새로 그리기 때문에 이런 DOM을 최소한으로 조작하여 작업을 처리하는 방식으로 개선이 가능한데 리액트가 바로 `Virtual DOM 방식`을 이용하여 DOM 업데이트를 추상화함으로 DOM 처리 횟수를 최소화하고 효율적으로 진행한다.

## 📗 Virtual DOM

이전에 UI가 데이터를 표현했다 -> 데이터가 변경되면 UI의 상태를 확인하고 그 상태에 따라 UI를 바꿔줬다. 내가 표현하고 싶은 상태가 UI에 있었다.

그러나 나는 상태를 그리고 이 상태에 따른 UI를 정의하는 방식이 Virtual DOM이다.

virtual DOM -> map 으로 데이터를 뿌리는 방식.

Virtual DOM은 실제 DOM에 접근하여 조작하는 대신, 이를 추상화한 자바스크립트 객체를 구성하여 사용한다. 실제 DOM의 가벼운 사본이라고 생각하면 편할듯 하다.

리액트에서 데이터가 변하면 웹 브라우저에 실제 DOM을 업데이트하는 데에는 다음의 세 가지 단계가 있다.

1. 데이터를 업데이트 하면 전체 UI를 Virtual DOM에 리렌더링한다.
2. 이전 Virtual DOM에 있던 내용과 현재 Virtual DOM의 내용을 비교한다.
3. 바뀐 부분만 실제 DOM에 적용한다.

<img src="https://thebook.io/img/080203/041.jpg">

그러나 Virtual DOM을 사용한다고 사용하지 않을때와 비교해서 무조건 빠르지 않다.

리액트는 `지속적으로 데이터가 변화하는 대규모 어플리케이션 구축하기`라는 목적이 있다.

리액트와 Virtual DOM이 언제나 제공하는 것은 업데이트 처리 간결성이다. UI를 업데이트하는 과정에서 생기는 복잡합을 모두 해소하고, 더욱 쉽게 업데이트 할 수 있게 해준다.

## 📕 리액트의 기타 특징

일부 웹 프레임워크가 MVC(Model-View-Controller)나 MVW(Model-View-Whatever // ex : AngularJS)등의 구조가 아닌 오직 뷰(View)만 담당한다.

또한 리액트는 프레임워크가 아닌 라이브러리이다. 다른 웹 프레임워크가 Ajax, 데이터 모델링, 라우팅 등의 기능을 내장하고 있는 반면, 리액트는 뷰(View)만 신경 쓰는 라이브러리이므로 기타 기능은 직접 구현하여 사용해야 한다.

그러나 이러한 부분들 또한 리액트 라우터(react-router), Ajax 처리를 위한 axios나 fetch, 상태 관리에 리덕스(redux)나 MobX등을 사용하면 된다.

<img src="https://thebook.io/img/080203/042.jpg">

또한 리액트는 다른 웹 프레임워크나 라이브러리와 혼용이 가능하다. Backbone.js나 AngularJS 등의 프레임워크와도 언제든 사용이 가능하다.

<img src="https://thebook.io/img/080203/042_2.jpg">

## 📘 리액트 개발 도구

리액트 프로젝트를 생성하는데 있어서 Node.js(크롬 V8 자바스클비트 엔진으로 빌드한 자바스크립트 런타임)는 필수다.

리액트 애플리케이션은 웹 브라우저에서 실행되는 코드로 주로 사용하는 개발 도구로는 ECMAScript6를 호환시켜 주는 `바벨(babel)`, 모듈화된 코드를 한 파일로 합치고(번들링) 코드를 수정할 떄마다 웹 브라우저를 리로딩 하는 등의 여러 기능을 지닌 `웹팩(webpack)`등이 있다.

## 📙 create-react-app

`create-react-app`은 리액트 프로젝트를 생성할 때 필요한 `웹팩`, `바벨`의 설치 및 설정 과정을 생략하고 바로 간편하게 프로젝트 작업 환경을 구축해 주는 도구이다.

터미널에 다음과 같이 입력하면 된다.

**$ npm create react-app hello-react**

## 📒 번들러(bundler)

위의 명령어로 리액트 프로젝트를 만들면 다음과 같은 구문을 맞이하게된다.

```js
import React from "react";
```

이 코드는 리액트를 불러와서 사용할 수 있게 해준다. 리액트 프로젝트 생성 시 node_modules라는 디렉터리가 생성되는데 여기에 react 모듈이 같이 설치되고, 위와 같은 구문으로 리액트를 불러와 사용할 수 있다.

모듈을 사용하는 것은 원래 브라우저에는 없는 기능이다. 브라우저가 아닌 환경에서 JavaScript를 실행할 수 있게 해주는 환경인 Node.js의 기능이다.(Node.js에서는 import가 아닌 require라는 구문을 사용하여 패키지를 불러옴)

이러한 기능을 브라우저에서도 사용하기 위해 번들러(bundler)를 사용한다. 단어 그 자체로 번들(bundle)은 파일을 묶듯이 연결하는 것을 의미한다.

<img src="https://thebook.io/img/080203/057.jpg">

리액트에선 주로 웹팩(WebpacK)이 편의성과 확장성이 뛰어나 주로 사용한다.

이러한 번들러 도구를 사용하면 import(or require)로 모듈을 불러왔을 때 불러온 모듈을 모두 합쳐 하나의 파일을 생성해 준다.(최적화 과정에선 여러 파일로 분리 될 수 있음)

실습 프로젝트에서 src/index.js를 시작으로 필요한 파일을 다 불러와 번들링하게 된다.

리액트에는 다음과 같이 파일을 import하는 구문또한 존재한다.

```js
import logo from ‘./logo.svg‘;
import ‘./App.css‘;
```

웹팩을 사용하면 위 코드 예시처럼 SVG파일과 CSS파일도 불러와 사용할 수 있다. 이렇게 파일을 불러오는 것은 웹팩의 `로더(loader)`라는 기능이 담당한다.

로더에는 CSS 파일을 불러오는 css-loader, 웹 폰트나 미디어 팡리을 불러오는 file-loader, 자바스크립트 파일을 불러오면서 최신 자바스크립트 문법으로 작성된 코드를 `바벨`이라는 도구를 사용해 ES5 문법으로 변환시키는 babel-loader 등이 있다.

이러한 웹팩의 로더는 원래 직접 설치하고 설정해야 하지만 create-react-app으로 프로젝트를 생성하면 이런 번거로운 작업을 모두 대신 해준다.

# 🚩 JSX

react에서 컴포넌트가 렌더링하는 HTML로 작성된 코드는 HTML도 아니고 문자열 템플릿도 아닌 JSX라고 부른다.

JSX는 자바스크립트 확장 문법으로 XML과 유사하다고 한다. 이런 형식으로 작성된 코드는 브라우저에서 실행되기 이전 코드가 번들링되는 과정에서 바벨을 사용하여 일반 자바스크립트로 변환된다.

```js
// JSX문법 변환 전
function App() {
  return (
    <div>
      Hello <b>react</b>
    </div>
  );
}

// 변환 후 코드
function App() {
return React.createElement(“div“, null, “Hello “, React.createElement(“b“, null, “react“));
}
```

## 👍 JSX 장점

1. 보기 쉽고 익숙하다

    HTML과 유사하다보니 결국 HTML 코드를 작성하는 것과 비슷.

2. 높은 활용도

    JSX에서는 div span등의 HTML 태그를 사용할 수 있고, 앞으로 만들 컴포넌트또한 JSX안에 작성이 가능하다.

> 🔍 ReactDOM.render는 무엇인가?

```js
// src/index.js 파일
import React from ‘react‘;
import ReactDOM from ‘react-dom‘;
import ‘./index.css‘;
import App from ‘./App‘;
import * as serviceWorker from ‘./serviceWorker‘;


ReactDOM.render(<App />, document.getElementById(‘root‘));



// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
```

React.render()는 컴포넌트를 페이지에 렌더링하는 역할을 하며, react-dom 모듈을 불러와 사용할 수 있다.

이 함수의 첫번째 파라미터에는 페이지에 렌더링할 내용을 JSX로 작성하고, 두 번째 파라미터에는 해당 JSX를 렌더링할 document 내부 요소를 설정한다.

---

## 📚 JSX 문법

JSX는 편리하지만 반드시 준수해야할 문법(규칙)이 존재한다.

### 📗 감싸인 요소

컴포넌트에 여러 요소가 있다면 반드시 부모 요소 하나로 감싸야 한다.

> 📝 예시

```js
import logo from './logo.svg';

function App() {
  return (
<h1>안녕ㅋㅋ</h1>
<h2>동작 테스트</h2>
  );
}

export default App;
```

다음과 같은 구조는 부모 요소가 없기 때문에 동작하지 않는다.

`<div>` 태그나 `<Fragment>` 태그, `<>` 태그를 사용하여 하나의 요소로 감싸주어야 한다.

Virtual DOM에서 컴포넌트 변화를 감지할 때 효율적으로 비교할 수 있도록 컴포넌트 내부는 하나의 DOM 트리 구조로 이뤄져야 한다는 규칙이 있기 때문이다.

### 📕 자바스크립트 표현

JSX 안에서는 자바스크립트 표현식을 쓸 수 있다. 자바스크립트 표현식을 작성하려면 JSX 내부에서 코드를 `{ }`로 감싸면 된다.

## 🏷 if 문 대신 조건부 연산자(= 삼항 연산자)

JSX 내부의 자바스크립트 표현식에서 if 문을 사용할 수 없다.

조건에 따라 다른 내용을 렌더링해야 할 때는 JSX 밖에서 if 문을 사용하여 사전에 값을 설정하거나, { } 안에 조건부 연산자를 사용해야 한다.

> 📝 예시

```js
import React from ‘react‘;

function App() {
  const name = ‘리액트‘;
  return (
    <div>
      {name === ‘리액트‘ ? (
        <h1>리액트입니다.</h1>
      ) : (
        <h2>리액트가 아닙니다.</h2>
      )}
    </div>
  );
}

export default App;
```

변수명 name값에 따라 출력되는 문구가 다르다.

## 🏷 AND 연산자(&&)를 사용한 조건부 렌더링

특정 조건을 만족할 때 내용을 보여 주고, 만족하지 않을 때 아예 아무것도 렌더링하지 않아야 하는 상황에 사용한다.

> 📝 예시

```js
// 삼항 연산자 이용
import React from "react";

function App() {
    const name = "뤼왝트";
    return <div>{name === "리액트" ? <h1>리액트입니다.</h1> : null}</div>;
}

export default App;

// && 연산자 이용
import React from ‘react‘;

function App() {
  const name = ‘뤼왝트‘;
  return <div>{name === ‘리액트‘ && <h1>리액트입니다.</h1>}</div>;
}

export default App;
```

name 변수값에 따라 삼항연산자의 false 값을 null로 해둘 경우 아무것도 보여 주지 않는다.

그러나 && 연산자를 사용하면 더욱 짧은 코드로 같은 작업을 할 수 있다.

여기서 한 가지 주의해야 할 점은 falsy한 값인 0은 예외적으로 렌더가 된다는 것이다.

> 📝 예시

```js
const number = 0;
return number && <div>내용</div>;
```

이러한 코드는 화면에 숫자 0을 보여준다.

## 🏷 undefined를 렌더링하지 않기

리액트 멈포넌트에서는 함수에서 undefined만 반환하여 렌더링하는 상황을 만들어선 안된다고 나와있는데 테스트 결과 오류는 뜨지않고 아무것도 렌더만 되지않는다.

> 📝 예시

```js
function App() {
    const name = undefined;
    return name;
}
```

JSX에 감싸서 표현해도 똑같이 렌더만되지 않는다.

```js
function App() {
    const name = undefined;
    return <>{name}</>;
}
```

값이 undefined 일 때 보여주고 싶다면

```js
function App() {
    const name = undefined;
    return <div>{name || "보여주고싶은 문구"}</div>;
}
```

## 🏷 인라인 스타일링

리액트에서 DOM 요소에 스타일을 적용할 때는 문자열 형태로 넣는 것이 아니라 객체 형태로 넣어 주어야 한다.

그러므로 스타일 이름중에 `-`기호가 들어가는 경우 `-`문자를 없애고 카멜 케이스로 작성해야 한다.

> 📝 예시

```js
import React from "react";

function App() {
    const name = "리액트";
    const style = {
        // background-color는 backgroundColor와 같이 -가 사라지고 카멜 표기법으로 작성한다.
        backgroundColor: "black",
        color: "aqua",
        fontSize: "48px", // font-size -> fontSize
        fontWeight: "bold", // font-weight -> fontWeight
        padding: 16, // 단위를 생략하면 px로 자동 지정된다.
    };
    return <div style={style}>{name} </div>;
}

export default App;
```

style 객체를 미리 선언하지 않고 바로 style 값을 지정할 수 있다.

```js
import React from "react";

function App() {
    const name = "리액트";
    return (
        <div
            style={{
                backgroundColor: "black", // 카멜케이스로
                color: "aqua",
                fontSize: "48px", // font-size -> fontSize
                fontWeight: "bold", // font-weight -> fontWeight
                padding: 16, // 단위를 생략하면 px로 지정된다.
            }}
        >
            {name}
        </div>
    );
}

export default App;
```

## 🏷 class 대신 calssName

일반 HTML에서 CSS 클래스를 사용할 때에는 `<div class="test"></div>` 와 같이 사용하는데 JSX는 class만 className으로 바꿔주면 된다.

물론 class로해도 스타일은 적용되지만 개발자 도구 Console 탭에서 경고가 나타나게 된다.

## 🏷 주석

JSX 안에서 주석을 작성하는 방법은 일반 자바스크립트에서 주석을 작성할 때와 조금 다르다.

> 📝 예시

```js
function App() {
    const name = "리액트";
    return (
        <>
            {/* 주석은 이렇게 작성한다. */}
            <div
                className="react" // 시작 태그를 여러 줄로 작성하게 된다면 여기에 주석을 작성할 수 있다.
            >
                {name}
            </div>
            // 하지만 이런 주석이나 / 이런 주석은 페이지에 그대로 나타나게 된다.
            */
            <input />
        </>
    );
}
```

JSX 내부에서 주석을 작성할 때는 `{/* …주석 내용 */}`와 같은 형식으로 작성한다.

# 🚩 컴포넌트

리액트를 사용하여 어플리케이션의 인터페이스를 설계할 때 사용자가 볼 수 있는 요소는 여러개의 컴포넌트로 구성되어 있다.

<img src="https://thebook.io/img/080203/084.jpg">

위의 예시는 총 네 가지 컴포넌트를 사용하여 구성했다.

화면 중앙의 사각형 레이아웃의 역할을 하며 전체적인 틀을 잡아주는 컴포넌트, 새로운 항목을 추가할 수 있는 컴포넌트, 할 일 항목을 여러개 보여주는 컴포넌트, 각 항목을 보여 주기 위해 사용되는 컴포넌트들이다.

컴포넌트의 기능은 단순한 템플릿 이상이다. 데이터가 주어졌을 때 이에 맞추어 UI를 만들어 주는 것은 물론이고, 라이프사이클 API를 이용하여 컴포넌트가 화면에서 나타날 때, 사라질 때, 변화가 일어날 때 주어진 작업들을 처리할 수 있으며, 임의 메서드를 만들어 특별한 기능을 붙여 줄 수 있다.

## 클래스형 컴포넌트

앞의 예제에서 사용한 컴포넌트는 함수형 컴포넌트이다. 컴포넌트를 선언하는 방식은 함수평 컴포넌트와 클래스형 컴포넌트 2가지이다.

> 📝 예시

```js
// 함수형 컴포넌트
import React from "react";
import "./App.css";

function App() {
    const name = "리액트";
    return <div className="react">{name}</div>;
}

export default App;

// 클래스형 컴포넌트
import React, { Component } from "react";

class App extends Component {
    render() {
        const name = "react";
        return <div className="react">{name}</div>;
    }
}

export default App;
```

클래스형 컴포넌트로 바뀌었지만 역할은 함수형 컴포넌트와 동일하다.

> 🔍 ES6의 클래스 문법

ES6 이전에는 자바스크립트에 클래스(class)가 없었다. 개념 자체는 있었지만, 그것을 구현하려면 class 대신 prototype이라는 문법을 사용하여 다음과 같이 작업해야 했다.

> 📝 예시

```js
function Dog(name) {
    this.name = name;
}

Dog.prototype.say = function () {
    console.log(this.name + " : 멍멍");
};
var dog = new Dog("검둥이");
dog.say(); // 검둥이 : 멍멍
```

ES6 문법부터는 이것과 기능이 똑같은 코드를 class를 사용하여 다음과 같이 작성할 수 있다.

```js
class Dog {
    constructor(name) {
        this.name = name;
    }
    say() {
        console.log(this.name + ": 멍멍");
    }
}

const dog = new Dog("흰둥이");
dog.say(); // 흰둥이: 멍멍
```

클래스형 컴포넌트에서는 render 함수가 꼭 있어야 하고, 그 안에서 보여 주어야 할 JSX를 반환해야 한다.

> 🔍 ES6의 클래스 문법

화살표 함수(arrow function)는 ES6 문법에서 함수를 표현하는 새로운 방식이다. 그렇다고 기존의 function 선언 방식을 아예 대체하진 않는다.

사용 용도가 서로 조금 다르기 때문인데 화살표 함수는 주로 함수를 파라미터로 전달할 때 유용하다.

> 📝 예시

```js
setTimeout(function() {
  console.log('hello world');
}, 1000);

setTimeout(() => {
  console.log('hello world')
}), 1000);
```

무엇보다 서로 가리키는 this의 값이 다르기 때문이다.

```js
// function() 형식
function BlackDog() {
    this.name = "흰둥이";
    return {
        name: "검둥이",
        bark: function () {
            console.log(this.name + ": 멍멍!");
        },
    };
}

const blackDog = new BlackDog();
blackDog.bark(); // 검둥이: 멍멍!

// Arrow function 형식
function WhiteDog() {
    this.name = "흰둥이";
    return {
        name: "검둥이",
        bark: () => {
            console.log(this.name + ": 멍멍!");
        },
    };
}

const whiteDog = new WhiteDog();
whiteDog.bark(); // 흰둥이: 멍멍!
```

function()을 사용했을 때는 검둥이가 나타나고, () =>를 사용했을 때는 흰둥이가 나타난다.

일반 함수는 자신이 종속된 객체를 this로 가리키며, 화살표 함수는 자신이 종속된 인스턴스를 가리킨다.

또한 화살표 함수는 값을 연산하여 바로 반환해야 할 때 사용하면 가독성을 높일 수 있다.

> 🔍 Reactjs Code Snippet

Vscode 확장프로그램으로 설치했다면 컴포넌트 코드를 빠르고 간편하게 생성할 수 있다.

에디터 창에서 rsc를 입력하고 엔터를 누르면 해당 파일의 이름을 가진 컴포넌트 형태를 빠르게 생성해준다.

<img src="https://thebook.io/img/080203/090.jpg">

rfec 입력 시

현재 있는 js file 이름을 기반으로한 function template가 만들어진다.

클래스형은 안쓰곘지만 rcc를 입력하면 된다.

# 📚 모듈 내보내기 및 불러오기

## 📗 모듈 내보내기(export)

작성한 컴포넌트에서 맨 아랫단 코드를 보면 다음과 같다.

```js
export default MyComponent;
```

이 코드는 다른 파일에서 이 파일을 import할 때, 위에서 선언한 MyComponent 클래스를 불러오도록 설정한다.

## 📕모듈 불러오기(import)

다른 컴포넌트에서 원하는 컴포넌트(MyComponent)를 불러오려면 다음과 같이 import 구문을 사용하면 된다.

> 📝 예시

```js
import React from "react";
import MyComponent from "./MyComponent";

const App = () => {
    return <MyComponent />;
};

export default App;
```

# 📚 props

props는 properties의 줄인 표현으로 컴포넌트 속성을 설정할 때 사용하는 요소이다.

props 값은 해당 컴포넌트를 불러와 사용하는 `부모 컴포넌트`에서 설정할 수 있다.

## 📗JSX 내부에서의 props 렌더링

props 값은 컴포넌트 함수의 파라미터로 받아 와서 사용할 수 있다.

props를 렌더링할 때는 JSX 내부에서 `{ }` 기호로 감싸 주면 된다.

> 📝 예시

```js
// src/Components/MyComponent.js 파일
import React from "react";

const MyComponent = (props) => {
    return <div>안녕하세요, 제 이름은 {props.name}입니다.</div>;
};

export default MyComponent;
```

## 📕컴포넌트에서 props 값 지정해주기

부모 컴포넌트에서 우리가 사용할 컴포넌트의 props 값을 지정해야 사용할 수 있다.

> 📝 예시

```js
// src/App.js(부모 컴포넌트)
import React from "react";
import MyComponent from "./MyComponent";

const App = () => {
    return <MyComponent name="이필웅" />;
};

export default App;
```

## 📘 비구조화 할당 문법을 통해 props 내부 값 추출하기

MyComponent에서 props 값을 조회할 때마다 props.name, props.children과 같이 props.이라는 키워드를 앞에 붙여 주고 있는데 `비구조화 할당`을 사용하면 더 쉽게 추출이 가능하다.

> 📝 예시

```js
// 할당 전
const MyComponent = (props) => {
    return (
        <div>
            안녕하세요, 제 이름은 {props.name}입니다. <br />
            children 값은 {props.children}
            입니다.
        </div>
    );
};

// 할당 후
const MyComponent = (props) => {
    const { name, children } = props;
    return (
        <div>
            안녕하세요, 제 이름은 {name}입니다. <br />
            children 값은 {children}
            입니다.
        </div>
    );
};
```

## 📙propTypes를 통한 props 검증

컴포넌트의 필수 props를 지정하거나 props의 타입(type)을 지정할 때는 propTypes를 사용한다.

propTypes를 사용하려면 코드 상단에 import 구문을 사용하여 불러와야한다.

> 📝 예시

```js
// import 구문
import PropTypes from ‘prop-types‘;

// propTypes 사용 구문
MyComponent.propTypes = {
  name: PropTypes.string
};
```

물론 다른 형태의 값을 입력하여도 화면에 출력은 되지만 console창에 오류가 뜨게된다.

## 📒isRequired를 사용하여 필수 propTypes 설정

propTypes를 지정하지 않았을 때 경고 메시지를 띄워 주는 문법인데 뒤에 isRequired를 붙여 주면 된다.

> 📝 예시

```js
MyComponent.propTypes = {
    name: PropTypes.string.isRequired,
};
```

동시에 다양한 종류의 값들을 설정할 수 있다. (https://github.com/facebook/prop-types 에서 확인 가능)

> 🔍 defaultProps와 propTypes는 꼭 사용해야 하는가?

필수는 아니나 큰 규모의 프로젝트로 가서 협업을 진행하게 될 때 어떤 컴포넌트에 어떤 props가 필요한지 쉽게 알 수 있게 해주는 도구 정도의 역할로 이해하면 좋을 것 같다.

# state

`state`는 컴포넌트 내부에서 바뀔 수 있는 값을 의미한다

props는 컴포넌트가 사용되는 과정에서 부모 컴포넌트가 설정하는 값이며, 컴포넌트 자신은 해당 props를 읽기 전용으로만 사용할 수 있다. props를 바꾸려면 부모 컴포넌트에서 바꾸어 주어야 한다.

## 📚 클래스형 컴포넌트의 state

Counter.js라는 컴포넌트로 어떠한 녀석이 어떠한 기능을 하는지 알아보자.

> 📝 예시

```js
import React, { Component } from "react";

// 클래스형 컴포넌트
class Counter extends Component {
    // 컴포넌트 생성자 메소드 (state 설정 시 무조건 작성하여 설정해야 한다)
    constructor(props) {
        super(props); // 클래스형 컴포넌트에서 constructor 작성 시 super(props)를 호출해야 한다. -> 현재 클래스형 컴포넌트가 상속하고 있는 리액트의 Component 클래스가 지닌 생성자 함수를 호출한다.

        // state의 초깃값 설정하는 구문
        this.state = {
            number: 0,
        };
    }
    render() {
        const { number } = this.state; // state를 조회할 때는 this.state로 조회한다.
        return (
            <div>
                <h1>{number}</h1>
                <button
                    // onClick을 통해 버튼이 클릭되었을 때 호출할 함수를 지정한다.
                    onClick={() => {
                        // this.setState를 사용하여 state에 새로운 값을 넣을 수 있다.
                        this.setState({ number: number + 1 });
                    }}
                >
                    +1
                </button>
            </div>
        );
    }
}

export default Counter; // 모듈 내보내는 구문
```

### 📗 state 객체 안에 여러 값이 존재하는 경우

state 객체 안에는 여러 값이 있을 수 있다.

> 📝 예시

```js
class Counter extends Component {
    constructor(props) {
        super(props);
        this.state = {
            number: 0,
            fixedNumber: 0, // fixedNumber 추가
        };
    }

    render() {
        const { number, fixedNumber } = this.state; // fixedNumber 추가
        return (
            <div>
                <h1>{number}</h1>
                <h2>바뀌지 않는 값: {fixedNumber}</h2>
                <button
                    onClick={() => {
                        this.setState({
                            number: number + 1,
                            fixedNumber: fixedNumber + 1, // fixedNumber 추가
                        });
                    }}
                >
                    +1
                </button>
            </div>
        );
    }
}
```

class 형의 경우 this.setState()안에 state값으로 쓰일 객체값들을 뭘 넣고 어떻게 증감시키냐에 따라 state의 값이 변화한다.

책의 예시처럼 하려면 setState 안의 fixedNumber만 빼면 하나만 오르고 위와 같은 구조면 둘다 오른다.

### 📕 state를 constructor에서 꺼내기

앞에서 state의 초깃값을 지정하기 위해 constructor 메서드를 선언해 주었는데 다른 방식으로도 state의 초기값을 지정할 수 있다.

> 📝 예시

```js
class Counter extends Component {
  state = {
    number: 0,
    fixedNumber: 0
  };
  render() {
    const { number, fixedNumber } = this.state; // state를 조회할 때는 this.state로 조회합니다.
    return (...);
  }
}
```

위의 구문은 아래와 같이 수정해도 똑같이 기능한다. 도대체 위와같이 왜쓰는걸까 싶은데 뭔가 이해하지 못한 설명안한 별도의 구조가 있지않을까 싶다. 클래스형을 공부하는게 의미가 있나 싶지만

### 📘 this.setState에 객체 대신 함수 인자 전달하기

this.setState를 사용하여 state 값을 업데이트할 때는 상태가 비동기적으로 업데이트된다.

> 📝 예시

```js
onClick={() => {
  // this.setState를 사용하여 state에 새로운 값을 넣을 수 있다.
  this.setState({ number: number + 1 });
  this.setState({ number: this.state.number + 1 });
}}
```

재미난 점은 아래 this.state.number +1은 기대와는 다르게 동작한다. +1씩밖에 오르지 않는다.

this.setState를 사용한다 해서 state 값이 바로 바뀌지는 않기 때문이다.

해결책은 this.setState를 사용할 때 객체 대신에 함수를 인자로 넣어 주는 것이다.

> 📝 예시

```js
this.setState((prevState, props) => {
    return {
        // 업데이트하고 싶은 내용
    };
});
```

여기서 prevState는 기존 상태이고, props는 현재 지니고 있는 props를 가리킨다. 만약 업데이트하는 과정에서 props가 필요하지 않다면 생략해도 된다.

> 📝 예시

```js
<button
    // onClick을 통해 버튼이 클릭되었을 때 호출할 함수를 지정합니다.
    onClick={() => {
        this.setState((prevState) => {
            return {
                number: prevState.number + 1,
            };
        });
        // 위 코드와 아래 코드는 완전히 똑같은 기능을 합니다.
        // 아래 코드는 함수에서 바로 객체를 반환한다는 의미입니다.
        this.setState((prevState) => ({
            number: prevState.number + 1,
        }));
    }}
>
    +1
</button>
```

다음과 같이 두 번째로 this.setState 함수를 사용할 때에는 화살표 함수에서 바로 객체를 반환하도록 하면 값이 2씩 올라감을 확인할 수 있다.

### 📙 this.setState가 끝난 후 특정 작업 실행하기

setState를 사용하여 값을 업데이트하고 난 다음 특정 작업을 하고 싶을 때에는 setState의 두 번째 파라미터로 콜백(callback) 함수를 등록하여 작업을 처리할 수 있다.

보통은 onClick등에 콜백을 사용하지 않고 호출하면 값은 변경되도 그뒤에 무언가 변하진 않는다.

> 📝 예시

```js
<button
  onClick={() => {
      this.setState(
          {
              number: number + 1
      },
      // onClick을 통해 버튼이 클릭되었을 때 호출할 함수를 지정한다.
      () => {
        console.log(‘방금 setState가 호출되었습니다.’);
        console.log(this.state);
      }
    );
  }}
>
  +1
</button>
```

---

## 📚 함수형 컴포넌트에서 useState 사용하기

요근래에는 함수형으로 짜는것이 권장된다고 할정도니 함수형 컴포넌트에서도 Hooks을 사용하여 state를 사용할 수 있다.

### 📗 useState 사용하기

배열 비구조화 할당을 이용한 것이 useState라고 할 수 있다.

> 📝 예시

```js
// 사용하기 위해선 다음과 같은 구문을 삽입해야 함
import React, { useState } from ‘react‘;

// 배열 비구조화 할당 사용
const [message, setMessage] = useState("");
```

클래스형 컴포넌트에서의 state 초깃값은 객체 형태를 넣어야 하지만 useState에서는 반드시 객체가 아니어도 상관없다.

값의 형태는 자유이다. 숫자, 문자, 객체. 배열 모두 상관없다. useState("")의 `""`는 초기값이다.

함수를 호출하면 배열이 반환되는데 이 배열의 첫 번쨰 원소인 message는 state값 즉 현재 상태이고, 두 번째 원소인 setMessage는 세터(setter)함수라 부르는 상태 변경 함수이다.

useState의 두 요소는 이름을 자유롭게 바꾸어도 아무런 지장이 없다.

### 📕 state를 사용할 때 주의 사항

state 값을 바꾸어야 할 때는 setState 혹은 useState를 통해 전달받은 세터 함수를 사용해야 한다.

> 📝 잘못된 코드들의 예

```js
// 클래스형 컴포넌트
this.state.number = this.state.number + 1;
this.state.array = this.array.push(2);
this.state.object.value = 5;

// 함수형 컴포넌트
const [object, setObject] = useState({ a: 1, b: 1 });
object.b = 2;
```

그렇다면 배열이나 객체를 업데이트 해야 할 때는 배열이나 객체 사본을 만들고 그 사본에 값을 업데이트한 후, 그 사본의 상태를 setState나 세터 함수를 통해 업데이트 한다.

> 📝 예시

```js
// 객체 다루기
const object = { a: 1, b: 2, c: 3 };
const nextObject = { ...object, b: 2 }; // 사본을 만들어서 b 값만 덮어 쓰기

// 배열 다루기
const array = [
{ id: 1, value: true },
{ id: 2, value: true },
{ id: 3, value: false }
];
let nextArray = array.concat({ id: 4 }); // 새 항목 추가
nextArray.filter(item => item.id != = 2); // id가 2인 항목 제거
nextArray.map(item => (item.id === 1 ? { ...item, value: false } : item)); // id가 1인 항목의 value를 false로 설정
// nextArray = [{id: 1, value: false}, {id: 2, value: true}, {id: 3, value: false},{id: 4}]
```

# ❗️ 정리

props와 state는 둘 다 컴포넌트에서 사용하거나 렌더링할 데이터를 담고 있어 비슷해 보이지만 역할이 다르다는 것을 기억하자.

props는 부모 컴포넌트가 설정, state는 컴포넌트 자체적으로 지닌 값으로 내부에서 업데이트가 가능하다.

물론 props를 사용한다고 값이 고정적이진 않다. 부모 컴포넌트의 state를 자식 컴포넌트의 props로 전달하고, 자식 컴포넌트에서 특정 이벤트가 발생할 때 부모 컴포넌트의 메소드를 호출한다면 props도 유동적으로 이용이 가능하다.
<img src="https://thebook.io/img/080203/117.jpg">
