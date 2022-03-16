# PoiemaWeb - Javascript

# step 0 - start

# 1. 프로그래밍이란?

프로그래밍이란 컴퓨터에게 실행을 요구하는 일종의 `커뮤니케이션`이다. 한마디로, 프로그래밍에 앞서 문제(요구사항)을 명확히 이해한 후 적절한 문제 해결 방안의 정의가 필요하다.

이때 요구되는 능력이 문제 해결 능력이다. 알고리즘등에 국한되는 능력을 말하는 것이 아닌 이를 포함하는 좀 더 큰 차원의 능력을 의미한다.

대부분의 문제(요구사항)은 복잡하고 명확하지 않은 경우가 많다. 때문에 문제(요구사항)을 명확히 이해하는 것이 우선이며, 복잡함을 단순하게 `분해(Decomposition)`하고, 자료를 정리 `구분(Modeling)`해야 하며 이를 순서에 맞게 행위를 배열해야 함이 최종적인 목표이다.

즉, 프로그래밍이란 0과 1밖에 알지 못하는 기계가 실행할 수 있는 정도로 정확하고 상세하게 요구사항을 설명하는 작업이며 그 결과물이 바로 코드이다.

모호하고 대략적인 요구사항을 전달해도 우리의 머리 속에 있는 의도를 정확히 꿰뚫어 완벽히 이해하는 컴퓨터는 절대 존재할 수 없기 때문이다.

때문에 우리는 문제 해결 방안을 고려함에 있어서 컴퓨터의 입장에서 문제를 바라보아야 한다. 바로 이때 필요한 것이 `컴퓨터적 사고(Computational thinking)` 이다.

사람의 일반적인 사고 방식은 매우 포괄적이며 실생활에서 경험하고 있는 익숙한 사항에 대해 당연시하는 안이한 인식이 있다.

문제 해결 능력은 직감과 직관의 영역이라고 볼 수 있는데 이는 문제를 바라보는 우리의 사고와 경험에 영향을 받는다.

예를 들어 “듣다(Listen)”라는 행위를 사람은 하나의 간단하고 당연한 기능으로 생각한다. 하지만 컴퓨터에게 이 행위를 설명하는 것은 단순하지 않다.

또한 사람은 이 소리의 크기를 "크다" or "작다"라는 상대적인 표현을 이용하여 표현하는데 이는 기준이 불명확한 표현이다. 고로 "현재 볼륨의 크기를 1단계 크게 조정해라" 혹은 "볼륨의 크기를 60으로 조정해라" 라는 식의 명령을 내려야 한다.

컴퓨터는 "사랑", "좋다","붉다"와 같은 추상적인 관념과 개념은 명령으로 인식함에 있어서 컴퓨터에게 매우 난해한 것들이다. 사람의 얼굴을 보고 지인인지 판단하는 일또한 마찬가지.

그러나 347^9(347의 9승)같은 계산은 컴퓨터에겐 굉장히 쉬운 작업이다.

이처럼 컴퓨터와 사람은 사고, 인지의 방식이 다르다. 따라서 해결 과제를 컴퓨터의 관점으로 사고(Computational thinking)해야 한다.

이에는 논리적, 수학적 사고가 필요하게 되며 해결 과제를 작은 단위로 분해하고 패턴화하여 추출하며 프로그래밍 내에서 사용될 모든 개념은 평가 가능하도록 정의되어야 한다.

예로 사람처럼 두발로 걷는 로봇을 위해 "걷다"라는 기능을 디자인 했다고 가정해 보자.
<img src="https://poiemaweb.com/img/walk.png">

“걷다”라는 기능을 디자인하려면 판단하여야 하는 상태와 그 상태를 판단하는 시기, 그리고 판단 기준을 정의하여야 하며 이를 바탕으로 분해한 처리(Process)의 실행 여부를 결정한다. 예를 들어 장애물이란 무엇(크기, 움직임…)인지 어떤 범위 내에 있는 것인지 명확히 수치화하여 정의해야 하는 법이다.

# 2. 프로그래밍 언어

문제 해결 능력을 바탕으로 정의된 문제 해결 방안은 컴퓨터에게 전달되어야 한다.

이때 명령을 수행할 주체는 컴퓨터이다. 따라서 인간이 이해할 수 있는 자연어가 아니라 컴퓨터가 이해할 수 있는 언어, 즉 `기계어(Machine code)`로 명령을 전달해야 한다.

인간이 기계어를 이해하여 직접 기계어로 명령을 전달하는 것은 매우 어려운 작업이다. 기계어는 우리가 사용하는 언어와는 너무나도 다른 체계를 가지기 때문이다. 심지어 비트 단위로 기술되어 있다.

x86 아키텍처 리눅스 환경에서 그 유명한 “Hello world”를 출력하는 기계어 코드이다.

> 📝 예제

```c++
// Hello world 출력 기계어 코드
7F 45 4C 46 01 01 01 00 00 00 00 00 00 00 00 00 02 00 03 00 01 00 00 00 35 40 B3 04 2C 00 00 00 00 00 00 00 00 00 00 00 34 00 20 00 01 00 00 00 00 00 00 00 00 40 B3 04 B2 0C EB 1C 62 00 00 00 62 00 00 00 05 00 00 00 00 10 00 00 48 65 6C 6C 6F 20 77 6F 72 6C 64 0A B9 4C 40 B3 04 93 CD 80 EB FB
```

직접 기계어로 명령을 전달하는 것을 대신할 가장 유용한 대안은 인간이 이해할 수 있는 약속된 구문(Syntax, 문법)으로 구성된 “프로그래밍 언어(Programming Language)”를 사용하여 프로그램을 작성한 후, 그것을 컴퓨터가 이해할 수 있는 기계어로 변환하여 주는 일종의 번역기를 이용하는 것이다.

이 일종의 번역기를 `컴파일러(compiler)` 혹은 `인터프리터(interpreter)`라고 한다.

<img src="https://poiemaweb.com/img/compiler.png">

`언어(Language)`는 자신의 생각을 상대에게 전달하는 방법으로 언어 공동체 내에서 이해될 수 있는 말의 집합이다.

<img src="https://poiemaweb.com/img/com-model.png">

언어는 자연어와 `인공어`로 구분할 수 있다. `프로그래밍 언어`란 컴퓨터와의 대화(명령)에 사용되는 일종의 표현 수단으로 인간과 컴퓨터(컴파일러 또는 인터프리터) 모두가 이해할 수 있는 약속된 형태의 `인공어`이다.

아래는 “Hello world”를 출력하는 자바스크립트 코드이다. 위의 기계어 코드보다 인간이 이해하기 쉬운, 즉 읽기 쉬운 코드가 되었다.

```js
console.log("Hello world");
```

프로그래밍은 프로그래밍 언어를 사용하여 컴퓨터에게 실행을 요구하는 일종의 `커뮤니케이션`이다.

