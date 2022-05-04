# 입력이 여러개인 경우

```js
// 백준 :
// 링크 : https://www.acmicpc.net/problem/
// 설명 :

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

console.log(input);
```

---

# 입력이 하나의 숫자인 경우

```js
// 백준 :
// 링크 : https://www.acmicpc.net/problem/
// 설명 :

const input = Number(require("fs").readFileSync("/dev/stdin"));

console.log(input);
```
