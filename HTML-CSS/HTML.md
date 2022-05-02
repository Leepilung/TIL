# HTML

<style>
    .li {
        background-color : gray;
        padding : 0.5rem;
    }
</style>

HTML은 웹 페이지를 만드는데 사용하는 `마크업 언어`이다.

HyperText Markup Language의 약자이고 웹 페이지는 HTML 문서라고도 불리며, HTMl 태그들로 구성된다.

각각의 HTML 태그는 웹 페이지의 디자인이나 기능을 결정하는데 사용된다.

## \* HTML 태그(tag)

HTML 태그는 태그 이름을 꺾쇠 괄호(<>)로 감싸 표현한다.

```
<태그이름>  // 시작 태그
 내용
</태그이름> // 종료 태그
```

태그에 따라 시작 태그만 있고 종료 태그가 없는 태그도 존재한다.

그 종류로는 `<img> <br> <hr>` 등과 같이 종료 태그 없이 시작 태그만을 가지는 태그를 `빈 태그(empty tag)` 라고도 부른다.

## \* W3C

W3C는 World Wide Web Consortium의 약자이다.

W3C가 관리하는 대표적 웹표준들은 다음과 같다.

1. HTML
2. CSS
3. DOM
4. SVG
5. XHTML
6. XML

## \* HTML 기본 구조

<img src =  http://tcpschool.com/lectures/img_html_basic_structure.png>

`<!DOCTYPE html>` : 현재 문서가 HTML5 문서임을 명시하는 부분이다.

`<html>` : HTML 문서의 루트(root) 요소를 정의한다.

`<head>` : HTML 문서의 메타데이터(metadata)를 정의한다.

-   메타데이터(metadata)란 ? : HTML 문서에 대한 정보(data)로 웹 브라우저에는 직접적으로 표현되지 않는 정보를 의미한다.

-   이러한 메타데이터는` <title>, <style>, <meta>, <link>, <script>, <base>`태그 등을 이용하여 표현할 수 있다.

`<title>` : HTML 문서의 제목(title)을 정의하며, 다음과 같은 용도로 사용된다.

-   웹 브라우저의 툴바(toolbar)에 표시된다.
-   웹 브라우저의 즐겨찾기(favorites)에 추가할 때 즐겨찾기의 제목이 된다.
-   검색 엔진의 결과 페이지에 제목으로 표시된다.

`<body>`: 웹 브라우저를 통해 보이는 내용(content) 부분이다.

`<h1>` ~ `<h6>` : 제목(heading)을 나타낸다.

`<p>` : 단락(paragraph)을 나타낸다.

## \* HTML 요소 구조

<img src = http://tcpschool.com/lectures/img_html_tag_structure.png>

HTML 요소는 여러 속성을 갖는다. 또한 HTML 요소는 시작 태그로 시작해서 종료 태그로 끝난다.

속성은 HTML 요소 중에서도 언제나 시작 태그 내에서만 정의되며, 속성이름과 속성값으로 표현된다.

> 속성 이름은 언제나 소문자로 작성하자

HTML5 표준에서 속성 이름에 대소문자를 구분하지는 않는다. 그러나 W3C에서는 속성이름을 사용할 때 될 수 있으면 소문자로 작성하도록 권장하고 있다.

> 속성값은 언제나 따옴표로 감싸자

HTML5 표준에서 속성값에 따옴표 사용을 강제하지 않는다.
그러나 속성값을 따옴표로 감싸지 않으면 예상치 못한 오류등이 발생한다.

## EX )

> 예제
> <img src="quotes.jpg" alt="이미지가 없어요">

<img src="quotes.jpg" alt=이미지가 없어요>

---

이와 같이 속성값에 띄어쓰기가 들어가는 경우 따옴표를 사용해야 정확한 값을 저장할 수 있다.

속성값을 감쌀 때는 보통 큰 따옴표("")가 사용되며, 작은따옴표('')도 사용할 수 있다.

# HTML 텍스트 요소

## \* 제목(Heading)

HTML은 제목을 표현할 수 있는 다양한 크기의 <h> 태그를 제공한다.

## EX )

> 예제

<h1>제목1의 크기입니다!</h1>
<h2>제목2의 크기입니다!</h2>
<h3>제목3의 크기입니다!</h3>
<h4>제목4의 크기입니다!</h4>
<h5>제목5의 크기입니다!</h5>
<h6>제목6의 크기입니다!</h6>

---

`<h>` 태그의 위 아래로 약간의 여백이 자동으로 삽입된다.

이런 `<h>`태그는 제목의 표현이라는 기능 뿐 아니라 여러 검색엔진에서 이 `<h>` 태그를 이용하여 키워드를 수집하고, 파악한다.

## \* 단락(Paragraph)

단락이란 내용상 끊어서 구분할 수 있는 하나하나의 부분을 의미하며, 문단이라고 부른다.

## EX )

> 예제

<h1>제목1의 크기입니다!</h1>
<h2>제목2의 크기입니다!</h2>
<h3>제목3의 크기입니다!</h3>
<p>여기서부터 단락입니다.</p>

`<p>` 태그의 위아래로는 약간의 여백(margin)이 자동으로 삽입된다.

---

### \* 띄어쓰기와 줄 나누기

