# CSS 요소 정리

# CSS란?

CSS는 Cascading Style Sheets의 약자로

HTML,XHTML,XML 같은 문서의 스타일을 꾸밀 때 사용하는 스타일 시트 언어이다.

HTML4 부터는 이러한 모든 서식 설정을 HTML 문서로부터 따로 분리하는 것이 가능하다.

# CSS를 사용하는 이유

HTML만으로 웹 페이지를 제작할 경우 HTML 요소의 세부 스타일을 일일이 따로 지정해 주어야만 한다.

이 작업은 매우 많은 시간이 걸리며, 완성한 후에도 스타일의 변경 및 유지 보수가 매우 힘들어진다.

이러한 문제점을 해소하기 위해 W3C(World Wide Web Consortium)에서 만든 스타일 시트 언어가 바로 CSS이다.

CSS는 웹 페이지의 스타일을 별도의 파일로 저장할 수 있게 해주므로 사이트의 전체 스타일을 손쉽게 제어할 수 있다.

웹 사이트의 스타일을 일관성 있게 유지할 수 있게 해주며, 그에 따른 유지 보수 또한 쉬워진다.

이러한 외부 스타일 시트는 보통 확장자를 .css 파일로 저장한다.

# CSS 문법

<img src="http://tcpschool.com/lectures/img_css_syntax.png" alt="css 이미지 설명 파일">

CSS의 문법은 선택자(selector)와 선언부(declaratives)로 구성된다.

선택자는 CSS를 적용하고자 하는 HTML 요소(element)를 가리킨다.

선언부는 하나 이상의 선언들을 세미콜론(;)으로 구분하여 포함할 수 있으며, 중괄호({ })를 사용하여 전체를 둘러싼다.

각 선언은 CSS 속성명(property)과 속성값(value)을 가지며, 그 둘은 콜론(:)으로 연결된다.

이러한 CSS 선언(declaration)은 언제나 마지막에 세미콜론(;)으로 끝마친다.

# CSS 선택자

스타일을 적용할 HTML 요소를 가리키는 데 사용하는 선택자는
다음과 같다.

-   HTML 요소 선택자
-   아이디(id) 선택자
-   클래스(class) 선택자
-   그룹(group) 선택자

> HTML 요소 선택자

CSS를 적용할 대상으로 HTML 요소의 이름을 직접 사용하여 선택할 수 있다.

태그를 직접 입력함으로써 사용한다.

```html
<style>
    h2 {
        color: teal;
        text-decoration: underline;
    }
</style>

<h1>HTML 요소 선택자를 이용한 선택</h1>
<h2>이 부분에 스타일을 적용합니다.</h2>
<p>
    요소 선택자를 이용하여 스타일을 적용할 HTML 요소를 직접 선택할 수 있습니다.
</p>
```

[실습 링크](http://tcpschool.com/examples/tryit/tryhtml.php?filename=css_intro_syntax_01)

> 아이디(id) 선택자

아이디 선택자는 CSS를 적용할 대상으로 특정 요소를 선택할 때 사용한다.

이 선택자는 웹 페이지에 포함된 여러 요소 중에서 특정 아이디 이름을 가지는 요소만을 선택해준다.

주로 `#아이디명`으로 사용한다.

EX)

<style>
    #heading { color: teal; text-decoration: line-through; }
</style>

<h2 id="heading">이 부분에 스타일을 적용합니다.</h2>

HTML과 CSS에서는 하나의 웹 페이지에 속하는 여러 요소에 같은 아이디 이름을 사용해도 별 문제없이 동작한다.

하지만 이렇게 중복된 아이디를 가지고 자바스크립트 작업을 하게 되면 오류가 발생한다.

따라서 되도록이면 하나의 웹 페이지에 속하는 요소에는 다른 아이디 이름을 사용하거나 클래스를 사용하는 것이 좋다.

> 클래스(Class) 선택자

클래스 선택자는 특정 집단의 여러 요소를 한 번에 선택할 때 사용한다.

이러한 특정 집단을 클래스(class)라고 하며, 같은 클래스 이름을 가지는 요소들을 모두 선택해 준다.

주로 `.클래스명`으로 사용한다.

## EX )

<style>
    .headings { color: lime; text-decoration: overline; }
</style>

...

<h2 class="headings">이 부분에 스타일을 적용합니다.</h2>
<p>class 선택자를 이용하여 스타일을 적용할 HTML 요소들을 한 번에 선택할 수 있습니다.</p>
<h3 class="headings">이 부분에도 같은 스타일을 적용합니다.</h3>

예제 코딩)

```html
<style>
    .headings {
        color: lime;
        text-decoration: overline;
    }
</style>

<h2 class="headings">이 부분에 스타일을 적용합니다.</h2>
<p>
    class 선택자를 이용하여 스타일을 적용할 HTML 요소들을 한 번에 선택할 수
    있습니다.
</p>
<h3 class="headings">이 부분에도 같은 스타일을 적용합니다.</h3>
```