프로그래밍 언어는 `Syntax(구문)`와 `Semantics(의미)`의 조합으로 표현된다.

# 3. Syntax & Semantics

프로그래밍 학습은 일반적으로 프로그래밍 언어의 문법을 배우는 것부터 시작한다. 이는 외국어 학습과 유사하다고 할 수 있다.

그러나 이미 경험을 통해 알고 있겠지만 문법을 잘 안다고 해서 외국어를 잘한다고 말할 수는 없다.

외국어를 잘하려면 외국어 화자의 말이나 문장을 정확히 이해한 후, 문맥에 따른 적절한 어휘 선택, 그리고 순차적으로 결론을 향해 나아가는 문장 구성이 필요하다.

즉, 문법에 맞는 문장을 구성하는 것은 물론 `의미(Semantics)`를 가지고 있어야 언어의 역할을 충실히 수행할 수 있다.

```
Colorless green ideas sleep furiously.
– 노엄 촘스키(Noam Chomsky)
```

MIT의 저명한 언어학자인 노엄 촘스키는 위 문장을 통해서 `언어의 의미`는 `문맥`에 있는 것이지 문법에 있는 것이 아니란 것을 지적하고 있다.

위 문장은 `문법(Syntax)`적으로 전혀 문제가 없지만 `의미(Semantics)`는 없다. 프로그래밍도 마찬가지다. 아래 예제를 보자.

> 📝 예제

```js
const number = "string";

console.log(number * number); // NaN
```

자바스크립트의 변수에는 어떠한 타입의 값이라도 할당할 수 있다. 따라서 위 예제는 문법적으로 전혀 문제가 없다.

하지만 의미적으로는 옳지 않다. number라는 변수 이름에 문자열이 할당되어 있기 때문이다. number라는 변수 이름에는 숫자를 할당하는 것이 의미적으로 옳기 때문이다.

결국 문제 해결 능력을 통해 만들어낸 해결 방안은 프로그래밍 언어의 문법을 통해 표현한다. 즉, 작성된 코드는 해결 방안의 구체적 구현물이다.

그리고 이것은 프로그래밍 언어의 문법에 부합하는 것은 물론이고 수행하고자 하는 바를 정확히 수행하는 것, 즉 요구사항이 실현(문제가 해결)되어야 의미가 있다.

<img src="https://poiemaweb.com/img/coding.png">

프로그래밍의 목적은 문제 해결임을 기억하자.

대부분의 프로그래밍 언어는 `“변수와 값”`, `“키워드”`, `“연산자”`, `“표현식과 문”`, `“조건문”`과 `“반복문”`에 의한 `“흐름제어(Control flow)”`, `“함수”` 그리고 `“객체”`, `“배열”` 등의 `“자료구조”`와 같은 문법을 제공한다.

프로그래밍 언어가 제공하는 문법을 적절히 사용하여 `변수`를 통해 값을 저장하고 참조하며 `연산자`로 값을 연산, 평가하고 `조건문`과 `반복문`에 의한 흐름제어로 코드의 실행 순서를 제어하고 함수로 재사용이 가능한 문의 집합을 만들며 객체, 배열 등으로 자료를 구조화한다.

**결국 프로그래밍은 요구사항의 집합을 분석하여 적절한 자료구조와 함수의 집합으로 변환한 후, 그 흐름을 제어하는 것이다.**

# 4. 기본 개념과 동작 원리 이해의 중요성

**프로그래머가 해야 할 일은 문제를 해결하기 위한 방안을 고안하고 이것을 문법에 맞게 코드로 구현하는 것이다.**

구현된 코드는 의도한 대로 정확히 동작하여 문제를 해결해야 한다. 이때 자신이 구현한 코드가 컴퓨터 내부에서 어떻게 동작할 것인지 그리고 무엇을 돌려 줄 것인지 예측 가능해야 하며 이것을 동료에게 명확히 설명할 수 있어야 한다.

이를 위해서는 프로그래밍 언어의 **기본 개념과 동작 원리를 정확히 이해하는 것**이 중요하다.

기본 개념과 동작 원리를 이해하지 못한 상태에서 Copy & Paste로 단순히 동작만 하는 코드를 만들고 그것에 만족한다면 그렇게 구현한 코드는 언제 무너져도 이상할 것이 없는 사상누각일 뿐이다. 동시에 신뢰할 수 없고 유지하고 보수하기 까다로운 코드가 될 것이다. 그리고 문제 해결 능력은 어느 선에서 성장을 멈추고 말 것이다.

기본 개념은 문맥에 맞는 정확한 용어를 사용할 수 있게 돕는다. 문맥에 맞는 정확한 용어의 사용은 오해를 불러 일으키지 않는 명확한 의사 소통을 가능케 한다. 이는 `협업의 기본이며 필수 요소`이다.

동작 원리의 이해는 코드의 동작을 예측할 수 있게 돕는다. 요구 사항을 코드로 구현하려면 당연히 자신이 작성하는 코드의 동작을 예측할 수 있어야 한다.

동작이 예측되지 않는 코드를 작성한다는 것은 말이 되지 않는다. 또한 에러를 발생시키는 코드를 만나면 에러가 발생하는 원인을 이해해야 `디버깅이 가능`하다. 이를 위해 코드의 동작을 예측할 수 있는 능력은 필수 불가결적 요소이다.

즉, 기본 개념과 동작 원리의 이해는 어렵고 생소한 용어들로 이루어진 기술적 의사소통을 가능케하고, 자신의 머리 속에서 코드를 실행시켜 볼 수 있는 능력을 갖게 한다.

이를 통해 다른 사람이 작성한 코드를 이해하는 것은 물론 의도 또한 파악할 수 있게 되어 보다 효과적인 코드를 생산할 수 있는 기본기를 쌓을 수 있다. `기본기는 아무리 강조해도 지나침이 없다.`

```
빨리 가는 유일한 방법은 제대로 가는 것이다.
- 로버트 C. 마틴(Robert C. Martin), “클린 코드”의 저자
```

# 프론트엔드 개발자 학습 방향

## 🧐 프론트 엔드 개발자가 하는 일

애플리케이션을 사용하는 사람(유저)이 애플리케이션과 소통하기 위한 창구(User Interface)를 사용하기 좋게 구현한다.

UI는 상태 정보를 서버로 전송하기도 하고, 서버의 데이터(id등)를 가져와서 UI에 표시하기도 한다.

디자이너(디자인), 백엔드 개발자(서버)와의 협업

## 📚 프론트 엔드 개발에 필요한 기술

- HTML : tags & attributes(기본적인 태그들과 속성들), Semantic web(html 5에서 추가됨)

- CSS : Layout(float,flex,grid), transition/animation(동적 화면 기법), 반응형 웹, Preprocessor(Sass,PostCSS), CSS방법론, CSS 프레임 워크(Bootstrap, Semantic UI)

