# React 이론 정리2

복습용으로 최대한 축약하여 이해하는데 있어 어색함이나 부족함 없게끔 정리하는 것이 목표.

# 컴포넌트 스타일링

리액트에서 컴포넌트를 스타일링 하는 방식은 다양하다. 여러 방식 중 정해진 방식은 딱히 없고 회사마다 요구하는 스팩도 다르고, 취향에 따라 선택하기 때문이다.

방식들은 다음과 같다.

-   일반 CSS: 컴포넌트를 스타일링하는 가장 기본적인 방식이다.

-   Sass: 자주 사용되는 CSS 전처리기(pre-processor) 중 하나로 확장된 CSS 문법을 사용하여 CSS 코드를 더욱 쉽게 작성할 수 있도록 해준다.

-   CSS Module: 스타일을 작성할 때 CSS 클래스가 다른 CSS 클래스의 이름과 절대 충돌하지 않도록 파일마다 고유한 이름을 자동으로 생성해 주는 옵션이다.

-   styled-components: 스타일을 자바스크립트 파일에 내장시키는 방식으로 스타일을 작성함과 동시에 해당 스타일이 적용된 컴포넌트를 만들 수 있게 해준다.

## CSS

프로젝트는 일반 CSS 방식이 기본이다. CSS를 작성할 때 중요한 점은 CSS 클래스를 중복되지 않게 만드는 것이다. CSS 클래스가 중복되는 것을 방지하는 여러 방식이 있는데 이름을 지을 때 특별한 규칙을 사용하는 것이고, 다른 방식은 CSS Selector를 활용하는 것이다.

### 이름 짓는 규칙

프로젝트를 자동 생성하면 나오는 App.css를 보면 이름을 컴포넌트 이름-클래스 형태로 지어진 경우가 많다.(ex : App-header) 이와 같이 클래스 이름에 컴포넌트 이름을 포함시키는 방식으로 중복되는 클래스를 만들어 사용을 방지할 수 있다.

비슷한 방식으로 BEM 네이밍이라는 방식또한 존재한다. CSS 방법론 중 하나로서 이름을 지을 때 일종의 규칙을 준수하여 해당 클래스가 어디에서 어떤 용도로 사용되는지 명확하게 작성하는 방식이다. (ex : .card_title-primary)

### CSS Selector

CSS Selector를 사용하면 CSS 클래스가 특정 클래스 내부에만 있는 경우에만 스타일을 저용할 수 있다. 예로 .App 안에 들어있는 .logo에 스타일을 적용하고 싶다면 다음과 같이 작성하면 된다.

```css
.App .logo {
    animation: App-logo-spin infinite 20s linear;
    height: 40vmin;
}
```

그러나 여전히 종속관계를 표현하는 것이 굉장히 지저분하게 느껴진다. 노멀하지만 간편하지는 않은 방법이라고 생각되는 방식이다.

## Sass 사용하기

Sass(Syntactically Awesome Style Sheets === 문법적으로 매우 멋진 스타일시트)는 CSS 전처리기로 복잡한 작업을 쉽게 할 수 있도록 해 주고, 스타일 코드의 재활용성을 높여 줄 뿐만 아니라 코드의 가독성을 높여 유지 보수를 용이하게 한다.

create-react-app 구버전에서는 Sass를 사용하려면 추가 작업이 필요했는데, v2 버전부터는 별도의 추가 설정 없이 바로 사용할 수 있다.

Sass에서는 두 가지 확장자 .scss와 .sass를 지원한다. Sass가 처음 나왔을 때는 .sass 확장자만 지원되었으나 나중에 개발자들의 요청에 의해 .scss 확장자도 지원하게 되었다고 한다.

.sass와 .scss의 문법은 꽤 다르다.

```scss
/*sass의 경우 */
$font-stack: Helvetica, sans-serif
$primary-color: #333

body
  font: 100% $font-stack
  color: $primary-color

/*scss의 경우 */
$font-stack: Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}
```

.sass 확장자는 중괄호({})와 세미콜론(;)을 사용하지 않는다. 반면 .scss는 기존 CSS를 작성하는 방식과 크게 다르지 않다.

sass를 사용하기 위해선 node-sass라는 라이브러리의 설치가 필요하다. 이 라이브러리는 sass를 css로 변환해준다.

```scss
// 변수 사용하기
$red: #fa5252;
$orange: #fd7e14;
$yellow: #fcc419;
$green: #40c057;
$blue: #339af0;
$indigo: #5c7cfa;
$violet: #7950f2;
// 믹스인 만들기(재사용되는 스타일 블록을 함수처럼 사용할 수 있음)
@mixin square($size) {
    $calculated: 32px * $size;
    width: $calculated;
    height: $calculated;
}

.SassComponent {
    display: flex;
    .box {
        // 일반 CSS에서는 .SassComponent .box와 마찬가지
        background: red;
        cursor: pointer;
        transition: all 0.3s ease-in;
        &.red {
            // .red 클래스가 .box와 함께 사용되었을 때
            background: $red;
            @include square(1);
        }
        &.orange {
            background: $orange;
            @include square(2);
        }
    }
}
```