> 그룹(group) 선택자

그룹 선택자는 위에서 언급한 여러 선택자를 같이 사용하고자 할 때 사용한다.

그룹 선택자는 여러 선택자를 쉼표(,)로 구분하여 연결한다.

그룹 선택자는 코드를 중복해서 작성하지 않도록 하여 코드를 간결하게 만들어 준다.

## EX )

```html
<style>
    h1 {
        color: navy;
    }
    h1,
    h2 {
        text-align: center;
    }
    h1,
    h2,
    p {
        background-color: lightgray;
    }
</style>
```

[실습링크](http://tcpschool.com/examples/tryit/tryhtml.php?filename=css_intro_syntax_04)

> CSS 주석(comments)

주석(comment)이란 개발자가 작성한 해당 코드에 대한 이해를 돕는 설명이나 디버깅을 위해 작성한 구문을 의미한다.

이러한 주석은 다른 CSS 코드와는 달리 웹 브라우저에 의해 해석되지 않는다.

> 문법

```
/* 주석내용 */
```

## EX )

```html
<style>
    p {
        color: teal; /*이것은 한 줄짜리 주석입니다.*/
        font-size: 30px;
    }
    /* 
이것은 두 줄짜리 주석입니다.
몇 줄이라도 가능합니다. 
*/
</style>
```

-   다른 주석문들과 마찬가지로 CSS에서 주석을 작성할 때는 절대로 주석 내부에 또 다른 주석을 넣어서는 안 된다.

---

## CSS-Element

### padding

컨텐츠 안을 차지하는 스페이스를 의미한다.

margin과는 반대로 작용함. padding을 키우면 컨텐츠 블록의 크기가 padding의 크기만큼 커짐.

### margin

컨텐츠 밖을 띄워주는 스페이스를 의미한다.

보통 컨텐츠(블록)간의 간격을 줄 때 사용한다고 보면 된다. margin을 키우면 컨텐츠(블록)나 아티클간의 간격이 벌어진다.

---

## `<input>` 요소

<input> 의 형태와 같이 입력창이 나타나는 요소.
html에서 input type으로 입력 타입(type)을 설정할 수 있다.

종류는 수없이 많은데

-   `<input type="button"> ` = <input type="button">
-   `<input type="checkbox">` = <input type="checkbox">
-   `<input type="color">` = <input type="color">
-   `<input type="date">` = <input type="date">
-   `<input type="datetime-local">` = <input type="datetime-local">
-   `<input type="email">` = <input type="email">
-   `<input type="file">` = <input type="file">
-   `<input type="hidden">` = <input type="hidden">
-   `<input type="image">` = <input type="image">
-   `<input type="month">` = <input type="month">
-   `<input type="number">` = <input type="number">
-   `<input type="password">` = <input type="password">
-   `<input type="radio">` = <input type="radio">
-   `<input type="range">` = <input type="range">
-   `<input type="reset">` = <input type="reset">
-   `<input type="search">` = <input type="search">
-   `<input type="submit">` = <input type="submit">
-   `<input type="tel">` = <input type="tel">
-   `<input type="text">` = <input type="text">
-   `<input type="time">` = <input type="time">
-   `<input type="url">` = <input type="url">
-   `<input type="week">` = <input type="week">

등이 있다.

### Input Type: text

<input type="text"> 텍스트 입력(text input)위 한 줄의 입력 필드를 정의한다.

### Input Type: password

<input type="password"> 는 password 필드를 정의한다.

password 필드의 문자는 별표나 동그라 미로 표시로 가려진다.

### Input Type: date

<input type="date"> 는 사용자가 날짜를 포함해야 하는 입력 필드에 사용됩니다.

브라우저의 지원에 따라서, 날짜 선택기(date picker)가 입력 필드로 표시될 수도 있다.

---

# border

html에서와 css에서의 border은 성격이 다소 다른데 CSS에서의 border 위주로 우선 설명을 적어보자.

border : 선 너비, 선 모양, 선 색상 등을 지정할 수 있다.

1. 선 두께(border-width) : 픽셀로 임의 지정하거나 , thin, medium, thick등으로 지정 가능.
2. 선 모양(border-style) : none, dotted, dashed, solid, double, groove, ridge, inset, outset 등으로 모양 지정 가능.
3. 선 색상(border-color) : 색상 이름이나, rgb, rgb 코드등으로 입력 가능.

두께, 선 모양, 색상등을 한번에 지정할 수도 있고 각각 따로 지정할 수도 있다.

ex)

```
border : 5px solid;
border : solid red;
```

app.use(express.static(\_\_dirname + "/static"));

## border-radius