- 크로스 브라우징

- 🌟 JavaScript : ES5, ES6, ES Next(ES6 이후 갱신되는 항목들), DOM/Event, Ajax, 동작 원리(브라우저, 자바스크립트 엔진), node.js(서버사이드 애플리케이션을 위한 자바스크립트 런타임 환경)

- HTTP (잘 알아둬야함.)

- Tools : Git, Webpack, Babel, ESLint, npm ...

- Library / Framework : SPA(Angular, React, Vue.js), TypeScript, jQuery, Lodash, Axios ...

- TDD(Test Driven Development) : karma / jasmine, mocha, chai

- 알고리즘 / 자료구조

학습할 내용이 매우 많고, 범위가 넓다. 순서를 정해두고 차근 차근 공부할 필요가 있다.

## ⁉️ 초심자가 경험하는 3가지 어려움

1. 책이나 수업의 내용이 하나도 모르는 경우 + 주변 개발자들의 말을 알아 들을 수 없는 경우

   -> 배경 지식 : 기본적인 CS 지식(Memory,CPU,이진수 등) + 용어에 대한 이해() + 기본 상식을 갖출 필요가 있음.

2. 어떻게 만들어야 할 지 감조차 오지 않는 경우

   -> 문제 해결 능력 : 문제(해결 과제)가 무엇인지 알아채는 능력 + Computational thinking + 알고리즘 / 자료구조 + 많은 경험 등을 총체적으로 묶은 개념

   - 문제 해결 능력 = 해결 과제(문제/요구사항)의 명확한 이해가 필요함 -> 복잡함을 단순하게 분해 -> 자료를 정리하고 구분(Modeling) -> 순서에 맞게 행위를 배열

3. 어떻게 만들어야 할 지는 알겠는데 막상 코딩하려니 불가능한 경우 + 인터넷에서 글어온 코드를 수정할 수 없는 경우

   -> 구현 능력 : 문법에 대한 정확한 이해가 필요함 + 많은 연습

   get.addEventListener등의 이벤트등을 활용할 필요가 있음.

## ⛳️ 공부 방법

**단순 반복 != 의식적인 연습**

의식적인 연습을 꾸준히 반복하는 만큼 성장한다.

시행착오는 내가 무엇을 알고 무엇을 모르는지를 알게하는 과정이다.

무엇을 모르는지 알았다면 몰랐던 것을 아기 위해 시도하고 실패하는 의식적인 연습을 반복하는 것이 중요하다.

이 과정에서 모르는것이 너무 많다면 베이스가 되는 구체적 목표를 수립하고 작은 성취를 반복하자.

수박 겉핥기식 학습은 문제가 있다. -> 본질에서 벗어난 학습법에 해당함. 적절한 지점을 찾아내 균형을 잡는 것또한 능력이다.

피드백에 늘 겸손하고 적극적으로 반응하여 행동을 교정하는 것이 필요하다.

적절한 지점을 찾아내 균형을 잡는 것 또한 능력이다.

## ✨ 마음 가짐

- 서두르지 말기.

- 두려워하지 말고 일단 해보고 실패하기.(실패는 영원하지 않음)

- 사람은 잘 착각하고 또 잘잊는다. 늘 기록하고 수정하자.

- 기본기(JS, HTML, CSS)가 중요하다. 기본기는 알파이자 오메가.

- 일을 좋아하도록 노력하자.

- 호기심을 갖자. 이유를 알고싶지 않은가? -> 설명할 수 없으면 모르는 것이다.(호이스팅, 클로저 등등)

- 꾸준히 노력하자.

---

# step 1 - What is JavaScript?

# 🌈 1. 자바스크립트의 탄생

1995년 당시 약 90%의 시장 점유율로 웹 브라우저 시장을 지배하고 있던 넷스케이프 커뮤니케이션즈(Netscape comunications)는 정적인 HTML을 동적으로 표현하기 위해 경량의 프로그래밍 언어를 도입하기로 결정했다.

그래서 탄생한 언어가 브렌던 아이크(Brendan Eich)가 개발한 `자바스크립트(JavaScript)`이다.

자바스크립트는 1996년 3월 넷스케이프 커뮤니케이션즈의 웹 브라우저인 Netscape Navigator 2에 탑재되었고 “Mocha”로 명명되었다. 그해 9월 “LiveScript”로 이름이 변경되었고, 12월 `“JavaScript”`로 최종 명명되었다.

이렇게 탄생한 자바스크립트는 현재 모든 브라우저의 표준 프로그래밍 언어가 되었다. 그러나 자바스크립트가 순탄하게 성장했던 것은 아니다.

자바스크립트가 탄생한 뒤 얼마 지나지 않아 자바스크립트의 파생 버전인 JScript가 출시되어 자바스크립트는 위기를 맞게 된다.

# 💥 2. 자바스크립트의 파편화와 표준화

1996년 8월, 마이크로소프트는 자바스크립트의 파생 버전인 “JScript”를 Internet Explorer 3.0에 탑재하였다. 그런데 문제는 JScript와 자바스크립트가 표준화되지 못하고 적당히 호환되었다는 것이다.

즉, 자사 브라우저의 시장 점유율을 점유하기 위해 자사 브라우저에서만 동작하는 기능을 경쟁적으로 추가하기 시작했다는 것이다.

이로 인해 브라우저에 따라 웹 페이지가 정상 동작하지 않는 크로스 브라우징 이슈가 발생하기 시작했고 모든 브라우저에서 동작하는 웹 페이지를 개발하는 것은 무척 어려워졌다.

이에 자바스크립트의 파편화를 방지하고 모든 브라우저에서 동일하게 동작하는 표준화된 자바스크립트에 대한 필요성이 제기되기 시작했다.

이를 위해 1996년 11월, 넷스케이프 커뮤니케이션즈는 컴퓨터 시스템의 표준을 관리하는 비영리 표준화 기구인 `ECMA 인터내셔널`에 자바스크립트의 표준화를 요청하였다.

1997년 7월, ECMA-262라 불리는 표준화된 자바스크립트 초판(ECMAScript 1)의 명세(specification)가 완성되었고 상표권 문제로 자바스크립트는 ECMAScript로 명명되었다.

이후 1999년 ECMAScript 3(ES3)이 공개되었고 10년 만인 2009년 출시된 ECMAScript 5(ES5)는 HTML5와 함께 출현한 표준안이다.

2015년 ECMAScript 6(ECMAScript 2015)가 공개되었고 범용 프로그래밍 언어로서 갖추어야 할 `let/const 키워드, 화살표 함수, 클래스, 모듈` 등과 같은 기능들을 대거 도입하는 큰 변화가 있었다. ES6 이후의 버전업은 작은 기능의 추가 레벨로 매년 공개할 것으로 예고되었다. ECMAScript 버전별 특징은 아래와 같다.