위의 예시와 같이 변수명을 이용하여 변수를 사용할 수 있고, mixin등을 함수처럼 사용하여 원하는 값을 넣어 유동적으로 사용이 가능하다.

### uitls 함수 분리하기

여러 파일에서 사용될 수 있는 Sass 변수나 믹스인은 다른 파일로 따로 분리하여 작성한 뒤 필요한 곳에서 쉽게 불러와 사용이 가능하다.

```scss
/* uitls.js로 분리시킨 변수명 선언과 믹스인 구문*/
// 변수 사용하기
$red: #fa5252;
$orange: #fd7e14;
$yellow: #fcc419;
$green: #40c057;
$blue: #339af0;
$indigo: #5c7cfa;
$violet: #7950f2;
// 믹스인 만들기(재사용되는 스타일 블록을 함수처럼 사용할 수 있음)
@mixin square($size) {
    $calculated: 32px * $size;
    width: $calculated;
    height: $calculated;
}
```

이를 아까처럼 사용하기 위해 scss파일을 불러올 때에는 `@import` 구문을 사용한다.

```scss
@import './styles/utils';

.SassComponent {
  display: flex;
  .box {
    background: red; // 일반 CSS에서는 .SassComponent .box와 마찬가지
    cursor: pointer;
    transition: all 0.3s ease-in;
    (...)
  }
}
```

### node_modules에서 라이브러리 불러오기

Sass의 장점 중 하나는 라이브러리를 쉽게 불러와서 사용할 수 있다는 점이다.

설치한 라이브러리를 사용하는 가장 기본적인 방법은 상대 경로를 이용하여 node_moduels까지 들어가서 불러오는 방법이다.

그러나 이런 구조는 스타일 파일이 깊숙히 위칳나 경우 ../를 매우 많이 적어야 해 번거로워진다. 때문에 더 쉬운 방법이 `물결 문자(~)`를 사용하는 방법이다.

```scss
@import ‘../../../node_modules/library/styles‘;

위의 구문이 아래와 같이 바뀐다.
@import ‘~library/styles‘;
```

물결 문자를 사용하면 자동으로 node_modules에서 라이브러리 디렉터리를 탐지하여 스타일을 불러올 수 있다.

## CSS Module

CSSModule은 CSS불러와 사용할 때 클래스 이름을 고유한 값인 파일이름*클래스이름*해시값 등의 형태로 자동으로 만들어 클래스 이름의 중첩을 방지한다.

.module.css 확장자로 파일을 저장하기만 하면 CSS Module이 적용된다.

## classnames

classnames는 CSS 클래스를 조건부로 설정할 때 매우 유용한 라이브러리다.

설치는 npm install classnames

대략적인 사용법은 다음과 같다.

```js
import classNames from ‘classnames’;


classNames(‘one’, ‘two’); // = ‘one two‘
classNames(‘one’, { two: true }); // = ‘one two‘
classNames(‘one’, { two: false }); // = ‘one‘
classNames(‘one’, [‘two’, ‘three’]); // = ‘one two three‘



const myClass = ‘hello’;
classNames(‘one’, myClass, { myCondition: true }); // = ‘one hello myCondition‘
```

이런 식으로 여러 종류의 파라미터를 조합하여 CSS 클래스를 설정할 수 있기 때문에 컴포넌트에서 조건부로 클래스를 설정할 때 매우 편리하다.

props에 따른 다른 스타일 지정또한 매우 간단하다.

```js
const MyComponent = ({ highlighted, theme }) => (
    <div className={classNames("MyComponent", { highlighted }, theme)}>
        Hello
    </div>
);
```

위의 예시의 경우 엘리먼트 클래스의 props로 전달받은 highlighted 값이 true면 해당 클래스가 적용되고, false면 적용되지 않는식이다.

추가로 theme으로 전달받는 문자열은 내용 그대로 클래스에 적용된다.

만약 라이브러리르 사용하지 않는다면 다음과 같은 구문으로 사용해야 한다.

```js
const MyComponent = ({ highlighted, theme }) => (
    <div className={`MyComponent ${theme} ${highlighted ? "highlighted" : ""}`}>
        Hello
    </div>
);
```

가독성 측면에서 매우 뒤떨어진다.

## styled-components

컴포넌트 스타일링의 또 다른 방식으로 자바스크립트 파일 안에 스타일을 선언하는 방식이다.

'CSS-in-JS'로도 부르는데 이와 관련된 라이브러리가 굉장히 많은데 가장 선호하는 라이브러리가 styled-components이다.

설치 : npm install styled-components

styled-components를 사용하면 자바스크립트 파일 하나에 스타일까지 작성할 수 있기 때문에 .css 또는 .scss 확장자를 가진 스타일 파일을 따로 만들지 않아도 된다는 장점이 있다.


# React 개발자 도구

리액트 개발자 도구는 브라우저에 나타난 리액트 컴포넌트를 심층 분석할 수 있도록 리액트 개발 팀이 만들었으며, 크롬 웹 스토어에서 React Developer Tools를 검색하여 설치할 수 있다.

