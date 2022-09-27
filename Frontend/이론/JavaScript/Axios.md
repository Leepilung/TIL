# Axios란 ? (작성 중)

추가 작성 진행중 [공식문서 링크](https://yamoo9.github.io/axios/guide/api.html#http-%EB%A9%94%EC%84%9C%EB%93%9C-%EB%B3%84%EC%B9%AD)

> 목표

1. Axios란 무엇인가에 대한 개념적인 이해
2. 설치 방법 및 이해하지 못하고 있는 문법들에 대한 정리

Axios는 브라우저, Node.js를 위한 Rpmise API를 활용하는 HTTP 비동기 통신 라이브러리이다.

## 설치법

npm i axios

## 멀티 요청

```js
function getUserAccount() {
  return axios.get('/user/12345');
}

function getUserPermissions() {
  return axios.get('/user/12345/permissions');
}

axios.all([getUserAccount(), getUserPermissions()])
  .then(axios.spread(function (acct, perms) {
    // Both requests are now complete
  }));
```

여러 개의 요청을 동시에 수행하는 경우 `axios.all()` 메소드를 사용한다.

## API를

구성(configuration) 설정을 `axios()`에 전달하여 요청할 수 있다.

```js
axios(config)
```