|         버전          | 출시년도 |                                                                               특징                                                                               |
| :-------------------: | :------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|          ES1          |   1997   |                                                                               초판                                                                               |
|          ES2          |   1998   |                                                           ISO/IEC 16262 국제 표준과 동일한 규격을 적용                                                           |
|          ES3          |   1999   |                                                                 정규 표현식, try…catch 예외 처리                                                                 |
|          ES5          |   2009   |         HTML5와 함께 출현한 표준안. JSON, strict mode, 접근자 프로퍼티(getter, setter), 향상된 배열 조작 기능(forEach, map, filter, reduce, some, every)         |
| ES6 (ECMAScript 2015) |   2015   | let, const, class, 화살표 함수, 템플릿 리터럴, 디스트럭처링 할당, spread 문법, rest 파라미터, Symbol, Promise, Map/Set, iterator/generator, module import/export |
| ES7 (ECMAScript 2016) |   2016   |                                              지수(\*\*) 연산자, Array.prototype.includes, String.prototype.includes                                              |
| ES8 (ECMAScript 2017) |   2017   |                                 async/await, Object 정적 메소드(Object.values, Object.entries, Object.getOwnPropertyDescriptors)                                 |
| ES9 (ECMAScript 2018) |   2018   |                                                                   Object Rest/Spread 프로퍼티                                                                    |

# 🗓 3. 자바스크립트 성장의 역사

초창기 자바스크립트는 웹 페이지의 보조적인 기능을 수행하기 위해 한정적인 용도로 사용되었다. 이 시기에 대부분 로직은 주로 웹 서버에서 실행되었고 브라우저는 서버로부터 전달받은 HTML과 CSS를 단순히 렌더링하는 수준이었다.

1999년, 자바스크립트를 이용해서 `비동기적(Asynchronous)`으로 서버와 브라우저가 데이터를 교환할 수 있는 통신 기능인 `Ajax(Asynchronous JavaScript and XML)`가 XMLHttpRequest이라는 이름으로 등장했다.

이전의 웹 페이지는 서버로부터 완전한 HTML을 전송 받아 웹 페이지 전체를 렌더링하는 방식으로 동작했다. 따라서 화면이 전환되면 서버로부터 새로운 HTML을 전송 받아 웹 페이지 전체를 처음부터 다시 렌더링하였다.

이는 변경이 없는 부분까지 포함된 HTML을 서버로부터 다시 전송 받기 때문에 불필요한 데이터 통신이 발생하고, 변경이 없는 부분까지 처음부터 다시 렌더링해야 하기 때문에 퍼포먼스 측면에서도 불리한 방식이다. 이로 인해 화면 전환이 일어나면 화면이 순간적으로 깜박이는 현상이 발생하고 이는 웹 애플리케이션의 한계로 받아들여 졌다.

Ajax의 등장은 이전의 패러다임을 획기적으로 전환했다. 즉, 웹 페이지의 변경이 필요 없는 부분은 다시 렌더링하지 않고, 서버로부터 필요한 데이터만을 전송 받아 변경이 필요한 부분만을 한정적으로 렌더링하는 방식이 가능해진 것이다. 이로 인해 웹 브라우저에서도 데스크톱 애플리케이션과 유사한 빠른 퍼포먼스와 부드러운 화면 전환이 가능케 되었다.

2005년, 구글이 발표한 `Google Maps`는 웹 애플리케이션 개발 프로그래밍 언어로서 자바스크립트의 가능성을 확인하는 계기를 마련했다. 웹 브라우저에서 자바스크립트와 Ajax를 기반으로 동작하는 Google Maps가 데스크톱 애플리케이션과 비교해 손색이 없을 정도의 퍼포먼스와 부드러운 화면 전환 효과를 보여준 것이다.

<img src="https://poiemaweb.com/img/Google_Maps_Beta.png">

2006년, jQuery의 등장으로 다소 번거롭고 논란이 있던 DOM(Document Object Model)을 보다 쉽게 제어할 수 있게 되었고 크로스 브라우징 이슈도 어느 정도 해결되었다. jQuery는 넓은 사용자 층을 순식간에 확보했다. 이로 인해 당시 다소 까다로운 자바스크립트보다 배우기 쉽고 직관적인 jQuery를 더 선호하는 개발자가 양산되기도 했다.

Google Maps를 통해 가능성이 확인된 자바스크립트로 웹 애플리케이션을 구축하려는 시도가 늘어가면서 보다 빠르게 동작하는 자바스크립트 엔진이 요구되었다. 2008년 등장한 구글의 V8 자바스크립트 엔진은 이러한 요구에 부합하는 빠른 성능을 보여 주었다. V8 자바스크립트 엔진의 등장으로 자바스크립트는 데스크톱 애플리케이션과 유사한 사용자 경험(user experience)을 제공할 수 있는 웹 애플리케이션 개발 프로그래밍 언어로 정착하게 되었다.

V8 자바스크립트 엔진으로 촉발된 자바스크립트의 발전으로 말마암아 과거 웹 서버에서 수행되던 역할들이 클라이언트(브라우저)로 이동하였고, 이로써 웹 애플리케이션에서 프런트엔드 영역이 주목받는 계기가 되었다.

2009년, 브라우저에서만 동작하던 자바스크립트를 브라우저 이외의 환경에서 동작시킬 수 있는 자바스크립트 실행 환경인 Node.js의 등장으로 자바스크립트는 웹 브라우저를 벗어나 서버 사이드 애플리케이션 개발에서도 사용되는 범용 프로그래밍 언어가 되었다.

웹 브라우저에서만 동작하는 반쪽짜리 프로그래밍 언어 취급을 받던 자바스크립트는 이제 프런트엔드 영역은 물론 백엔드 영역까지 아우르는 웹 프로그래밍 언어의 표준으로 자리잡고 있다.

자바스크립트는 크로스 플랫폼을 위한 가장 중요한 언어로 주목받고 있다. 자바스크립트는 웹은 물론 모바일 `하이브리드 앱(PhoneGap, Ionic)`, `서버 사이드(NodeJS)`, `데스크톱(Electron)`, `머신 러닝(TensorFlow.js)`, `로보틱스(Johnny-Five)` 프로그래밍 언어로서 세계에서 가장 인기있는 프로그래밍 언어이다.

<img src="https://poiemaweb.com/img/most-Popular-technologies.png">

이제 웹 애플리케이션은 데스크톱 애플리케이션과 비교해도 손색없는 성능과 사용자 경험을 제공하는 것이 필수가 되었고, 개발 규모와 복잡도도 더불어 상승했다. 이전의 개발 방식으로는 복잡해진 개발 과정을 수행하기 어려워졌고, 이러한 필요에 따라 많은 패턴과 라이브러리가 출현하였다. 이는 개발에 많은 도움을 주었지만 유연하면서 확장이 쉬운 애플리케이션 아키텍처 구축을 어렵게 하였고 필연적으로 `프레임워크`가 등장하게 되었다.

