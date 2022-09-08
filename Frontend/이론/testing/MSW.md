# MSW란?

현재 내용 업데이트 중

[참조 링크](https://fe-developers.kakaoent.com/2022/220825-msw-integration-testing/)

> 목표

1. MSW란 무엇인지?
2. MSW의 도입 방법
3. MSW를 통한 테스트 방법은 어떻게 이뤄지는지에 대한 숙지 

## 개요

오늘날 프론트엔드에도 굉장히 많은 테스트 도구들이 등장하였다. Jest, Cypress.. 이외에 효율적으로 통합 테스트나 e2e 테스트(End to End 테스트 : 개발물을 사용자 관점에서 테스트 하는 방법)를 작성할 수 있게 되었다.

그러나 프론트엔드에서 코드 테스트를 작성하다 보면 더미 데이터를 만들어야 하거나 많은 API를 모킹해가며 테스트를 진행해야 함에는 변함이 없다.

이러한 문제를 해결하기 위해 나온 것이 `MSW(Mock Service Worker)`이다.

`MSW`는 API 요청을 가로채서 사전에 설정해둔 목업 데이터를 넘겨주도록 설정해 주는 도구이다.

서버 개발자와 협의가 이뤄진 API 스펙만 있다면 미리 목업 데이터를 만들어, 실제 데이터를 호출하듯이 테스트를 해볼 수 있게 되는 것이다.

## MSW 설치 및 통합 테스트 기본 세팅 방법

1. [install](https://mswjs.io/docs/getting-started/install) : MSW설치
2. [Define mocks(Mocking REST API)](https://mswjs.io/docs/getting-started/mocks/rest-api) : API 모킹 핸들러 설정
3. [Integrate(Node)](https://mswjs.io/docs/getting-started/integrate/node) : 노드 환경(jest)에서 사용 가능하도록 설정