직역하면 경계면의 각도를 의미한다. 보통 직사각형으로 나뉘는 박스들(대표적으로 button)등의 경계면 각도를 둥글게 만들어준다. 값이 커질수록 원형에 가까워짐.

와 같은 형태로 입력하면 된다.

# button

## button - type

button의 type은 크게 3종류로 나뉜다. 종류로는 button / submit / reset이 있다.

> button

button은 말그대로 클릭을 할 수 있는 버튼이 브라우저 창에 생기며, 클릭해도 아무런 기능이 없다. 이와 같은 button은 자바스크립트와 같은 다른 언어의 함수 및 기능을 구현하면, 해당 기능을 실행하기 위한 대상의 역할을 한다.

> submit

submit은 `<input type="submit>`과 동일한 기능을 수행하며, 서버로 데이터를 전달하는 역할을 하는 타입이다. 참고로 아무런 타입 붕여 없이 `"<button>버튼</button>"`과 같이 설정해도 button의 기본 디폴트 값이 submit이다.

> reset

button을 감싸고 있는 form 데이터에 입력된 데이터를 초기화하는 타입이다.

# CSS 카운터

CSS counters를 사용하면 문서에서의 위치에 따라 콘텐츠의 모양을 조정할 수 있다. 예를 들어, counters를 사용해 웹페이지의 제목에 자동으로 번호를 매길 수 있다.

Counters는 요소가 몇 번이나 사용되었는지 추적하여 CSS 규칙에 따라 증가하며, 본질적으로 변수이다.

CSS counter를 사용하려면 먼저 `counter-reset` 속성(초깃값 0)을 사용하여 초기화 해야한다.

초기화 된 counter의 값은 `counter-increment`에 따라 증가하거나 감소한다.

counter의 이름으로 "none", "inherit", "initial"은 사용이 불가능하다. 이런 이름을 사용하면 선언은 무시된다.

## 카운터 표시하기

Counter의 값은 content 속성에서 `counter()`나 `counters()` 함수를 사용하여 표시할 수 있다.

`counter()` 함수는 `'counter(name)'`와 `'counter(name, style)'` 두 가지 형태로 사용할 수 있다. 생성된 텍스트는 가상 요소가 속한 범위에 있는 이름(name)의 가장 안쪽 counter의 값이다. 텍스트는 지정된 서식(기본값은 십진수decimal)으로 뿌려진다.

`counters()` 함수도 `'counters(name, string)'`나 `'counters(name, string, style)'` 두 가지 형태로 사용할 수 있다.

## 예제

> CSS

```css
body {
    counter-reset: section; /* counter 이름을 'section'으로 지정합니다.
                                                   초깃값은 0입니다. */
}

h3::before {
    counter-increment: section; /* section의 카운터 값을 1씩 증가시킵니다. */
    content: "Section " counter(section) ": "; /* section의 카운터 값을 표시합니다. */
}
```

> HTML

```html
<h3>Introduction</h3>
<h3>Body</h3>
<h3>Conclusion</h3>
```

MD문서로는 잘 표현이 안되니까 이건 [MDN 링크](https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Lists_and_Counters/Using_CSS_counters#a_more_sophisticated_example "MDN카운터") 참고하기.

# overflow

CSS의 overflow 프로퍼티는 요소내의 컨텐츠가 너무 커서 요소내에 모두 보여주기 힘들때 그것을 어떻게 보여줄지를 지정한다.

overflow 에 사용할 수 있는 값은 네가지가 있다.

-   visible : 기본 값 넘칠 경우 컨텐츠가 상자 밖으로 보여진다.

-   hidden : 넘치는 부분은 잘려서 보여지지 않는다.

-   scroll : 스크롤바가 추가되어 스크롤할 수 있다.(가로, 세로 모두 추가 가능)

-   auto : 컨텐츠 량에 따라 스크롤바를 추가할지 자동으로 결정된다.( 필요에 따라 가로, 세로 별도로 추가될 수도 있다.)

위의 4가지값과 함께 x축이나 y축에 별도로

-   overflow-x : 값
-   overflow-y : 값

의 형태로 사용도 가능하다.

# :nth-child

:nth-child() 의사 클래스는 형제 사이에서의 순서에 따라 요소를 선택한다.

```css
/* 목록의 두 번째 <li> 선택 */
li:nth-child(2) {
  color: lime;
}

/* 임의의 그룹에서 네 번째에 위치하는 모든 요소 선택 */
:nth-child(4n) {
  color: lime;
}
```

nth-child 의사 클래스는 형제의 목록에서, 선택하려는 요소의 인덱스 패턴을 나타내는 하나의 매개변수를 사용해 지정한다.

인덱스는 1부터 시작한다.

키워드 값에는 

* odd
형제 요소에서 홀수번째(1,3,5, ...)인 요소를 나타낸다.
* even
형제 요소에서 짝수번째(2,4,6, ...)인 요소를 나타낸다.

함수형 표기법도 가능하다.