또한 SPA(Single Page Application)가 대중화되면서 Angular, React, Vue.js 등 다양한 SPA 프레임워크/라이브러리 또한 많은 사용층을 확보하고 있다.

# 4. JavaScript와 ECMAScript

`ECMAScript`는 자바스크립트의 표준 명세인 ECMA-262를 말하며 프로그래밍 언어의 타입, 값, 객체와 프로퍼티, 함수, 빌트인 객체 등 `핵심 문법(core syntax)`을 규정한다. 각 브라우저 제조사는 `ECMAScript`를 준수하여 브라우저에 내장되는 자바스크립트 엔진을 구현한다.

자바스크립트는 일반적으로 프로그래밍 언어로서 기본 뼈대를 이루는 ECMAScript와 브라우저가 별도 지원하는 클라이언트 사이드 `Web API`, 즉 (DOM, BOM, Canvas, XMLHttpRequest, Fetch, requestAnimationFrame, SVG, Web Storage, Web Component, Web worker) 등을 아우르는 개념이다.

클라이언트 사이드 Web API는 ECMAScript와는 별도로 World Wide Web Consortium (W3C)에서 별도의 명세로 관리하고 있다. 클라이언트 사이드 Web API의 자세한 내용은 MDN web [docs: Web API](https://developer.mozilla.org/ko/docs/Web/API)를 참고하기 바란다.

# 5. 자바스크립트의 특징

# 함수 호이스팅

자바스크립트는 ES6의 let, const를 포함하여 모든 선언(var, let, const, function, function\*, class)을 `호이스팅(Hoisting)`한다.

호이스팅이란 여러번 공부했듯이 var 선언문이던 function 선언문이던 모든 선언문이 해당 Scope의 선두로 옮겨진 것처럼 동작하는 특성을 말한다.

즉 자바스크립트는 모든 선언문(var, let, const, function, function\*,class)등이 선언되기 이전에 참조가 가능하다.

함수 선언문으로 정의된 함수는 자바스크립트 엔진이 스크립트가 로딩되는 시점에 바로 초기화되고 이를 VO(variable object)에 저장한다.

즉, 함수 선언, 초기화, 할당이 한번에 이뤄진다. 그렇기 때문에 함수 선언의 위치와 상관없이 소스 내 어느 곳에서든지 호출이 가능해진다.

그러나 주의할 점은 함수 표현식으로 함수를 정의한 경우이다.

> EX )

```js
var res = square(5); // TypeError: square is not a function

var square = function (number) {
  return number * number;
};
```

함수 선언문의 경우와는 달리 TypeError가 발생하였다. 함수 표현식의 경우 함수 호이스팅이 아니라 변수 호이스팅이 발생하기 떄문이다.

변수 호이스팅은 변수의 생성 및 초기화와 할당이 분리되어 진행된다. 호이스팅된 변수는 할당이 이뤄지지 않았기 떄문에 undefined로 초기화 되고 실제값의 할당은 할당문에서 이뤄진다.

함수 표현식은 함수 선언문과는 달리 스크립트 로딩 시점에 변수 객체(VO)에 함수를 할당하지 않고 runtime에 해석되고 실행되므로 이 두가지를 구분하는 것은 중요하다.

JavaScript: The Good Parts의 저자이며 자바스크립트의 권위자인 더글러스 크락포드(Douglas Crockford)는 이와 같은 문제 때문에 함수 표현식만을 사용할 것을 권고하고 있다. 함수 호이스팅이 함수 호출 전 반드시 함수를 선언하여야 한다는 규칙을 무시하므로 코드의 구조를 엉성하게 만들 수 있다고 지적한다.

또한 함수 선언문으로 함수를 정의하면 사용하기에 쉽지만 대규모 애플리케이션을 개발하는 경우 인터프리터가 너무 많은 코드를 변수 객체(VO)에 저장하므로 애플리케이션의 응답속도는 현저히 떨어질 수 있으므로 주의해야 할 필요가 있다.

# First-class object (일급 객체)

일급 객체(first-class object)란 생성, 대입, 연산, 인자 또는 반환값으로서의 전달 등 프로그래밍 언어의 기본적 조작을 제한없이 사용할 수 있는 대상을 의미한다.

다음 조건을 만족하면 일급 객체로 간주한다.

1. 무명의 리터럴로 표현이 가능하다.
2. 변수나 자료 구조(객체, 배열 등)에 저장할 수 있다.
3. 함수의 매개변수에 전달할 수 있다.
4. 반환값으로 사용할 수 있다.

# 순수 함수(Pure function), 비순수 함수(Impure function)

함수중에서 원시 타입의 인수는 값을 복사하여 매개변수에 전달하기 때문에, 함수 몸체에서 그값을 변경하여도 어떠한 부수 효과(side-effect)도 발생시키지 않는다.

하지만 객체형 인수는 참조값을 매개변수에 전달하기 때문에 함수 몸체에서 그 값을 변경할 경우 원본 객체가 변경되는 부수 효과(side-effect)가 발생한다.

이와 같이 부수효과를 발생시키는 비순수 함수(Impure function)는 복잡성을 증가시킨다. 비순수 함수를 최소환으로 줄이는 것이 부수 효과를 최대한 억제하는 것과 같고 디버깅을 쉽게 만드는 방법이다.

한마디로 어떤 외부 상태도 변경하지 않는 함수를 순수함수(Pure function), 외부 상태도 변경시키는 부수 효과(side-effect)가 발생시키는 함수를 비순수 함수(Impure function)이라고 한다.

# arguments 프로퍼티

arguments 객체는 함수 호출 시 전달된 인수(argument)들의 정보를 담고 있는 순회가능한(iterable) 유사 배열 객체(array-like object)이며 함수 내부에서 지역변수처럼 사용된다. 즉, 함수 외부에서는 사용할 수 없다.

> EX )

```js
function multiply(x, y) {
  console.log(arguments);
  return x * y;
}

multiply(); // NAN {}
multiply(1); // NAN { '0': 1 }
multiply(1, 2); // 2 { '0': 1, '1': 2 }
multiply(1, 2, 3); // 2 { '0': 1, '1': 2, '2': 3 }
```

# caller 프로퍼티

caller 프로퍼티는 자신을 호출한 함수를 의미한다.

> EX )

```js
function foo(func) {
  var res = func();
  return res;
}

function bar() {
  return "caller : " + bar.caller;
}

console.log(foo(bar));
// caller : function foo(func) {
//     var res = func();
//     return res;
// } 출력
console.log(bar()); // caller : null 출력
```

# 즉시 실행 함수

