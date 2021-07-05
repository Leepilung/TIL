# HTML , CSS 요소 정리

# CSS란?

CSS는 Cascading Style Sheets의 약자로

HTML,XHTML,XML 같은 문서의 스타일을 꾸밀 때 사용하는 스타일 시트 언어이다.

> `<input>` 요소

<input> 의 형태와 같이 입력창이 나타나는 요소.
html에서 input type으로 입력 타입(type)을 설정할 수 있다.

종류는 수없이 많은데

- `<input type="button"> ` = <input type="button">
- `<input type="checkbox">` = <input type="checkbox">
- `<input type="color">` = <input type="color">
- `<input type="date">` = <input type="date">
- `<input type="datetime-local">` = <input type="datetime-local">
- `<input type="email">` = <input type="email">
- `<input type="file">` = <input type="file">
- `<input type="hidden">` = <input type="hidden">
- `<input type="image">` = <input type="image">
- `<input type="month">` = <input type="month">
- `<input type="number">` = <input type="number">
- `<input type="password">` = <input type="password">
- `<input type="radio">` = <input type="radio">
- `<input type="range">` = <input type="range">
- `<input type="reset">` = <input type="reset">
- `<input type="search">` = <input type="search">
- `<input type="submit">` = <input type="submit">
- `<input type="tel">` = <input type="tel">
- `<input type="text">` = <input type="text">
- `<input type="time">` = <input type="time">
- `<input type="url">` = <input type="url">
- `<input type="week">` = <input type="week">

등이 있다.

## Input Type: text

<input type="text"> 텍스트 입력(text input)위 한 줄의 입력 필드를 정의한다.

## Input Type: password

<input type="password"> 는 password 필드를 정의한다.

password 필드의 문자는 별표나 동그라 미로 표시로 가려진다.

## Input Type: date

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

와 같은 형태로 입력하면 된다.