# React 이론 정리2

복습용으로 최대한 축약하여 이해하는데 있어 어색함이나 부족함 없게끔 정리하는 것이 목표.

# 🚩 이벤트 핸들링

사용자가 웹 브라우저에서 DOM 요소들과 상호 작용하는 것을 `이벤트(event)`라고 한다.

예를 들어 버튼에 마우스 커서를 올렸을 때는 onmouseover 이벤트를 실행하고, 클릭했을 때는 onclick 이벤트를 실행하는 것, Form 요소가 값이 바뀔 때 onchange 이벤트를 실행하는 것들이 해당된다.

## ❗️ React에서 이벤트를 사용할 때 주의 사항

> 1. 이벤트 이름은 카멜 표기법으로 작성한다.

예를 들어 HTML의 onclick은 리액트에서는 onClick으로 작성해야 한다.

> 2. 이벤트에 실행할 자바스크립트 코드를 전달하는 것이 아니라, 함수 형태의 값을 전달한다.

HTML에서 이벤트를 설정할 때는 큰따옴표 안에 실행할 코드를 넣었지만, 리액트에서는 함수 형태의 객체를 전달한다.

화살표 함수 문법으로 함수를 만들어 전달해도 되고, 렌더링 부분 외부에서 만들어서 전달해도 된다.

> 3. DOM 요소에만 이벤트를 설정할 수 있다.

div, button, input, form, span 등의 DOM 요소에는 이벤트를 설정할 수 있지만, 우리가 직접 만든 컴포넌트에는 이벤트를 자체적으로 설정할 수 없다.

예를 들어 다음과 같이 MyComponent에 onClick 값을 설정한다면 MyComponent를 클릭할 때 이벤트(doSomething 함수)를 실행하는 것이 아니라, 그냥 이름이 onClick인 props를 MyComponent에게 전달해 줄 뿐인 것이다.

> 📝 예시

```js
<MyComponent onClick={doSomething} />
```

따라서 컴포넌트에 자체적으로 이벤트를 설정할 수는 없다. 하지만 전달받은 props를 컴포넌트 내부의 DOM 이벤트로 설정할 수는 있다.

> 📝 예시

```js
<div onClick={this.props.onClick}>{/* (…) */}</div>
```