함수의 정의와 동시에 실행되는 함수를 `즉시 실행 함수(IIFE, Immediately Invoke Function Expression)`라고 한다. 최초 한번만 호출되며 다시 호출할 수는 없다. 이러한 특징을 이용하여 최초 한번만 실행이 필요한 초기화 처리등에 사용할 수 있다.

> EX )

```js
// 기명 즉시 실행 함수(named immediately-invoked function expression)
(function myFunction() {
  var a = 3;
  var b = 5;
  return a * b;
}());

// 익명 즉시 실행 함수(immediately-invoked function expression)
(function () {
  var a = 3;
  var b = 5;
  return a * b;
}());

// SyntaxError: Unexpected token (
// 함수선언문은 자바스크립트 엔진에 의해 함수 몸체를 닫는 중괄호 뒤에 ;가 자동 추가된다.
function () {
  // ...
}(); // => };();

// 따라서 즉시 실행 함수는 소괄호로 감싸준다.
(function () {
  // ...
}());

(function () {
  // ...
})();
```

자바스크립트에서 가장 큰 문제점 중의 하나는 파일이 분리되어 있다하여도 글로벌 스코프가 하나라는 점, 글로벌 스코프에 선언된 변수나 함수는 코드 내의 어디서든지 접근이 가능하다는 점이다.

따라서 다른 스크립트 파일 내에서 동일한 이름으로 명명된 변수나 함수가 같은 스코프 내에 존재할 경우 원치 않는 결과를 가져올 수 있다.

즉시 실행 함수 내에 처리 로직을 모아 두면 혹시 있을 수도 있는 변수명 또는 함수명의 충돌을 방지할 수 있어 이를 위한 목적으로 즉시실행함수를 사용되기도 한다.

특히 jQuery와 같은 라이브러리의 경우, 코드를 즉시 실행 함수 내에 정의해 두면 라이브러리의 변수들이 독립된 영역 내에 있게 되므로 여러 라이브러리들은 동시에 사용하더라도 변수명 충돌과 같은 문제를 방지할 수 있다.

화살표 함수는 즉시실행 불가.

# 스코프

## 렉시컬 스코프

> EX )

```js
var x = 1;

function foo() {
  var x = 10;
  bar();
}

function bar() {
  console.log(x);
}

foo(); // 1
bar(); // 1
```

위의 예제를 처음 봤을땐 10 , 1이 출력될것이라 생각했었따. 그러나 어림없는 소리. 1, 1이 출력되었고 이러한 결과가 나온대에는 이유가 있었다.

스코프 범위를 어디로 하느냐는 두가지 패턴이 존재하는데

1. 함수를 어디서 `호출`하였는지에 따라 상위 스코프를 결정하는 것.
2. 함수를 어디서 `선언`하였는지에 따라 상위 스코프를 결정하는 것.

1번의 방식이었다면 위 예제에서 10, 1이 출력되었겠지만, 결과물은 1,1 즉 2번의 방식이다.

프로그래밍 언어는 이 두가지 방식 중 하나의 방식으로 함수의 상위 스코프를 결정한다.

1번의 방식을 `동적 스코프(Dynamic scope)`라 하고

2번의 방식을 `렉시컬 스코프(Lexical scope)` 혹은 `정적 스코프(Static scope)`라 한다.

문제는 자바스크립트를 비롯한 대부분의 프로그래밍 언어는 `렉시컬 스코프`를 따른다는 점이다.

`렉시컬 스코프는 함수를 어디서 호출하는지가 아니라 어디에 선언하였는지에 따라 결정된다.` 자바스크립트는 렉시컬 스코프를 따르므로 함수를 선언한 시점에 상위 스코프가 결정된다.

함수를 어디에서 호출했는가는 스코프 결정에 있어 아무런 의미를 주지 않는다.

## 암묵적 젼역

예제를 통해 알아봐야 하는 항목이므로 예제를 우선 보자.

> EX )

```js
var x = 10; // 전역 변수

function foo() {
  // 선언하지 않은 식별자
  y = 20;
  console.log(x + y);
}

foo(); // 30
```

위 예제에서 y는 선언하지 않은 식별자이다. 따라서 y = 20이 실행되면 참조 에러가 발생할 것처럼 보인다.

하지만 선언하지 않은 식별자 y는 마치 선언된 변수처럼 동작한다. 이는 선언하지 않은 식별자에 값을 할당하면 전역 객체의 프로퍼티가 되기 떄문이다.

foo 함수가 호출되면 자바스크립트 엔진은 변수 y에 값을 할당하기 위해 먼저 스코프 체인을 통해 선언된 변수인지 확인한다.

이때 foo함수의 스코프와 전역 스코프 어디에서도 변수 y의 선언을 찾아볼 수 없으므로 참조 에러가 발생해야 하지만 자바스크립트 엔진은 `y = 20`을 `window.y = 20`으로 해석해버려 프로퍼티를 동적으로 생성한다.

결국 y는 전역 객체의 프로퍼티가 되어 마치 전역 변수처럼 동작한다. 이러한 현상을 `암묵적 전역(implicit global)`이라고 한다.

하지만 y는 변수 선언없이 단지 전역 객체의 프로퍼티로 추가되었을 뿐이다.

따라서 y는 변수가 아니다. 따라서 `변수가 아닌 y는 변수 호이스팅이 발생하지 않는다.`

## 최소한의 전역변수 사용

전역변수 사용을 최소화하는 방법 중 하나는 어플리케이션에서 전역변수 사용을 위해 다음과 같이 전역변수 객체 하나를 만들어 사용하는 방법이라고 한다.(무려 더글라스 크락포드의 제안이라고 함)

> EX )

```js
var MYAPP = {};

MYAPP.student = {
  name: "Lee",
  gender: "male",
};

console.log(MYAPP.student.name);
```

## 즉시실행함수를 이용한 전역변수 사용 억제 방법

전역변수 사용을 억제하기 위한 또 하나의 방법은 즉시 실행 함수(IIFE, Immediately-Invoked Function Expression)을 사용하는 것이다.

이 방법을 사용하면 전역변수를 만들지 않아 라이브러리 등에서 자주 사용되는 방법이다. 즉시 실행되고 전역에서 바로 사라지기 때문

> EX )

```js
(function () {
  var MYAPP = {};

  MYAPP.student = {
    name: "Lee",
    gender: "male",
  };

  console.log(MYAPP.student.name);
})(); // Lee 출력

console.log(MYAPP.student.name); //Uncaught ReferenceError: MYAPP is not defined 에러 출력
```

# this

함수 호출 방식과 this 바인딩

자바스크립트의 경우 함수 호출 방식에 의해 this에 바인딩할 어떤 객체가 동적으로 결정된다. 다시 말해, 함수를 선언할 때 this에 바인딩할 객체가 정적으로 결정되는 것이 아니고, `함수를 호출할 때 함수가 어떻게 호출되었는지에 따라` this에 바인딩할 객체가 동적으로 결정된다.

