# Axios란 ?

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