HTML 코드에서 띄어쓰기나 줄 나누기를 여러 번 하더라도 오직 하나의 띄어쓰기나 줄로만 인식한다.

---

## EX )

> 예제

<p>
줄을 나누고 싶어서
이렇게 줄을 나눠봤습니다.

과연 그대로 출력이 되는가?

</p>

---

`<br>` 태그(break line)을 사용하면 새로운 단락을 만들지 않고도 줄을 나눌 수 있다.

`<br>` 태그는 위에서도 언급했듯이 종료 태그가 없는 빈 태그이다.

---

## EX )

> 예제

<p>
줄을 나누고 싶어서<br>
이렇게 줄을 나눠봤습니다.<br>
<br>
과연     그대로     출력이     될까요?
</p>

---

## \* 텍스트 서식 미리 정의하기

HTML 코드에서 작성한 텍스트 서식을 그대로 표현하려면 `<pre>`태그글 사용한다.

`<pre>`태그는 태그 내에 작성된 텍스트의 모든 띄어쓰기, 줄나누기등을 웹 브라우저에 그대로 표현한다.

---

## EX )

> 예제

<pre>
줄을 나누고 싶어서
이렇게 줄을 나눠봤습니다.

과연     그대로     출력이     될까요?
</pre>

---

## \* 수평 가로 구분선

단락을 나눌 때나, 내용상의 구분을 표현하고자 할 때 수평 가로 구분선을 사용한다.

수평 가로 구분선은 HTML 코드에서 `<hr>` 태그로 간단하게 만든다.

---

## EX )

> 예제

<p>저는 하나의 단락입니다.</p>
<hr>
<p>저는 하나의 단락입니다.</p>
<hr>
<p>저는 하나의 단락입니다.</p>

---

# \* 서식(Formatting)

HTML 문서에서 텍스틀 굵게 표현하고 싶을 때에는 `<b>`태그(bold text)나 `<strong>` 태그를 사용하면 된다.

---

## EX )

> 예제

`<p><b>"이 부분"</b>은 단순히 글씨가 굵은 부분이에요!</p>`

 <p><b>"이 부분"</b>은 단순히 글씨가 굵은 부분이에요!</p>

`<p><strong>"이 부분"</strong>은 중요한 부분이라서 굵게 표현됐어요!</p>`

<p><strong>"이 부분"</strong>은 중요한 부분이라서 굵게 표현됐어요!</p>

---

`<b>`태그는 단순히 화면의 텍스트를 굵게 표현해 준다

하지만 `<strong>`태그는 텍스트를 굵게 표현해줄 뿐만 아니라 그 내용이 중요하다는 의미도 함께 포함해 준다.

HTML 문서에서 이탤릭체를 표현하고 싶을 때에는 `<i>`태그(italic text)나` <em>`태그(emphasized text)를 사용한다.

---

## EX )

> 예제

`<p><i>"이 부분"</i>은 단순히 글씨가 이탤릭체인 부분이에요!</p>`

<p><i>"이 부분"</i>은 단순히 글씨가 이탤릭체인 부분이에요!</p>

`<p><em>"이 부분"</em>은 중요한 부분이라서 이탤릭체로 표현됐어요!</p>`

<p><em>"이 부분"</em>은 중요한 부분이라서 이탤릭체로 표현됐어요!</p>

---

## \* 하이라이팅 효과

`<mark>` 태그는 텍스트에 하이라이팅 효과를 적용시킨다.

---

## EX )

> 예제
>
> `<p><mark>"이 부분"</mark>만 하이라이팅하고 싶어요.</p>`

<p><mark>"이 부분"</mark>만 하이라이팅하고 싶어요.</p>

---

## \* 삭제 효과

`<del>`태그(delete)는 텍스트 중앙에 가로줄을 만들어 마치 텍스트를 지운 것과 같은 효과를 준다.

---

## EX )

> 예제

`<p><del>"이 부분"</del>을 지운 것처럼 하고 싶어요.</p>`

<p><del>"이 부분"</del>을 지운 것처럼 하고 싶어요.</p>

---

## \* 삽입 효과

`<ins>`태그(insert)는 텍스트 밑에 가로줄을 만들어 마치 빈칸에 텍스트를 삽입한 것과 같은 효과를 내줍니다.

---

ex)

`<p><ins>"밑줄 친 부분"</ins>에 들어갈 알맞은 말을 고르세요.</p>`

<p><ins>"밑줄 친 부분"</ins>에 들어갈 알맞은 말을 고르세요.</p>

---

## \* 위첨자와 아래첨자 효과

위첨자는 `<sup>`태그(superscript)를 사용하여, 아래첨자는 `<sub>`태그(subscript)를 사용하여 각각 표현할 수 있습니다.

---

ex)

`<p>X<sup>2</sup> + Y<sup>3</sup> = Z</p>`

<p>X<sup>2</sup> + Y<sup>3</sup> = Z</p>

`<p>물을 나타내는 화학식은 H<sub>2</sub>O 입니다.</p>`

<p>물을 나타내는 화학식은 H<sub>2</sub>O 입니다.</p>

---

## \* 인용구(Quotation)

HTML에서 인용구를 표현하는 방법은 다음과 같이 두 가지로 나뉜다.

1. 짧은 인용구
2. 블록 인용구