리액트에서 지원하는 이벤트 종류는 다음 [리액트 메뉴얼](https://facebook.github.io/react/docs/events.html)에서 확인하자.

# 🏷 e 객체(이벤트 객체)

> 📝 예시

```js
onChange={
  (e) => {
    console.log(e.target.value);
  }
}
```

다음과 같은 코드에서 쓰이는 e 객체는 `SyntheticEvnet`로 웹 브라우저의 `네이티브 이벤트`를 감싸는 객체라곤 하는데 저 두 키워드가 이해가 안간다.

네이티브 이벤트와 인터페이스가 같으므로 순수 자바스크립트에서 HTML 이벤트를 다룰 때와 똑같이 사용하면 된다고 한다.

아무튼 이벤트가 끝나고 나면 이벤트가 초기화되므로 정보를 참조할 수 없다. 예를들어 0.5초 뒤에 e 객체를 참조하면 e 객체 내부의 모든 값이 비워지게 된다.

# 📚 ref

일반적으로 HTML에서 DOM 요소에 이름을 달 때는 id를 사용한다.

> 📝 예시

```html
<!-- HTML의 경우 -->
<div id="“my-element“"></div>
```

이와 같이 특정 DOM 요소에 어떤 작업을 해야 할 때 id를 달면 CSS에서 특정 id에 특정 스타일을 적용하거나 자바스크립트에서 해당 id를 가진 요소에 작업하기도 한다.

리액트 프로젝트 내부에서 DOM에 이름을 다는 방법이 있는데 바로 ref(reference의 줄임말) 개념이다.

> 🔍 리액트 컴포넌트 안에서 id를 사용하면 안될까?

리액트 컴포넌트 안에서도 id를 사용할 수는 있다. JSX안에서 DOM에 id를 달면 DOM을 렌더링할 떄 그대로 전달된다. 그러나 특수한 경우가 아니면 사용을 권하지 않는다고 한다.

예를 들어 같은 컴포넌트르 여러번 사용한다고 가정하면 HTML에서 DOM의 id는 유일해야 하는데 컴포넌트는 재사용 가능성을 염두에 두기 때문에 중복 id를 가진 DOM이 여러개 생기기 때문이다.

ref는 전역적으로 작동하지도 않고 컴포넌트 내부에서만 작동하기 때문에 이런 문제가 생기지 않는다.

굳이 id를 사용해야 한다면 컴포넌트를 만들 때마다 id 뒷부분에 추가 텍스트를 붙여 중복 id를 방지하면 된다.

## 📗 ref의 사용처

ref는 DOM에 작업을 해야 할 때 사용한다는 것은 알았지만 어떤 작업을 해야할 때 사용하는가에 대해 알아보자면 'DOM을 직접적으로 건드려야 할 때' 사용한다.

## 📕 DOM을 꼭 사용해야 하는 상황

가끔 state만으로는 해결할 수 없는 기능이 있다.

-   특정 input에 포커스 주기
-   스크롤 박스 조작하기
-   Canvas 요소에 그림 그리기 등

위의 상황에서는 DOM에 직접적으로 접근해야 하는데, 이를 위해 바로 ref를 사용한다.

## 📘 ref 사용방법

### 🔖 콜백 함수를 통한 ref 설정

ref를 만드는 가장 기본적인 방법은 콜백 함수를 사용하는 것이다. ref를 달고자 하는 요소에 ref라는 콜백 함수를 props로 전달해 주면 된다.

이 콜백 함수는 ref 값을 파라미터로 전달받는다. 그리고 함수 내부에서 파라미터로 받은 ref를 컴포넌트의 멤버 변수로 설정해 준다. 잘 이해가 안가므로 예시를 통해 알아보자.

```js
<input
    ref={(ref) => {
        this.input = ref;
    }}
/>
```

this.input은 input 요소의 DOM을 가리킨다. 이 때 ref의 이름은 원하는 것으로 자유롭게 지정이 가능하다. DOM 타입과 관계없이 this.spuerman = ref처럼 마음대로 지정이 가능하다.

## 📙 컴포넌트에 ref 달기

리액트에서는 컴포넌트에도 ref를 달 수 있다. 이 방법은 주로 컴포넌트 내부에 있는 DOM을 컴포넌트 외부에서 사용할 때 쓴다.

### 🔖 사용법

```js
<MyComponent
    ref={(ref) => {
        this.myComponent = ref;
    }}
/>
```

이렇게 하면 예시에서 쓰인 MyComponent 내부의 메서드 및 멤버 변수에도 접근할 수 있다. 즉, 내부의 ref에도 접근할 수 있다(EX: myComponent.handleClick, myComponent.input 등).

## 📌 정리

컴포넌트 내부에서 DOM에 직접 접근해야 할 때는 ref를 사용한다. 먼저 ref를 사용하지 않고도 원하는 기능을 구현할 수 있는지 반드시 고려한 후에 활용하자.

컴포넌트끼리 데이터를 교류할 때는 언제나 데이터를 부모 ↔ 자식 흐름으로 교류해야 한다. ref를 이용하여 컴포넌트끼리의 데이터 교류는 잘못된 사용이다.

뭣보다 요샌 함수형 컴포넌트가 권장사항인지라 useRef라는 HOOK 함수를 주로 이용한다.

---

# 📚 컴포넌트 반복

리액트 프로젝트에서 반복적인 내용을 효율적으로 보여 주고 관리하는 방법을 알아보자.

## 📗 자바스크립트 배열의 map() 함수 사용

자바스크립트 배열 객체의 내장 함수인 `map() 함수`를 사용하여 반복되는 컴포넌트를 렌더링할 수 있다.

`map() 함수`는 파라미터로 전달된 함수를 사용해서 배열 내 각 요소를 원하는 규칙에 따라 변환한 후 그 결과로 새로운 배열을 생성한다.

## 🔍 Map() 함수

> 📝 문법

```js
arr.map(callback(currentValue[, index[, array]])[, thisArg])
```

> 📝 파라미터

-   callback: 새로운 배열의 요소를 생성하는 함수로 파라미터는 다음 세 가지입니다.

    -   currentValue: 현재 처리하고 있는 요소

    -   index: 현재 처리하고 있는 요소의 index 값

    -   array: 현재 처리하고 있는 원본 배열

-   thisArg(선택 항목): callback 함수 내부에서 사용할 this의 값

> 📝 설명

map은 callback 함수를 각각의 요소에 대해 한번씩 순서대로 불러 그 함수의 반환값으로 새로운 배열을 만든다.

> 📝 예시

```js
const nums = [1, 2, 3, 4, 5];
const processed = nums.map((num) => num * num);
// processed(5)[(1, 4, 9, 16, 25)];
```

## 📕 리액트 키(key)

리액트에서 key는 컴포넌트 배열을 렌더링했을 때 어떤 원소에 변동이 있었는지 알아내려고 사용한다.

예를 들어 유동적인 데이터를 다룰 때는 원소를 생성할 수도, 제거할 수도, 수정할 수도 있다.

`key가 없을 때`는 Virtual DOM을 비교하는 과정에서 리스트를 순차적으로 비교하면서 변화를 감지한다. 그러나 key가 있다면 이 값을 사용하여 어떤 변화가 일어났는지 더 빠르게 알아 낼 수 있다.(React 동작 원리)

## 📘 key 설정

key 값을 설정할 때는 map 함수의 인자로 전달되는 함수 내부에서 컴포넌트 props를 설정하듯이 설정하면 된다.

key값은 유일해야 하므로 고윳값을 사용해야 한다.

> 📝 예시

예로 들자면 게시판의 게실물을 렌더링한다면 게시물 번호를 key값으로 설정해야 한다. key값이 설정되있지 않은 경우 콘솔창에 에러가 지속적으로 출력된다.

```js
const articleList = articles.map(article => (
  <Article
      title={article.title}
      writer={article.writer}
      key={article.id}
  />
);
```

## 📙 동적 배열 렌더링

흔히 key값을 설정할때 고정된 배열의 경우 key값으로 index를 사용하여 리렌더링 하는 경우도 있지만 이는 비효율적이다.

이러한 상황에서 어떻게 고윳값을 만들 수 있는지 알아보자.

### 🔖 초기 상태 설정하기

우선 컴포넌트에서 useState를 사용하여 상태를 설정하자.

예시에서 총 세 가지 상태를 사용하는데 하나는 데이터 배열, 하나는 텍스트를 입력할 수 있는 input의 상태, 데이터 배열에서 새로운 항목을 추가할 떄 사용할 고유 id이다.

```js
import React, { useState } from "react";

const IterationSample = () => {
    const [names, setNames] = useState([
        { id: 1, text: "눈사람" },
        { id: 2, text: "얼음" },
        { id: 3, text: "눈" },
        { id: 4, text: "바람" },
    ]);
    const [inputText, setInputText] = useState("");
    const [nextId, setNextId] = useState(5); // 새로운 항목을 추가할 때 사용할 id

    const namesList = names.map((name) => <li key={name.id}>{name.text}</li>);
    return <ul>{namesList}</ul>;
};

export default IterationSample;
```

### 🔖 데이터 추가 기능 구현하기

새로운 이름을 등록할 수 있는 기능을 구현하는 예제로 알아보자.

```js
// IterationSample.js
import React, { useState } from ‘react‘;

const IterationSample = () => {
  const [names, setNames] = useState([
    { id: 1, text: ‘눈사람‘ },
    { id: 2, text: ‘얼음‘ },
    { id: 3, text: ‘눈‘ },
    { id: 4, text: ‘바람‘ }
  ]);
  const [inputText, setInputText] = useState(""); // names에 추가할 text
  const [nextId, setNextId] = useState(5); // 새로운 항목을 추가할 때 사용할 id

  const onChange = e => setInputText(e.target.value);
  const onClick = () => {
    const nextNames = names.concat({
      id: nextId, // nextId 값을 id로 설정하고
      text: inputText
    });
    setNextId(nextId + 1); // nextId 값에 1을 더해 준다.
    setNames(nextNames); // names 값을 업데이트한다.
    setInputText(“); // inputText를 비운다.
  };
const namesList = names.map(name => <li key={name.id}>{name.text}</li>);
  return (
    <>
      <input value={inputText} onChange={onChange} />
      <button onClick={onClick}>추가</button>
      <ul>{namesList}</ul>
    </>
  );
};

export default IterationSample;
```

배열에 새 항목을 추가할 때 배열의 push 함수를 사용하지 않고 concat을 사용했는데 이는 push 함수는 기존 배열 자체를 변경하는 반면, concat은 새로운 배열을 만들어 준다는 차이가 있기 때문이다.

리액트에서 상태를 업데이트할 때는 기존 상태를 그대로 두면서 새로운 값을 상태로 설정해야 한다. 이를 불변성 유지라고 하는데 불변성 유지를 해주어야 리액트 컴포넌트의 성능을 최적화할 수 있다.

### 🔖 데이터 제거 기능 구현하기

자바스크립트의 내장 함수 filter()를 사용하면 된다. 새로운 값을 생성하여 상태를 바꾸는게 낫기 때문이다.

> 📝 예시

```js
const numbers = [1, 2, 3, 4, 5, 6];
const biggerThanThree = numbers.filter((number) => number > 3);
// 결과: [4, 5, 6]

const numbers = [1, 2, 3, 4, 5, 6];
const withoutThree = numbers.filter((number) => number !== 3);
// 결과: [1, 2, 4, 5, 6]
```

## 📌 정리

컴포넌트 배열을 렌더링할 때에는 언제나 key 값을 설정하는데 있어 주의해야 한다.

또한 key값은 언제나 유일해야 한다. key 값이 중복된다면 렌더링 과정에서 오류가 발생하기 때문이다.

또한 상태 안에서 배열을 변형할 대에는 배열에 직접 접근하여 수정하는 것이 아닌 concat, filter등의 배열 내장 함수를 사용하여 새로운 배열을 만든 후 이를 새로운 상태로 설정해 주어야 한다.

---

# 🚩 컴포넌트 업데이트

컴포넌트는 다음과 같은 네 가지 경우에 업데이트한다.

1. props가 바뀔 때
2. state가 바뀔 때
3. 부모 컴포넌트가 리렌더링 될 때
4. this.forceUpdate등으로 강제로 렌더링을 트리거 할 때

# Hooks

Hooks은 함수형 컴포넌트에서도 상태 관리를 할 수 있는 useState, 렌더링 직후 작업을 설정하게 하는 useEffect등 다양한 기능을 제공하며 기존의 함수형 컴포넌트에서 할 수 없었던 다양한 작업을 할 수 있게 해준다.

## useState

useState는 가장 기본적인 Hook이며, 함수형 컴포넌트에서도 가변적인 상태를 지닐 수 있게 해준다.

useState는 import 구문을 통해 불러오고, 다음과 같이 사용한다.

```js
const [value, setValue] = useState(0);
```

useState의 파라미터는 상태의 기본값을 넣어 준다.

이 함수가 호출되면 배열을 반환하는데 그 배열의 첫 번째 원소가 상태의 값(state), 상태를 설정하는 함수(세터함수)이다.

이 함수에 파라미터를 넣어 호출하면 전달받은 파라미터로 값이 바뀌고 컴포넌트는 리렌더링 된다.(업데이트)

값의 변경은 세터함수를 호출하여 바꾸고 싶은 값을 입력하면 된다.(배열 같은 경우 새로운 배열을 반환하게끔 하는 것 잊지 말기)

```js
// value값 변경
setValue(5); // value의 값이 5로 변경됨.
```

## useEffect

useEffect는 리액트 컴포넌트가 렌러딩이 될 때마다 특정 작업을 수행하도록 설정할 수 있는 Hook이다.

```js
import React, { useState, useEffect } from ‘react‘;

const Info = () => {
  const [name, setName] = useState(“);
  const [nickname, setNickname] = useState(“);
  useEffect(() => {
    console.log(‘렌더링이 완료되었습니다!’);
    console.log({
      name,
      nickname
    });
  });

  const onChangeName = e => {
    setName(e.target.value);
  };

const onChangeNickname = e => {
    setNickname(e.target.value);
  };

return (
    (…)
  );
};

export default Info;
```

<img src="https://thebook.io/img/080203/195.jpg">

위와 같이 input창의 내용이 변경되서 리렌더링 될때마다 useEffect 안의 내용이 출력됨을 볼 수 있다.

### 마운트될 때만 실행하고 싶을 때

useEffect에서 설정한 함수를 컴포넌트가 화면에 맨 처음 렌더링될 때만 실행하고, 업데이트될 때는 실행하지 않으려면 함수의 두 번째 파라미터로 비어 있는 배열을 넣어 주면 된다.

```js
useEffect(() => {
    console.log("마운트될 때만 실행됩니다.");
}, []);
```

### 특정 값이 업데이트될 대만 실행하고 싶을 때

useEffect를 사용할 때, 특정 값이 변경될 때만 호출하고 싶을 경우에는 다음과 같이 작성하면 된다.

```js
// name값이 바뀔 때마다 렌더하길 원하는 경우
useEffect(() => {
    console.log(name);
}, [name]);
```

상태를 넣어도 되고 props를 넣어도 된다.

### 뒷정리하기

useEffect는 기본적으로 렌더링되고 난 직후마다 실행되며, 두 번째 파라미터 배열에 무엇을 넣는지에 따라 실행되는 조건이 달라진다.

컴포넌트가 언마운트되기 전이나 업데이트되기 직전에 어떠한 작업을 수행하고 싶다면 useEffect에서 뒷정리(cleanup) 함수를 반환해 주어야 한다.

```js
// useEffect만 다음과 같이 바꿔보자
useEffect(() => {
    console.log(‘effect‘);
    console.log(name);
    return () => {
      console.log(‘cleanup‘);
      console.log(name);
    };
  });
```

실행해보면 마운트되자마자 cleanup이 출력된다.

input창에 뭔가 입력하고 난 후에도 console창을 보면 업데이트 되기 전에 cleanup이 호출되고 effect와 name이 호출된다.

<img src="https://thebook.io/img/080203/199.jpg">

렌더링 될때마다 뒷정리 함수는 지속적으로 호출되고 뒷정리 함수가 호출될 때는 업데이트 되기 직전의 값을 보여준다.

## useReducer

useReducer는 useState보다 더 다양한 컴포넌트 상황에 따라 다양한 상태를 다른 값으로 업데이트해 주고 싶을 때 사용하는 Hook이다.

리듀서는 현재 상태, 그리고 업데이트를 위해 필요한 정보를 담은 액션(action) 값을 전달받아 새로운 상태를 반환하는 함수이다.

리듀서 함수에서 새로운 상태를 만들 때는 반드시 `불변성`을 지켜 주어야 한다.

```js
function reducer(state, action) {
return { … }; // 불변성을 지키면서 업데이트한 새로운 상태를 반환합니다.
}
```

액션 값은 주로 다음과 같은 형태로 이루어져 있다.

```js
{
  type: "INCREMENT",
  // 다른 값들이 필요하다면 추가로 들어감
}
```

기존의 Counter.js 컴포넌트 예제가 다음과 같이 바뀐다.

```js
import React, { useReducer } from "react";

function reducer(state, action) {
    // action.type에 따라 다른 작업 수행
    switch (action.type) {
        case "INCREMENT":
            return { value: state.value + 1 };
        case "DECREMENT":
            return { value: state.value - 1 };
        default:
            // 아무것도 해당되지 않을 때 기존 상태 반환
            return state;
    }
}

const Counter = () => {
    const [state, dispatch] = useReducer(reducer, { value: 0 });

    return (
        <>
            <p>
                현재 카운터 값은 <b>{state.value}</b>입니다.
            </p>
            <button onClick={() => dispatch({ type: "INCREMENT" })}>+1</button>
            <button onClick={() => dispatch({ type: "DECREMENT" })}>-1</button>
        </>
    );
};

export default Counter;
```

useReducer의 첫 번째 파라미터에는 리듀서 함수를 넣고, 두 번째 파라미터에는 해당 리듀서의 기본값을 넣어 준다.

이 Hook을 사용하면 state 값과 dispatch 함수를 받아 오는데, 여기서 state는 현재 가리키고 있는 상태고, dispatch는 액션을 발생시키는 함수이다.

dispatch(action)과 같은 형태로, 함수 안에 파라미터로 액션 값을 넣어 주면 리듀서 함수가 호출되는 구조이다.

useReducer를 사용했을 때의 가장 큰 장점은 컴포넌트 업데이트 로직을 컴포넌트 바깥으로 빼낼 수 있다는 점이다.

### useReducer를 사용하여 상태 관리하기

기존에 input을 여러개 사용한 컴포넌트를 useReducer를 이용해 수정해보자.

useReducer를 사용한다면 input을 여러개 사용해서 useState를 여러번 사용하는 컴포넌트들을 클래스형 컴포넌트에서 input에 name을 할당하고 e.target.name을 참조하여 변경해준 방식처럼 처리가 가능하다.

```js
// 기존의 Info 컴포넌트
import React, { useState } from "react";

const Info = () => {
    const [name, setName] = useState("");
    const [nickname, setNickname] = useState("");

    const onChangeName = (e) => {
        setName(e.target.value);
    };

    const onChangeNickname = (e) => {
        setNickname(e.target.value);
    };

    return (
        <div>
            <div>
                <input value={name} onChange={onChangeName} />
                <input value={nickname} onChange={onChangeNickname} />
            </div>
            <div>
                <div>
                    <b>이름:</b> {name}
                </div>
                <div>
                    <b>닉네임:</b> {nickname}
                </div>
            </div>
        </div>
    );
};

export default Info;
```

useReducer 사용한 이후

```js
import React, { useReducer } from "react";

function reducer(state, action) {
    return {
        ...state,
        [action.name]: action.value,
    };
}

const Info = () => {
    const [state, dispatch] = useReducer(reducer, {
        name: "",
        nickname: "",
    });
    const { name, nickname } = state;
    const onChange = (e) => {
        dispatch(e.target);
    };

    return (
        <div>
            <div>
                <input name="name" value={name} onChange={onChange} />
                <input name="nickname" value={nickname} onChange={onChange} />
            </div>
            <div>
                <div>
                    <b>이름:</b> {name}
                </div>
                <div>
                    <b>닉네임: </b>
                    {nickname}
                </div>
            </div>
        </div>
    );
};

export default Info;
```

매우 생소하다보니 어렵고 낯설게 느껴진다.. 자주 보고 사용해보는것으로 익숙해지자.

useReducer에서의 액션은 그 어떤 값도 사용 가능하다. 이런 식으로 인풋을 관리하면 아무리 인풋의 개수가 많아져도 코드를 짧고 깔끔하게 유지할 수 있다.

## useMemo

useMemo를 사용하면 함수형 컴포넌트 내부에서 발생하는 연산을 최적화할 수 있다.

한마디로 렌더링 성능을 최적화하기 위한 hook이다.

리스트에 숫자를 추가하면 추가된 숫자들의 평균을 보여 주는 함수형 컴포넌트를 작성해 보자.

```js
// 평균 구하는 컴포넌트 Average.js
import React, { useState } from "react";

const getAverage = (numbers) => {
    console.log("평균값 계산 중..");
    if (numbers.length === 0) return 0;
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
};

const Average = () => {
    const [list, setList] = useState([]);
    const [number, setNumber] = useState("");

    const onChange = (e) => {
        setNumber(e.target.value);
    };
    const onInsert = (e) => {
        const nextList = list.concat(parseInt(number));
        setList(nextList);
        setNumber("");
    };

    return (
        <div>
            <input value={number} onChange={onChange} />
            <button onClick={onInsert}>등록</button>
            <ul>
                {list.map((value, index) => (
                    <li key={index}>{value}</li>
                ))}
            </ul>
            <div>
                <b>평균값:</b> {getAverage(list)}
            </div>
        </div>
    );
};

export default Average;
```

그러나 위의 코드로는 getAverage() 메소드가 숫자를 등록할 때만이 아닌 인풋 내용이 수정될 때도 우리가 만든 getAverage 함수가 호출된다.

`useMemo` Hook을 사용하면 이러한 작업을 최적화할 수 있다.

렌더링하는 과정에서 `특정 값이 바뀌었을 때만 연산을 실행`하고, `원하는 값이 바뀌지 않았다면 이전에 연산했던 결과를 다시 사용하는 방식`이다.

useMemo를 사용해서 구문을 조금만 바꿔준다면 불필요한 함수 호출을 방지하게 된다.

```js
//useMemo 사용 후 코드
import React, { useState, useMemo } from "react"; // useMemo import구문 추가

const getAverage = (numbers) => {
    console.log("평균값 계산 중..");
    if (numbers.length === 0) return 0;
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
};

const Average = () => {
    const [list, setList] = useState([]);
    const [number, setNumber] = useState("");

    const onChange = (e) => {
        setNumber(e.target.value);
    };
    const onInsert = (e) => {
        const nextList = list.concat(parseInt(number));
        setList(nextList);
        setNumber("");
    };

    const avg = useMemo(() => getAverage(list), [list]); // useMemo를 활용한 구문

    return (
        <div>
            <input value={number} onChange={onChange} />
            <button onClick={onInsert}>등록</button>
            <ul>
                {list.map((value, index) => (
                    <li key={index}>{value}</li>
                ))}
            </ul>
            <div>
                <b>평균값:</b> {avg}{" "}
                {/* useMemo를 활용한 avg 변수로 출력값 변경 */}
            </div>
        </div>
    );
};

export default Average;
```

이렇게하면 list 배열의 내용이 바뀔 때만 getAverage 함수가 호출된다.

## useCallback

useCallback은 useMemo와 상당히 비슷한 함수이다. 주로 렌더링 성능을 최적화해야 할 때 사용하는데 이 Hook을 사용하면 이벤트 핸들러 함수를 필요할 때만생성할 수 있다.

첫 번째 파라미터에는 생성하고 싶은 함수를 넣고, 두 번째 파라미터에는 배열을 넣는다. 이 배열에는 어떤 값이 바뀌었을 때 함수를 새로 생성해야 하는지 명시해야 한다.

```js
const onChange = (e) => {
    setNumber(e.target.value);
};

const onInsert = (e) => {
    const nextList = list.concat(parseInt(number));
    setList(nextList);
    setNumber("");
};
```

위와 같은 구조의 경우 함수를 저렇게 선언하면 컴포넌트가 리렌더링될 때마다 함수들이 새로 생성된다.

대부분의 경우 이러한 방식은 문제가 없지만, 컴포넌트의 렌더링이 자주발생하거나 렌더링해야 할 컴포넌트의 개수가 많아지면 이 부분을 최적화해 주는 것이 좋다.

```js
import React, { useState, useMemo, useCallback } from "react";

const getAverage = (numbers) => {
    console.log("평균값 계산 중..");
    if (numbers.length === 0) return 0;
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
};

const Average = () => {
    const [list, setList] = useState([]);
    const [number, setNumber] = useState("");

    const onChange = useCallback((e) => {
        setNumber(e.target.value);
    }, []); // 컴포넌트가 처음 렌더링될 때만 함수 생성

    const onInsert = useCallback(() => {
        const nextList = list.concat(parseInt(number));
        setList(nextList);
        setNumber("");
    }, [number, list]); // number 혹은 list가 바뀌었을 때만 함수 생성

    const avg = useMemo(() => getAverage(list), [list]);

    return (
        <div>
            <input value={number} onChange={onChange} />
            <button onClick={onInsert}>등록</button>
            <ul>
                {list.map((value, index) => (
                    <li key={index}>{value}</li>
                ))}
            </ul>
            <div>
                <b>평균값:</b> {avg}
            </div>
        </div>
    );
};

export default Average;
```

onChange처럼 비어 있는 배열을 넣게 되면 컴포넌트가 렌더링될 때 단 한 번만 함수가 생성되며, onInsert처럼 배열 안에 number와 list를 넣게 되면 인풋 내용이 바뀌거나 새로운 항목이 추가될 때마다 함수가 생성된다.

함수 내부에서 상태 값에 의존해야 할 때는 그 값을 반드시 두 번째 파라미터 안에 포함시켜 주어야 한다.

예를 들어 onChange의 경우 기존의 값을 조회하지 않고 바로 설정만 하기 때문에 배열이 비어 있어도 상관없지만, onInsert는 기존의 number와 list를 조회해서 nextList를 생성하기 때문에 배열 안에 number와 list를 꼭 넣어 주어야 한다.

```js
useCallback(() => {
  console.log(‘hello world!‘);
}, [])


useMemo(() => {
  const fn = () => {
    console.log(‘hello world!‘);
  };
  return fn;
}, [])
```

위의 두 코드는 완전히 똑같은 코드다. useCallback은 결국 useMemo로 함수를 반환하는 상황에서 더 편하게 사용할 수 있는 Hook이다.

숫자, 문자열, 객체처럼 일반 값을 재사용하려면 useMemo를 사용하고, 함수를 재사용하려면 useCallback을 사용한다.

사용을 많이 안했던 Hooks들이라 여러번 반복해서 복습하자.

## useRef

useRef Hook은 앞서 다뤘던 ref를 함수형 컴포넌트에서도 사용할 수 있도록 해준다.

다음 예시 컴포넌트는 등록 버튼을 눌렀을 때 포커스가 인풋 쪽으로 넘어가도록 하였다.

```js
import React, { useState, useMemo, useCallback, useRef } from "react";

const getAverage = (numbers) => {
    console.log("평균값 계산 중..");
    if (numbers.length === 0) return 0;
    const sum = numbers.reduce((a, b) => a + b);
    return sum / numbers.length;
};

const Average = () => {
    const [list, setList] = useState([]);
    const [number, setNumber] = useState("");
    const inputEl = useRef(null); // useRef 추가구문

    const onChange = useCallback((e) => {
        setNumber(e.target.value);
    }, []);

    const onInsert = useCallback(() => {
        const nextList = list.concat(parseInt(number));
        setList(nextList);
        setNumber("");
        inputEl.current.focus();
    }, [number, list]);

    const avg = useMemo(() => getAverage(list), [list]);

    return (
        <div>
            <input value={number} onChange={onChange} ref={inputEl} />{" "}
            {/* input에 ref 구문 추가*/}
            <button onClick={onInsert}>등록</button>
            <ul>
                {list.map((value, index) => (
                    <li key={index}>{value}</li>
                ))}
            </ul>
            <div>
                <b>평균값:</b> {avg}
            </div>
        </div>
    );
};

export default Average;
```

주석 처리한 부분이 ref를 설정하고 사용하면서 추가한 구문들이다.

useRef를 사용하여 ref를 설정하면 useRef를 통해 만든 객체 안의 current 값이 실제 엘리먼트를 가리킨다.

## 커스텀 Hooks 만들기

여러 컴포넌트에서 비슷한 기능을 공유할 경우 커스텀 Hook을 작성하여 로직을 재사용할 수 있다.

예를 들어 다음의 Info라는 컴포넌트에서 여러 인풋을 관리하기 위해 useReducer로 작성했던 로직을 useInputs 이라는 Hook을 만들어 분리해 보자.

```js
// 수정 전의 Info 컴포넌트
import React, { useReducer } from "react";

function reducer(state, action) {
    return {
        ...state,
        [action.name]: action.value,
    };
}

const Info = () => {
    const [state, dispatch] = useReducer(reducer, {
        name: "",
        nickname: "",
    });
    const { name, nickname } = state;
    const onChange = (e) => {
        dispatch(e.target);
    };

    return (
        <div>
            <div>
                <input name="name" value={name} onChange={onChange} />
                <input name="nickname" value={nickname} onChange={onChange} />
            </div>
            <div>
                <div>
                    <b>이름:</b> {name}
                </div>
                <div>
                    <b>닉네임: </b>
                    {nickname}
                </div>
            </div>
        </div>
    );
};

export default Info;
```

여기서 useInput이라는 컴포넌트를 만들어보자

```js
import { useReducer } from "react";

function reducer(state, action) {
    return {
        ...state,
        [action.name]: action.value,
    };
}

export default function useInputs(initialForm) {
    const [state, dispatch] = useReducer(reducer, initialForm);
    const onChange = (e) => {
        dispatch(e.target);
    };
    return [state, onChange];
}
```

이제 이렇게 만든 컴포넌트를 가지고 수정을 하면 다음과 같이 깔끔해진다.

```js
import React from "react";
import useInputs from "./useInput"; // 컴포넌트 import 구문

const Info = () => {
    const [state, onChange] = useInputs({
        // reducer function 삭제 후 해당 useInput 가져다가 사용
        name: "",
        nickname: "",
    });
    const { name, nickname } = state;

    return (
        <div>
            <div>
                <input name="name" value={name} onChange={onChange} />
                <input name="nickname" value={nickname} onChange={onChange} />
            </div>
            <div>
                <div>
                    <b>이름:</b> {name}
                </div>
                <div>
                    <b>닉네임: </b>
                    {nickname}
                </div>
            </div>
        </div>
    );
};

export default Info;
```

## 📌 정리

리액트에서 Hooks 패턴을 사용하면 클래스형 컴포넌트를 작성하지 않고도 대부분의 기능을 구현할 수 있다.

동시에 매뉴얼에서는 새로 작성하는 컴포넌트의 경우 함수형 컴포넌트와 Hooks를 사용할 것을 권장하고 있으니 프로젝트를 개발할 때는 함수형 컴포넌트의 사용을 첫 번째 옵션으로 두고, 꼭 필요한 상황에서만 클래스형 컴포넌트를 사용하도록 하자.