```
함수의 상위 스코프를 결정하는 방식인 렉시컬 스코프(Lexical scope)는 함수를 선언할 때 결정된다. this 바인딩과 혼동하지 않도록 주의해야한다.
```

함수의 호출 방식들

1. 함수 호출
2. 메소드 호출
3. 생성자 함수 호출
4. apply / call / bind 호출

> EX )

```js
var foo = function () {
  console.dir(this);
};

// 1. 함수 호출
foo(); // window
// window.foo();

// 2. 메소드 호출
var obj = { foo: foo };
obj.foo(); // obj

// 3. 생성자 함수 호출
var instance = new foo(); // instance

// 4. apply/call/bind 호출
var bar = { name: "bar" };
foo.call(bar); // bar
foo.apply(bar); // bar
foo.bind(bar)(); // bar
```

## 1. 함수 호출

전역 객체(Global Object)는 모든 객체의 유일한 최상위 객체를 의미하며 일반적으로 Browser-side에서는 window, Server-side(Node.js)에서는 global 객체를 의미한다.

> EX )

```js
// in browser console
this === window; // true

// in Terminal
node;
this === global; // true
```

전역객체는 전역 스코프(Global Scope)를 갖는 전역변수(Global variable)를 프로퍼티로 소유한다. 글로벌 영역에 선언한 함수는 전역객체의 프로퍼티로 접근할 수 있는 전역 변수의 메소드이다.

> EX )

```js
var ga = "Global variable";

console.log(ga);
console.log(window.ga);

function foo() {
  console.log("invoked!");
}
foo(); // invoked! 출력
window.foo(); // invoked! 출력
```

기본적으로 `this`는 전역객체(Global object)에 바인딩된다. 전역함수는 물론이고 심지어 내부함수의 경우에도 `this`는 외부함수가 아닌 전역객체에 바인딩 된다.

> EX )

```js
function foo() {
  console.log("foo's this: ", this); // window
  function bar() {
    console.log("bar's this: ", this); // window
  }
  bar();
}
foo(); // window 두번 출력
```

또한 메소드으 내부함수일지라도 해당 내부함수가 객체의 프로퍼티가 아닌 이상 `this`는 전영객체에 바인딩된다.

```js
var value = 1;

var obj = {
  value: 100,
  foo: function () {
    console.log("foo's this: ", this); // obj
    console.log("foo's this.value: ", this.value); // 100
    function bar() {
      console.log("bar's this: ", this); // window
      console.log("bar's this.value: ", this.value); // 1
    }
    bar();
  },
};

obj.foo();
// foo's this:  {value: 100, foo: ƒ}
// foo's this.value :  100
// bar's this :  Window {0: global, window: Window, self: Window, document: document, name: '', location: Location, …}
// bar's this.value :  1
```

콜백함수의 경우에도 `this`는 프로퍼티로써 이용되도 전역객체에 바인딩된다.

> EX )

```js
var value = 1;

var obj = {
  value: 100,
  foo: function () {
    setTimeout(function () {
      console.log("callback's this: ", this); // window
      console.log("callback's this.value: ", this.value); // 1
    }, 100);
  },
};

obj.foo();
// callback's this :  Window {0: global, window: Window, self: Window, document: document, name: '', location: Location, …}
// callback's this.value :  1
```

**내부함수는 일반 함수, 메소드, 콜백함수 어디에서 선언되었든 관게없이 this는 전역객체를 바인딩한다.** 더글라스 크락포드는 “이것은 설계 단계의 결함으로 메소드가 내부함수를 사용하여 자신의 작업을 돕게 할 수 없다는 것을 의미한다” 라고 말한다. 내부함수의 `this`가 전역객체를 참조하는 것을 회피방법은 아래와 같다.

> EX )

```js
var value = 1;

var obj = {
  value: 100,
  foo: function () {
    var that = this; // Workaround : this === obj

    console.log("foo's this: ", this); // obj
    console.log("foo's this.value: ", this.value); // 100
    function bar() {
      console.log("bar's this: ", this); // window
      console.log("bar's this.value: ", this.value); // 1

      console.log("bar's that: ", that); // obj
      console.log("bar's that.value: ", that.value); // 100
    }
    bar();
  },
};

obj.foo();
```

이미지로 나타내면 다음과 같다.

<img src="https://poiemaweb.com/img/Function_Invocation_Pattern.png">

위 방법 이외에도 자바스크립트는 this를 명시적으로 바인딩할 수 있는 apply, call, bind등의 메소드를 제공한다.

> EX )

```js
var value = 1;

var obj = {
  value: 100,
  foo: function () {
    console.log("foo's this: ", this); // foo's this:  {value: 100, foo: ƒ}
    console.log("foo's this.value: ", this.value); // foo's this.value:  100
    function bar(a, b) {
      console.log("bar's this: ", this); // obj
      console.log("bar's this.value: ", this.value); // 100
      console.log("bar's arguments: ", arguments);
    }
    bar.apply(obj, [1, 2]); // bar's this:  {value: 100, foo: ƒ}
    // bar's this.value:  100
    // bar's arguments:  Arguments(2) [1, 2, callee: ƒ, Symbol(Symbol.iterator): ƒ]
    bar.call(obj, 1, 2); // bar's this:  {value: 100, foo: ƒ}
    // bar's this.value:  100
    // bar's arguments:  Arguments(2) [1, 2, callee: ƒ, Symbol(Symbol.iterator): ƒ]
    bar.bind(obj)(1, 2); // bar's this:  {value: 100, foo: ƒ}
    // bar's this.value:  100
    // bar's arguments:  Arguments(2) [1, 2, callee: ƒ, Symbol(Symbol.iterator): ƒ]
  },
};

obj.foo();
```


## 3. 생성자 함수 호출

자바스크립트의 생성자 함수는 말 그대로 객체를 생성하는 역할을 한다. 하지만 자바와 같은 객체지향 언어의 생성자 함수와는 다르게 그 형식이 정해져 있는 것이 아니라 기존 함수에 new 연산자를 붙여서 호출하면 해당 함수는 생성자 함수로 동작한다.

이는 반대로 생각하면 생성자 함수가 아닌 일반 함수에 new 연산자를 붙여 호출하면 생성자 함수처럼 동작할 수 있다. 따라서 일반적으로 생성자 함수명은 첫문자를 대문자로 기술하여 혼란을 방지하려는 노력을 한다고 한다.

> EX )
```js
// 생성자 함수
function Person(name) {
  this.name = name;
}

var me = new Person('Lee');
console.log(me); // Person&nbsp;{name: "Lee"}

// new 연산자와 함께 생성자 함수를 호출하지 않으면 생성자 함수로 동작하지 않는다.
var you = Person('Kim');
console.log(you); // undefined
```
new 연산자와 함께 생성자 함수를 호출하면 this 바인딩이 메소드나 함수 호출 때와는 다르게 동작한다.