## \* 짧은 인용구

짧은 인용구는 `<q>`태그(quotation)을 사용하여 표현할 수 있다. 자동으로 앞 뒤에 큰 따옴표가 붙는다.

---

## EX)

> 예제

<p>HTML의 정의는

<q>웹 페이지를 만들기 위한 하이퍼텍스트 마크업 언어</q>

입니다.</p>

---

## `\*` 블록 인용구

길이가 긴 인용문은 `<blockqoute>` 태그를 사용하여 표현할 수 있다.

---

## EX )

> 예제

<p>HTML의 정의</p>

<blockquote>

인터넷 서비스의 하나인 월드 와이드 웹을 통해 볼 수 있는 문서를 만들 때 사용하는 프로그래밍 언어의 한 종류이다.

</blockquote>

-> `<blockquote>`
`인터넷 서비스의 하나인 월드 와이드 웹을 통해 볼 수 있는 문서를 만들 때 사용하는 프로그래밍 언어의 한 종류이다`.
`</blockquote>`

---

## \* 축약형 표현

HTML에서 용어의 축약형을 표현하기 위해서는 `<abbr>`태그(abbreviation)를 사용한다.

`<abbr>`태그 위에 마우스를 위치시키면 title 속성에 명시한 용어의 원형이 나타낸다.

---

## EX)

> 예제

`<p><strong><abbr title="HyperText Markup Language 5">HTML5</abbr></strong> 란 웹 문서를 제작하는 데 쓰이는 프로그래밍 언어인 HTML의 최신규격입니다.</p> `

<p><strong><abbr title="HyperText Markup Language 5">HTML5</abbr></strong>
란 웹 문서를 제작하는 데 쓰이는 프로그래밍 언어인 HTML의 최신규격입니다.</p>

---

HTML5위에 마우스를 갖다대보면 title로 입력한 설명이 축약되어 나타난다.

## \* 주소 표현

`<address>`태그를 사용하면 HTML에서 주소를 표현할 수 있다.

이러한 주소는 이탤릭체로 표현되며, 위아래로 약간의 공백이 자동으로 삽입된다.

---

## EX)

> 예제

<address>
    서울특별시<br>
    강남구 테헤란로
</address>

---

# 주석(Comment)

주석이란 개발자가 작성한 해당 코드에 대한 이해를 돕는 설명이나 디버깅을 위해 작성한 구문을 의미한다.

이러한 주석은 다른 HTML 코드와 달리 웹 브라우저에 의해 표현되지 않는다.

문법은 `<!-- 주석 내용 -->`이 형태와 같다.

시작 태그에는 (`<!--`) 느낌표(!)가 있지만 종료 태그(-->)에는 느낌표가 없다.

이러한 주석은 HTML 코드의 어느 부분에서라도 사용할 수 있다.

---

## EX )

> 예제

<!-- 작성자 : 홍길동 -->

<p>이 부분은 조금 어려운 코드입니다.</p>

<!--
    위와 같이 어려운 코드의 이해를 돕기 위해서 적어놓은 설명입니다.
-->

---

주석은 웹페이지에선 표현되지 않는다.

실제로 주석으로
` <!--`
`위와 같이 어려운 코드의 이해를 돕기 위해서 적어놓은 설명입니다.`
`-->`
와 같이 표시되어있지만 MD에서는 표시되지 않는다.

중첩 주석은 사용할 수 없다.

# 문자셋(Character set)

웹 브라우저가 HTML 문서를 정확하게 나타내기 위해서는 해당 문서가 어떠한 문자셋으로 저장되었는지를 알아야한다.

따라서 HTML 문서가 저장될 때 사용된 문자셋에 대한 정보를 `<head>`태그 내의 `<meta>`태그에 명시한다.

HTML5에서 UTF-8의 경우 : `<meta charset="UTF-8">`와 같이 표기하고 있다.

-   UTF-8 : 자주 정리 했듯이 세상에 있는 거의 모든 문자를 표현할 수 있는 유니코드 문자를 지원하는 HTML5의 기본 문자셋이다.

# HTML 스타일

HTML 요소의 style 속성(attribute)을 이용하면 CSS 스타일을 HTML 요소에 직접 설정할 수 있다.

하지만 이러한 style 속성을 이용한 방법은 오직 단 하나의 HTML 요소에만 스타일을 적용할 수 있다.

> 기본 문법

<태그이름 style="속성이름:속성값">

의 형태를 취한다.

## 배경색 변경

style 속성을 이용해 배경색을 변경하는 예제를 알아보자.

<h1 style="background-color:white">

    style 속성을 이용한 배경색 변경

</h1>

위의 형식은 다음과 같은 형식으로 사용해야 나타나는 결과물이다.

`<h1 style="background-color:white">`

    style 속성을 이용한 배경색 변경

`</h1>`

---

## 글자색 변경

<h1 style="color:red">

    style 속성을 이용한 글자색 변경

</h1>

위의 형식은 다음과 같은 형식으로 사용해야 나타나는 결과물이다.

`<h1 style="color:red">`

    style 속성을 이용한 글자색 변경

`</h1>`

---

## 글자 크기 변경

<h1 style="font-size:250%">

    style 속성을 이용한 글자 크기 변경

</h1>

