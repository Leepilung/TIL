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

일반 함수는 자신이 종속된 객체를 this로 가리키며, 화살표 함수는 자신이 종속된 인스턴스를 가리킵니다.