## TIL (MD편)

> 마크다운(Syntax) 문법에 대해 정리해봅니다.

# 제목(Header)

> h1부터 h6까지 제목을 표현할 수 있습니다.

```md
# 제목 1

## 제목 2

## 제목 3

#### 제목 4

##### 제목 5

###### 제목 6

<h1>제목 1</h1>
<h2>제목 2</h2>
<h6>제목 6</h6>

# 가장 큰 제목

## 그다음 큰 제목
```

# 강조(Emphasis)

> 각각에 맞는 태그로 형태가 변환되어 입력됩니다.

```md
기본

<u>밑줄 표시</u>

<em> 기울기 </em>

<strong> 강조2 </strong>

<del> 취소선 </del>

~~취소선2~~

_이텔릭1_ _이텔릭2_

**두껍게2** **두껍게2**
```

# 목록

> ol ul 명령어에 따라 목록 태그로 변환 됩니다.

```md
순서가 없는 목록1 - ul

<ul>
    <li>목록1</li>
    <li>목록2</li>
    <li>목록3</li>
</ul>
순서가 없는 목록2 - ul
<ul>
    <li><p>목록1</p></li>
    <li><p>목록2</p></li>
    <li><p>목록3</p></li>
</ul>
순서가 있는 목록1 - ol
<ol>
    <li>목록1</li>
    <li>목록2</li>
    <li>목록3</li>
</ol>
순서가 있는 목록2 -ol, -ul
<ol>
    <li>첫번째</li>
    <li>두번째</li>
<ul>
    <li>2-1 목록</li>
    <li>2-2 목록</li>
    <li>2-3 목록</li>
</ul>
<li>세번째</li>
</ol>
```

# 인용(Blockqoutes)

> 인용은 이메일에서 처럼 >문자를 앞에 사용하는 방식이다.

<blockquote>
    <p>인용의 예입니다</p>
    <p>인용 안에서도 문단을 나누는게 가능합니다</p>
    <h3> 제목등의 다른 문법도 사용 가능합니다. </h3>
    <blockquote>
        <p> 인용안의 인용도 가능합니다.</p>
    </blockquote>
</blockquote>

```md
<blockquote>
    <p>인용의 예입니다</p>
    <p>인용 안에서도 문단을 나누는게 가능합니다</p>
    <h3> 제목등의 다른 문법도 사용 가능합니다. </h3>
    <blockquote>
        <p> 인용안의 인용도 가능합니다.</p>
    </blockquote>
</blockquote>
```

# 링크(Link)

> 링크를 거는 방법은 총 2가지이다. 여기서 title 명령어는 각주의 명명에 사용된다.

<p>예시1) 마크다운에 관한 자세한 내용은 <a href="http://daringfireball.net/projects/markdown/">여기</a>를 참고하여라.
<a href="http://en.wikipedia.org/wiki/markdown" title="wikipedia">여기</a>에도 잘 정리가 되어있다.</p>

```md
<p>예시1) 마크다운에 관한 자세한 내용은 <a href="http://daringfireball.net/projects/markdown/">여기</a>를 참고하여라.
<a href="http://en.wikipedia.org/wiki/markdown" title="wikipedia">여기</a>에도 잘 정리가 되어있다.</p>
```

<p>예시2) 마크다운에 관한 자세한 내용은 <a href="http://daringfireball.net/projects/markdown/" title="daring Fireball">여기</a>를 참고하여라. <a href="http://en.wikipedia.org/wiki/markdown" title="wikipedia:">여기</a>에도 잘 정리가 되어있다.</p>

```md
<p>예시2) 마크다운에 관한 자세한 내용은 <a href="http://daringfireball.net/projects/markdown/" title="daring Fireball">여기</a>를 참고하여라. <a href="http://en.wikipedia.org/wiki/markdown" title="wikipedia:">여기</a>에도 잘 정리가 되어있다.</p>
```

<p>예시3) 링크: <a href="http://google.com/">http://google.com</a>, 이메일: <a href="mailto:ek3434@naver.com">이필웅</a></p>

```md
<p>예시3) 링크: <a href="http://google.com/">http://google.com</a>, 이메일: <a href="mailto:ek3434@naver.com">이필웅</a></p>
```

# 이미지 (Images)

> 이미지 삽입은 링크와 메우 흡사하다. 다만 문자 앞에 !문자만 붙여주면 된다.

<p><img src="https://raw.github.com/dcurtis/markdown-mark/master/png/208x128.png" alt="마크다운 로고"></p>

```md
<p><img src="https://raw.github.com/dcurtis/markdown-mark/master/png/208x128.png" alt="마크다운 로고"></p>
```