위의 형식은 다음과 같은 형식으로 사용해야 나타나는 결과물이다.

`<h1 style="font-size:250%">`

    style 속성을 이용한 글자 크기 변경

`</h1>`

---

## 문단 정렬 변경

<h3 style="text-align:center">

    style 속성을 이용한 문단 정렬 변경

</h3>

위의 형식은 다음과 같은 형식으로 사용해야 나타나는 결과물이다.

`<h3 style="text-align:center">`

    style 속성을 이용한 문단 정렬 변경

`</h3>`

---

## 여러 스타일의 설정

style 속성을 이용하여 여러 CSS 스타일을 한 번에 적용할 수 있다.

<h1 style="background-color:white; color:maroon; font-size:150%; text-align:center">

    style 속성을 이용하여 한 번에 스타일링 하기!

</h1>

위의 형식은 다음과 같은 형식으로 사용해야 나타나는 결과물이다.

`<h1 style="background-color:white; color:maroon; font-size:150%; text-align:center">`

    style 속성을 이용하여 한 번에 스타일링 하기!

`</h1>`

> 기억해야할 포인트

-   style 속성값에 사용되는 CSS 속성(property)과 속성값들은 세미콜론(;)을 이용하여 구분한다.

-   CSS 속성을 하나만 사용할 때나, 여러 개의 CSS 속성 중 맨 마지막 CSS 속성은 세미콜론(;)을 생략할 수 있다.

# HTML 색

HTML 색(COLOR)표현은 세 가지 방법이 있다.

1. 색상 이름으로 표현

ex) <h4 style="color:rgb(0,0,255)">RGB 색상값으로 표현된 파란색</h4>

`<h4 style="color:rgb(0,0,255)">`RGB 색상값으로 표현된 파란색`</h4>`

2. RGB 색상값으로 표현

ex) <h4 style="color:#0000FF">16진수 색상값으로 표현된 파란색</h4>

`<h4 style="color:#0000FF">`16진수 색상값으로 표현된 파란색`</h4>`

3. 16진수 색상값으로 표현

16진수 색상값은 RGB 색상값을 각각 16진수로 변환한 것이다.

따라서 각각의 기본색(Red, Green, Blue)은 각각 00부터 FF까지의 범위를 가진다.

ex) <h4 style="color:#0000FF">16진수 색상값으로 표현된 파란색</h4>

`<h4 style="color:#0000FF">`16진수 색상값으로 표현된 파란색`</h4>`

> 기억해야할 포인트

-   HTML에서 색상 이름은 대소문자를 구분하지 않는다.

# HTML 배경

HTML 문서의 기본 배경(background)은 흰색이다.

또한, HTML 요소들도 각자 자신만의 배경을 가지고 있다.

HTML에서는 이러한 배경을 다음과 같이 변경할 수 있다.

1. 배경을 다른 색으로 변경

2. 배경을 다른 이미지로 변경

> 배경을 다른 색으로 변경

HTML5 이전까지는 bgcolor 속성을 이용하여 HTML 요소의 배경색을 다른 색으로 변경할 수 있었다.

하지만 HTML5부터는 bgcolor 속성을 더 이상 지원하지 않으며, CSS를 이용하여 배경색을 변경하도록 하고 있다.

## EX )

> 예제

```html
<style>
    body {
        background-color: lightblue;
    }

    h1 {
        background-color: rgb(255, 128, 0);
    }

    p {
        background-color: #ffffcc;
    }</style
>123
```

이걸 실제로 적용시키면 제법 끔찍한 모양으로 MD문서 전체의 배경색이 바뀌게 된다..

> 배경을 다른 이미지로 변경

background 속성을 이용하면 HTML 요소의 배경을 이미지(image)로 설정할 수 있다.

> 문법

```html
<태그이름 background="이미지주소">
```

## EX )

> 예제

```html
<body background="../img/관계형데이터베이스1.jpg"></body>
```

위의 예제에서 사용한 코드도 실제로 적용하면 img 폴더에 넣어둔 관계형데이터베이스1.jpg가 배경화면으로 도배된다.. (테스트해봤으니 하지말자)

그리고 배경으로 이미지를 사용하면 웹 페이지의 로딩시간이 증가하게 된다.

따라서 보통은 작은 사이즈의 이미지를 패턴(pattern)으로 만들어 배경 이미지로 반복 설정하여 사용한다.

# HTML 링크

HTML 링크(Link)

오늘날 웹 페이지에는 다른 페이지나 다른 사이트로 연결되는 수많은 하이퍼 링크(Hyperlink)가 존재한다.

여기서 Hyper란 컴퓨터 용어로서 텍스트 등의 정보가 동일 선상에 있는 것이 아닌 다중으로 연결되어 있는 상태를 의미한다.

한 텍스트에서 다른 텍스트로 건너뛰어 읽을 수 있는 기능을 하이퍼 링크(Hyper link) 혹은 간단히 링크(link)라고도 부르며, HTML에선 `<a>`태그로 표현한다.

### href 어트리뷰트

href 어트리뷰트는 이동하고자 하는 파일의 위치(경로)를 값으로 받는다. 경로(path)란 파일 시스템 상에서 특정 파일의 위치를 의미한다.

`<a>`태그의 href 속성은 링크를 클릭하면 연결할 페이지나 사이트의 URL 주소를 명시한다.

