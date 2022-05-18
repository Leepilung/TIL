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

# 입력이 여러개인데 처음에 숫자, 나머지 값을 그 숫자만큼 활용하는 경우

```js
// 백준 :
// 링크 : https://www.acmicpc.net/problem/
// 설명 :

const [N, ...arr] = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

console.log("----------------------");
console.log(N);
console.log(arr);
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

# node.js 디버깅용

```js
// 예제.txt 에 input 내용 입력후 저장
let input = require("fs")
    .readFileSync(__dirname + "/예제.txt")
    .toString()
    .split("\n");

const [n, ...arr] = input;
```
