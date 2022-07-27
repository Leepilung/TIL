# 🏷 SVG 컬러 변경 하는 방법

기본적으로 SVG 파일은 fill과 stroke가 분리되어있는데 대부분의 아이콘 SVG 파일의 경우 fill만 바꾸면 색상이 변경이 된다.

그 과정에서 fill을 바꾸는 방법이 여러가지 존재한다.

## 🔖 코드를 통한 색상 변경이 없는 경우

한번만 사용하고 이후에 색상 변경이 없는 경우에 사용하기 좋은 방법. 뭣보다 background태그로 줘도 이미지 색상자체가 변경된 것이기 때문에 mask 방식으로 적용이 안되는 경우 유용한 것 같다(추가 공부 필요)

SVG 파일을 텍스트 편집기로 열어 style태그를 통해 직접 색상 변화 클래스를 추가하는 방법이 있다.

```cs
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
<!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
<path d="M224 256c70.7 0 128-57.31 128-128s-57.3-128-128-128C153.3 0 96 57.31 96 128S153.3 256 224 256zM274.7 304H173.3C77.61 304 0 381.6 0 477.3c0 19.14 15.52 34.67 34.66 34.67h378.7C432.5 512 448 496.5 448 477.3C448 381.6 370.4 304 274.7 304z"/></svg>
```

fontawesome의 SVG 파일이다.

위와 같은 형태안에 style태그를 통해 클래스를 하나 추가하는 방식이다.

```cs
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
<!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. -->
<style>
  .gray{
    fill: gray; 
    // 원하는 색상을 기입하면 된다.
  }
</style>
// 이후에 아래 path 태그 안에 class 추가하는 방식
<path class="gray" d="M224 256c70.7 0 128-57.31 128-128s-57.3-128-128-128C153.3 0 96 57.31 96 128S153.3 256 224 256zM274.7 304H173.3C77.61 304 0 381.6 0 477.3c0 19.14 15.52 34.67 34.66 34.67h378.7C432.5 512 448 496.5 448 477.3C448 381.6 370.4 304 274.7 304z"/></svg>
```

## 🔖 css를 통해 색상을 변경하는 방법

클릭 이벤트등으로 입력된 svg 아이콘의 색상이 변경되는 경우가 굉장히 많다. 이 경우에 사용할 수 있는 방법이다.


```css
.icon {
  mask-image: url('@/assets/svg/ic_calendar-black.svg');
  mask-repeat: no-repeat;
  background-color: var(--color-white);
}
```

위와 같이 background를 활용하지 않고 mask-image 태그를 통해 부여하고 background-color를 조정하는 방식을 사용하면 이미지가 변경한다.
