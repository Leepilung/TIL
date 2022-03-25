# 백준 자바스크립트 에러 정리

# 런타임 에러 (EACCES)

14681 문제를 풀다가 발생

특정 구문이 permisiion denied 발생

구글링해도 파악이 잘 안됐으나 라인 바이 라인으로 테스트한 결과 체크하는데 성공

```js
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
```

여기서 readFileSync의 안에 해당 구문이 문제였음.

```js
const input = fs.readFileSync(0).toString().trim().split("\n");
```

해당 구문 안의 값을 '/dev/stdin'에서 0으로 바꾸니까 바로해결됨.