`<a>`태그는 텍스트나 단락, 이미지 등 다양한 HTML 요소에 사용할 수 있다.

href 어트리뷰트에는 다음의 값들을 사용할 수 있다.

-   절대 url ( 웹사이트 URL (href="http://www.naver.com/))
-   상대 url ( 자신의 위치를 기준으로한 대상의 URL (href="html/default.html"))
-   fragment identifier ( 페이지 내의 특정 id를 갖는 요소를 링크 (href="#top"))
-   메일 ( amilto : ~~~ )
-   script ( href="javascript:alert('Hello')" )

> 문법

```html
<a href="링크주소">HTML 링크</a>
<!-- 혹은 위의 어트리튜브 예시들 -->
<a href="html/my.html">Local file</a><br />
<a href="file/my.pdf" download>Download file</a><br />
<a href="#">fragment identifier</a><br />
<a href="mailto:someone@example.com?Subject=Hello again">Send Mail</a><br />
<a href="javascript:alert('Hello');">Javascript</a>
```

## EX )

> 📝 예제

```html
<a href="/html/intro">
    <h2>이 링크를 클릭해 보세요!</h2>
</a>
```

예제) 실 사용 시
<a href="/html/intro">

<h2>이 링크를 클릭해 보세요!</h2>
</a>

---

# target 속성

`<a>`태그의 target 속성은 링크로 연결된 문서를 어디에서 열지를 명시한다.

| target 속성값 |                               설명                               |
| :-----------: | :--------------------------------------------------------------: |
|    \_blank    |          링크로 연결된 문서를 새 창이나 새 탭에서 오픈.          |
|    \_self     |   링크로 연결된 문서를 현재 프레임(frame)에서 오픈. (기본설정)   |
|   \_parent    |        링크로 연결된 문서를 부모 프레임(frame)에서 오픈.         |
|     \_top     | 링크로 연결된 문서를 현재 창의 가장 상위 프레임(frame)에서 오픈. |
| 프레임(frame) |     이름 링크로 연결된 문서를 지정된 프레임(frame)에서 오픈.     |

## EX )

> 예제

```html
<h2><a href="/html/intro" target="_blank">blank</a></h2>

<h2><a href="/html/intro" target="_self">self</a></h2>

<h2><a href="/html/intro" target="_parent">parent</a></h2>

<h2><a href="/html/intro" target="_top">top</a></h2>

<h2><a href="/html/intro" target="myframe">myframe</a></h2>

<iframe name="myframe" style="width:50%; height: 330px"></iframe>
```

[실습링크](http://tcpschool.com/examples/tryit/tryhtml.php?filename=html_basic_links_02)

복습시 이 링크파트 실습은 꼭 링크를 타고 들어가서 직접 확인해볼 것.

`target="_blank"`를 사용하여 외부 페이지를 오픈하는 경우, 이동한 외부 페이지에서 자바스크립트 코드를 사용해 악의적인 페이지로 리다이렉트 할 수 있는 보안 취약점(Tabnabbing 피싱 공격)이 있다.

이를 방지하기 위해 rel="noopener noreferrer"를 추가하면 이를 방지할 수 있다고 한다.

-   [Tabnabbing 피싱 공격의 동작 원리와 대응책](https://tech.lezhin.com/2017/06/12/tabnabbing)
-   [Tabnabbing 공격과 rel=noopener 속성](https://blog.coderifleman.com/2017/05/30/tabnabbing_attack_and_noopener/)
-   [tabnabbing 공격 방어 대책 정리](https://medium.com/@youngminhong/tabnabbing-%EA%B3%B5%EA%B2%A9-%EB%B0%A9%EC%96%B4-%EB%8C%80%EC%B1%85-%EC%A0%95%EB%A6%AC-9276ebf63f94)

# 링크의 상태(state)

| 링크의 상태 |                     설명                      |
| :---------: | :-------------------------------------------: |
|    link     | 아직 한 번도 방문한 적이 없는 상태 (기본설정) |
|   visited   |       한 번이라도 방문한 적이 있는 상태       |
|    hover    |       링크 위에 마우스를 올려놓은 상태        |
|   active    |       링크를 마우스로 누르고 있는 상태        |

웹 브라우저에서 링크가 연결되어 있는 텍스트의 색상은 다음과 같다.

-   기본적으로 링크가 걸린 텍스트는 밑줄에, 텍스트 색상이 파란색으로 변경된다.

-   visited 상태의 링크는 밑줄에, 텍스트 색상이 보라색으로 변경된다.

-   active 상태의 링크는 밑줄에, 텍스트 색상이 빨간색으로 변경된다.

[실습 링크](http://tcpschool.com/examples/tryit/tryhtml.php?filename=html_basic_links_03)

-   이 파트도 복습할때 싱습 링크를 이용하자

# 페이지 책갈피

`<a>`태그의 name 속성을 이용하면 간단한 책갈피를 만들 수 있다.

우선 책갈피를 통해 가고 싶은 위치에 `<a>`태그를 만들고 name 속성을 작성한다.

그다음에 작성한 name 속성값을 이용하여 다른 `<a>`태그에서 링크를 걸면된다.

## EX )

> a태그 예제

```html
<a href="#bookmark"><p>제목 3으로 가는 링크</p></a>
...
<h2><a name="bookmark"></a>제목 3</h2>
```

# HTML 이미지

오늘날 웹 페이지에는 이러한 이미지가 매우 중요한 요소의 하나로 자리 잡고 있다.

웹 페이지에서 주로 사용되는 이미지의 종류는 다음과 같다.

|                                  JPEG 이미지                                   |                                        GIF 이미지                                         |                                   PNG 이미지                                   |
| :----------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------: |
| <img src="http://tcpschool.com/lectures/jpg_ex_img.jpg" alt="대충 jpg 이미지"> | <img src="http://tcpschool.com/lectures/gif_ex_img.gif" alt="대충 gif (움직이는) 이미지"> | <img src="http://tcpschool.com/lectures/png_ex_img.png" alt="대충 png 이미지"> |

# 이미지의 삽입

HTML 문서에 이미지를 삽입할 때는 `<img>`태그를 사용한다.

`<img>`태그는 종료 태그가 없는 빈 태그(empty tag)이며, 다음과 같은 문법으로 사용된다.

> 문법

```html
<img src="이미지주소" alt="대체문자열" />
```

src 속성은 이미지가 저장된 주소의 URL 주소를 명시한다.

alt 속성으로 이미지가 로딩될 수 없는 상황에서 이미지 대신 나타날 문자열을 설정할 수 있다.

## EX )

> alt 속성 예제

<img src="/img_html5_logo.png" alt="이미지가 없음...ㅠ">

```html
예제 코드 <img src="/img_html5_logo.png" alt="이미지가 없나봐요.." />
```

# 이미지의 크기(width, height) 설정

HTML에서는 style 속성을 사용하여 이미지의 크기를 설정할 수 있다.

또한, width 속성과 height 속성을 이용하면, 이미지의 너비와 높이를 각각 픽셀(pixel) 단위로 설정할 수도 있다.

CSS를 이용한 내부 스타일 시트나 외부 스타일 시트와 상관없이 이미지의 원래 크기를 유지하려면 style 속성을 사용하는 것이 좋다.

## EX )

> 이미지 설정 예제

<style>
    img {
        width:100%;
        border: 1px solid black;
    }
</style>

<img src="http://tcpschool.com/examples/images/img_flag.png" alt="html size" width="320" height="214">

<img src="http://tcpschool.com/examples/images/img_flag.png" alt="style size" style="width:320px; height:214px">

# 이미지의 테두리(border) 설정

border 속성을 사용하여 이미지의 테두리 사용 여부와 굵기를 설정할 수 있다.

> 이미지 테두리 예제

<img src="http://tcpschool.com/examples/images/img_flag.png" alt="이미지 테두리" style="width:320px; height:214px; border: 15px solid black">

# 이미지에 링크(link) 설정

이미지에 `<a>`태그를 이용하여 링크를 설정할 수 있다.

누르면 네이버로 연결된다.

> 이미지 링크 예제

<a href="http://www.naver.com" target="_blank">
<img src="http://tcpschool.com/examples/images/img_flag.png" alt="flag" style="width:320px; height:214px">
</a>

# 이미지 맵 만들기

이미지 맵(image map)이란 이미지의 일부를 클릭할 수 있도록 만들어서 버튼처럼 사용하는 기능을 의미한다.

HTML에서는 `<map>`태그를 이용하여 이미지 맵(image map)을 제작할 수 있다.

`<img>`태그의 usemap 속성을 `<map>`태그의 name 속성과 연결하면 이미지와 맵사이의 관계가 설정된다.

`<map>`태그는 하나 이상의 `<area>`태그를 가지며, 이 `<area>`태그가 바로 버튼과 같은 역할을 한다.

EX )

> 이미지맵 예제

<img src="http://tcpschool.com/examples/images/img_imagemap.jpg" alt="진실혹은거짓" usemap="#vending" style="width:320px; height:240px" />

<map name="vending">

<area shape="rect" coords="90,60,180,130" alt="거짓" href="https://ko.wikipedia.org/wiki/%EA%B1%B0%EC%A7%93%EB%A7%90">

<area shape="rect" coords="210,200,70,130" alt="진실" href="https://ko.wikipedia.org/wiki/%EC%A7%84%EC%8B%A4">

</map>

```html
<!-- 예제 코드 -->
<img
    src="http://tcpschool.com/examples/images/img_imagemap.jpg"
    alt="진실혹은거짓"
    usemap="#vending"
    style="width:320px; height:240px"
/>
<!-- usemap 으로 map name인 #vending과 연결 -->

<map name="vending">
    <area
        shape="rect"
        coords="90,60,180,130"
        alt="거짓"
        href="https://ko.wikipedia.org/wiki/%EA%B1%B0%EC%A7%93%EB%A7%90"
    />

    <area
        shape="rect"
        coords="210,200,70,130"
        alt="진실"
        href="https://ko.wikipedia.org/wiki/%EC%A7%84%EC%8B%A4"
    />
</map>
```

# HTML 리스트

리스트(list)란 여러 요소들을 일렬로 나열한 목록이나 명단을 의미한다.

HTML에서는 이러한 리스트를 표현하기 위해 다음과 같은 리스트를 제공한다.

1. 순서가 없는 리스트(unordered list)
2. 순서가 있는 리스트(ordered list)
3. 정의 리스트(definition list)

# 순서가 없는 리스트(Unordered List)

순서가 없는 리스트는 `<ul>`태그로 시작하며, 여기에 포함되는 각각의 리스트 요소는 `<li>`태그로 시작한다.

각각의 리스트 요소 앞에는 기본 마커(marker)로 검정색의 작은 원(bullet)이 위치한다.

## EX )

> 예제

<ul>
    <li>사과</li>
    <li>멜론</li>
    <li>바나나</li>
</ul>

CSS의 list-style-type 속성을 사용하면 리스트 요소 앞에 위치하는 마커(marker)를 다른 모양으로 변경할 수 있다.

-   disc : 검정색 작은 원 모양 (기본설정)
-   circle : 흰색 작은 원 모양
-   square : 사각형 모양

## EX )

> Circle 예제

<ul style="list-style-type: circle">
    <li>수박</li>
    <li>참외</li>
    <li>옥수수</li>
</ul>

> square 예제

<ul style="list-style-type: square">
    <li>수박</li>
    <li>참외</li>
    <li>옥수수</li>
</ul>

# 순서가 있는 리스트(Ordered List)

순서가 있는 리스트는 `<ol>`태그로 시작하며, 여기에 포함되는 각각의 리스트 요소는 `<li>`태그로 시작한다.

각각의 리스트 요소 앞에는 기본 마커로 아라비아 숫자가 위치한다.

## EX )

> 예제

<ol>
    <li>사과</li>
    <li>멜론</li>
    <li>바나나</li>
</ol>

순서가 없는 리스트와 마찬가지로 CSS의 `list-style-type` 속성을 사용하면 리스트 요소 앞에 위치하는 `마커(marker)`를 다른 모양으로 변경할 수 있다.

-   decimal("1") : 숫자 (기본설정)
-   upper-alpha("A") : 영문 대문자
-   lower-alpha("a") : 영문 소문자
-   upper-roman("I") : 로마 숫자 대문자
-   lower-roman("i") : 로마 숫자 소문자

## 📝 EX )

> 영문 대문자

<ol style="list-style-type: upper-alpha">
    <li>수박</li>
    <li>참외</li>
    <li>옥수수</li>
</ol>

> 영문 소문자

<ol style="list-style-type: lower-alpha">
    <li>수박</li>
    <li>참외</li>
    <li>옥수수</li>
</ol>

> 로마 대문자

<ol style="list-style-type: upper-roman">
    <li>수박</li>
    <li>참외</li>
    <li>옥수수</li>
</ol>

> 로마 소문자

<ol style="list-style-type: lower-roman">
    <li>수박</li>
    <li>참외</li>
    <li>옥수수</li>
</ol>

`start` 어트리뷰트로 리스트의 시작값을 지정할 수 도 있다.

<ol start="3">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>

reversed 어트리뷰트를 지정하면 리스트의 순서(mark)값을 반대로 표현한다.

<ol reversed>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ol>

# 정의 리스트(description list)

정의 리스트(description list)는 용어와 그에 대한 정의를 모아놓은 리스트로 `<dl>`태그로 시작한다.

`<dt>`태그에는 용어의 이름이 들어가고, `<dd>`태그에는 해당 용어에 대한 정의가 들어간다.

EX )

> 예제

<dl>
    <dt>호박</dt>
    <dd>- 박과의 한해살이 덩굴성 채소</dd>
    <dt>상추</dt>
    <dd>- 국화과의 한해살이 또는 두해살이풀</dd>
</dl>

# HTML 테이블

테이블(Table)이란 여러 종류의 데이터(data)를 보기 좋게 정리하여 보여주는 표를 의미한다.

HTML에서는 `<table>`태그를 사용하여 이러한 테이블을 작성할 수 있다.

`<table>`태그는 다음과 같은 태그들로 구성된다.

1. `<tr>`태그는 테이블에서 열을 구분해 준다.
2. `<th>`태그는각 열의 제목을 나타내며, 모든 내용은 자동으로 굵은 글씨에 가운데 정렬이 된다.
3. `<td>`태그는 테이블의 열을 각각의 셀(cell)로 나누어 준다.

## EX )

<table style="width:100%">
    <tr style="background-color:black">
        <th>참치</th>
        <th>고래</th>      
    </tr>
    <tr>
        <td>상어</td>
        <td>문어</td>
    </tr>
    <tr>
        <td>오징어</td>
        <td>고등어</td>
    </tr>
</table>

[실습링크](http://tcpschool.com/examples/tryit/tryhtml.php?filename=html_01)

CSS의 border 속성을 이용하여 테이블에 테두리를 표현할 수 있다.

border 속성값을 따로 명시하지 않으면, 해당 테이블은 언제나 빈 테두리를 가지게 된다.

```html
<style>
    table,
    th,
    td {
        border: 1px solid black;
    }
</style>
```

[실습링크](http://tcpschool.com/examples/tryit/tryhtml.php?filename=html_03)

실습링크에서 확인하면 테두리가 두 줄로 표현되는데 이를 한줄로 설정하려면 border-collapse 속성을 사용해야 한다.

border-collapse 속성값을 collapse로 설정하면, 테이블의 테두리를 한 줄로 표현할 수 있다.

```html
<style>
    table,
    th,
    td {
        border: 1px solid black;
        border-collapse: collapse;
    }
</style>
```

[실습링크](http://tcpschool.com/examples/tryit/tryhtml.php?filename=html_04)

# 테이블의 열 합치기

colspan 속성을 사용하면 테이블의 열(column)을 합칠 수 있다.

## EX )

```html
<table style="width:100%">
    <tr>
        <td>참치</td
        <td colspan="2">고래</td>
    </tr>
    <tr>
        <td>상어</td>
        <td>문어</td>
        <td>꽁치</td>
    </tr>
</table>
```

[실습링크](http://tcpschool.com/examples/tryit/tryhtml.php?filename=html_05)

# 테이블의 행 합치기

rowspan 속성을 사용하면 테이블의 행(row)을 합칠 수 있다.

## EX )

<table style="width:100%">
    <tr>
        <td rowspan="2">상어</td>
        <td>문어</td>        
        <td>꽁치</td>
    </tr>
    <tr>
        <td>고등어</td>        
        <td>돌고래</td>
    </tr>
</table>

```html
<!-- 코드 -->
<table style="width:100%">
    <tr>
        <td rowspan="2">상어</td>
        <td>문어</td>
        <td>꽁치</td>
    </tr>
    <tr>
        <td>고등어</td>
        <td>돌고래</td>
    </tr>
</table>
```

# 테이블의 열과 행 합치기

colspan 속성과 rowspan 속성을 함께 사용하면, 더욱 복잡한 테이블도 표현할 수 있다.

## EX )

<table style="width:100%">
    <tr>
        <td colspan="6">1</td>
    </tr>
    <tr>
        <td colspan="6">2</td>
    </tr>
    <tr>
        <td rowspan="3">3</td>
        <td rowspan="3">4</td>
        <td colspan="2">5</td>
        <td>6</td>
        <td>7</td>
    </tr>
    <tr>
        <td colspan="3">8</td>
        <td>9</td>
    </tr>
    <tr>
        <td colspan="4">10</td>
    </tr>
</table>

# 테이블의 캡션(caption) 설정

`<caption>`태그를 사용하면 테이블 상단에 제목이나 짧은 설명을 붙일 수 있다.

## EX )

<table style="width:100%">
    <caption>해양 생물</caption>
    <tr>
        <td>참치</td>
        <td>고래</td>
        <td>날치</td>    
    </tr>
</table>

# HTML 요소의 타입

HTML의 모든 요소는 해당 요소가 웹 브라우저에 어떻게 보이는가를 결정짓는 display 속성을 가진다.

대부분의 HTML 요소는 이러한 display 속성값으로 다음 두 가지 값 중 하나를 가지게 된다.

1. 블록(block)
2. 인라인(inline)

# 블록(block) 타입의 요소

display 속성값이 블록(block)인 요소는 언제나 새로운 라인(line)에서 시작하며, 해당 라인의 모든 너비를 차지한다.

## EX )

<p style="border: 3px solid red">
    p요소는 display 속성값이 블록인 요소입니다.
</p>

> 포인트

`<p>`, `<div>`, `<h>`, `<ul>`, `<ol>`, `<form>`요소는 display 속성값이 블록(block)인 대표적인 요소이다.

# `<div>`요소

`<div>`요소는 다른 HTML 요소들을 하나로 묶는 데 자주 사용되는 대표적인 블록(block) 요소이다.

`<div>`요소는 주로 여러 요소들의 스타일을 한 번에 적용하기 위해 사용된다.

## EX )

<div style="background-color:lightgrey; color:green; text-align:center">
    <h1>div요소를 이용한 스타일 적용</h1>
    <p>이렇게 div요소로 여러 요소들을 묶은 다음에 style 속성과 클래스 등을 이용하여
    한 번에 스타일을 적용할 수 있다.</p>
</div>

# 인라인(inline) 타입의 요소

display 속성값이 인라인(inline)인 요소는 새로운 라인(line)에서 시작하지 않는다.

또한, 요소의 너비도 해당 라인 전체가 아닌 해당 HTML 요소의 내용(content)만큼만 차지한다.

`<span>`, `<a>`, `<img>`요소는 display 속성값이 인라인(inline)인 대표적인 요소들이다.

## `<span>`요소

`<span>`요소는 텍스트(text)의 특정 부분을 묶는 데 자주 사용되는 인라인(inline) 요소이다.

## EX )

<p>
    <span style="background-color:grey; color:orange">span태그</span>는 display 속성값이 인라인인 요소입니다.
</p>

# audio

audio 태그는 HTML5에서 새롭게 추가된 태그이며 IE8 이하에서는 사용이 불가능하다.

> atrribute

-   src : 음악 파일 경로
-   preload : 재생 전에 음악 파일을 모두 불러올 것인지 지정
-   autoplay : 음악 파일을 자동 재생 개시할 것인지 지정
-   loop : 음악을 반복할 것인지 지정
-   controls : 음악 재생 도구를 표시할 것인지 지정. 재생 도구의 외관은 브라우저마다 차이가 존재한다.

## 📝 EX )

<html>
  <body>
    <audio controls></audio>
  </body>
</html>

재생 형식또한 브라우저마다 차이가 존재한다.