-> 생성할때 그냥 해당 메소드들을 복사하는 느낌(?)


## 3.2 객체 리터럴 방식과 생성자 함수 방식의 차이

객체 리터럴 방식과 생성자 함수 방식의 차이를 비교해 보자.

```js
// 객체 리터럴 방식
var foo = {
  name: 'foo',
  gender: 'male'
}

console.dir(foo); // Object 출력

// 생성자 함수 방식
function Person(name, gender) {
  this.name = name;
  this.gender = gender;
}

var me  = new Person('Lee', 'male');
console.dir(me); // Person 출력

var you = new Person('Kim', 'female');
console.dir(you); // Person 출력
```
객체 리터럴 방식과 생성자 함수 방식의 차이는 프로토타입 `객체([[Prototype]])`에 있다.

* `객체 리터럴 방식`의 경우, 생성된 객체의 프로토타입 객체는 Object.prototype이다.
* `생성자 함수 방식`의 경우, 생성된 객체의 프로토타입 객체는 Person.prototype이다.

## 3.3 생성자 함수에 new 연산자를 붙이지 않고 호출할 경우

**일반함수와 생성자 함수에 특별한 형식적 차이는 없으며 함수에 new 연산자를 붙여서 호출하면 해당 함수는 생성자 함수로 동작한다.**

그러나 객체 생성 목적으로 작성한 생성자 함수를 new 없이 호출하거나 일반함수에 new를 붙여 호출하면 오류가 발생할 수 있다. 

일반함수와 생성자 함수의 호출시 `this 바인딩 방식이 다르기 떄문`.

일반 함수를 호출하면 this는 전역객체에 바인딩되지만 new 연산자와 함께 생성자 함수를 호출하면 this는 생성자 함수가 암묵적으로 생성한 빈 객체에 바인딩 된다.

## 4. apply/call/bind 호출

this에 바인딩될 객체는 함수 호출 패턴에 의해 결정된다. 이는 자바스크립트 엔진이 수행하는 것이다.

이러한 자바스크립트 엔진의 암묵적 this 바인딩 이외에 this를 특정 객체에 명시적으로 바인딩하는 방법도 제공된다. 

이것을 가능하게 하는 것이 `Function.prototype.apply`, `Function.prototype.call` 메소드이다.

이 메소드들은 모든 함수 객체의 프로토타입 객체인 Function.prototype 객체의 메소드이다.

```js
func.apply(thisArg, [argsArray])

// thisArg: 함수 내부의 this에 바인딩할 객체
// argsArray: 함수에 전달할 argument의 배열
```

기억해야 할 것은 apply() 메소드를 호출하는 주체는 함수이며 apply() 메소드는 this를 특정 객체에 바인딩할 뿐 본질적인 기능은 함수 호출이라는 것이다.

> EX )
```js
var Person = function (name) {
  this.name = name;
};

var foo = {};

// apply 메소드는 생성자함수 Person을 호출한다. 이때 this에 객체 foo를 바인딩한다.
Person.apply(foo, ['name']);

console.log(foo); // { name: 'name' }
```
빈 객체 foo를 apply() 메소드의 첫번째 매개변수에, argument의 배열을 두번째 매개변수에 전달하면서 Person 함수를 호출하였다.

이때 Person 함수의 this는 foo 객체가 된다. Person 함수는 this의 name 프로퍼티에 매개변수 name에 할당된 인수를 할당하는데 this에 바인딩된 foo 객체에는 name 프로퍼티가 없으므로 name 프로퍼티가 동적 추가되고 값이 할당된다.

apply() 메소드의 대표적인 용도는 arguments 객체와 같은 유사 배열 객체에 배열 메소드를 사용하는 경우이다. arguments 객체는 배열이 아니기 때문에 slice() 같은 배열의 메소드를 사용할 수 없으나 apply() 메소드를 이용하면 가능하다.

> EX )
```js
function convertArgsToArray() {
  console.log(arguments);

  // arguments 객체를 배열로 변환
  // slice: 배열의 특정 부분에 대한 복사본을 생성한다.
  var arr = Array.prototype.slice.apply(arguments); // arguments.slice
  // var arr = [].slice.apply(arguments);

  console.log(arr);
  return arr;
}

convertArgsToArray(1, 2, 3);
```
Array.prototype.slice.apply(arguments)는 “Array.prototype.slice() 메소드를 호출하라. 단 this는 arguments 객체로 바인딩하라”는 의미가 된다. 

결국 Array.prototype.slice() 메소드를 arguments 객체 자신의 메소드인 것처럼 arguments.slice()와 같은 형태로 호출하라는 것이다.

<img src="https://poiemaweb.com/img/apply.png">

call() 메소드의 경우, apply()와 기능은 같지만 apply()의 두번째 인자에서 배열 형태로 넘긴 것을 각각 하나의 인자로 넘긴다.

```js
Person.apply(foo, [1, 2, 3]);

Person.call(foo, 1, 2, 3);
```

apply()와 call() 메소드는 콜백 함수의 this를 위해서 사용되기도 한다.

# 실행 컨텍스트 -> 무조건 복습, 너무 어려움

실행 컨텍스트(Execution Context)는 scope, hoisting, this, function, closure 등의 동작원리를 담고 있는 자바스크립트의 핵심원리이다. 실행 컨텍스트를 바로 이해하지 못하면 코드 독해가 어려워지며 디버깅도 매우 곤란해 질 것이다.

ECMAScript 스펙에 따르면 실행 컨텍스트를 **실행 가능한 코드를 형상화하고 구분하는 추상적인 개념**이라고 정의한다. 좀 더 쉽게 말하자면 **실행 컨텍스트는 실행 가능한 코드가 실행되기 위해 필요한 환경** 이라고 말할 수 있겠다. 여기서 말하는 실행 가능한 코드는 아래와 같다.

* 전역 코드 : 전역 영역에 존재하는 코드
* Eval 코드 : eval 함수로 실행되는 코드
* 함수 코드 : 함수 내에 존재하는 코드

일반적으로 실행 가능한 코드는 전역 코드와 함수 내 코드이다.

자바스크립트 엔진은 코드를 실행하기 위하여 실행에 필요한 여러가지 정보를 알고 있어야 한다. 실행에 필요한 여러가지 정보란 아래와 같은 것들이 있다.

* 변수 : 전역변수, 지역변수, 매개변수, 객체의 프로퍼티
* 함수 선언
* 변수의 유효범위(Scope)
* this

이와 같이 실행에 필요한 정보를 형상화하고 구분하기 위해 자바스크립트 엔진은 실행 컨텍스트를 물리적 객체의 형태로 관리한다. 