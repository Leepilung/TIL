# Sass(Scss) 문법 정리

# 🏷 주석(Comment)

CSS에서 주석은 `/* .... */` 이다.

Sass(Scss)는 JS처럼 두 가지 스타일의 주석을 사용한다.

```scss
// 컴파일되지 않는 주석
/* 컴파일되는 주석 */
/*
컴파일되는
여러 줄
주석
*/
```

# 🏷 데이터 종류(Data Types)

|  데이터  |                 설명                  |                   예시                   |
| :------: | :-----------------------------------: | :--------------------------------------: |
| Numbers  |                 숫자                  |            1, .82, 20px, 2em…            |
| Strings  |                 문자                  | bold, relative, "/images/a.png", "dotum" |
|  Colors  |               색상 표현               |   red, blue, #FFFF00, rgba(255,0,0,.5)   |
| Booleans |                 논리                  |               true, false                |
|  Nulls   |             아무것도 없음             |                   null                   |
|  Lists   |     공백이나 ,로 구분된 값의 목록     |  (apple, orange, banana), apple orange   |
|   Maps   | Lists와 유사하나 값이 Key: Value 형태 |     (apple: a, orange: o, banana: b)     |

## 🚩 특이사항

sass(scss)에서 사용하는 데이터 종류들에는 몇 가지 특이사항이 있다.

-   Numbers: 숫자에 단위가 있거나 없다.
-   Strings: 문자에 따옴표가 있거나 없다.
-   Nulls: 속성값으로 null이 사용되면 컴파일하지 않는다.
-   Lists: ()를 붙이거나 붙이지 않는다.
-   Maps: ()를 꼭 붙여야 한다.

# 🏷 중첩(Nesting)

Sass는 중첩 기능을 사용할 수 있다.

상위 선택자의 반복을 피하고 좀 더 편리하게 복잡한 구조를 작성할 수 있는 장점이 있다.

> 📝 예제

```scss
// scss에서의 문법
.section {
    width: 100%;
    .list {
        padding: 20px;
        li {
            float: left;
        }
    }
}
```

위의 문법이 컴파일되면 다음과 같은 css로 처리된다.

```css
/* css에서 처리되는 결과 */
.section {
    width: 100%;
}
.section .list {
    padding: 20px;
}
.section .list li {
    float: left;
}
```

# 🏷 Ampersand (상위 선택자 참조)

중첩 안에서 `&` 키워드는 상위(부모) 선택자를 참조하여 치환한다.

> 📝 예제

```scss
// scss에서의 문법
.btn {
    position: absolute;
    &.active {
        color: red;
    }
}

.list {
    li {
        &:last-child {
            margin-right: 0;
        }
    }
}
```

위의 문법이 컴파일되면 다음과 같은 css로 처리된다.

```css
/* css에서 처리되는 결과 */
.section {
    width: 100%;
}
.section .list {
    padding: 20px;
}
.section .list li {
    float: left;
}
```

`&` 키워드가 참조한 상위 선택자로 치환되는 것이기 때문에 다음과 같이 응용할 수도 있다.

```scss
// scss에서의 문법
.fs {
    &-small {
        font-size: 12px;
    }
    &-medium {
        font-size: 14px;
    }
    &-large {
        font-size: 16px;
    }
}
```

위의 문법이 컴파일되면 다음과 같은 css로 처리된다.

```css
/* css에서 처리되는 결과 */
.fs-small {
    font-size: 12px;
}
.fs-medium {
    font-size: 14px;
}
.fs-large {
    font-size: 16px;
}
```
