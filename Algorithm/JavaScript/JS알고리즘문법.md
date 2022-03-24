# 자바스크립트 활용 코딩테스트 문법 정리

# 백준

# 입,출력

백준의 경우 입력이 미리 주어진다(A = x, B = y 등으로)

때문에 python에서의 input이나 sys.stdin.readline()과 같은 녀석들로 입력값을 받아와야 하는데 입력부분은 우선 다음과 같다.

### 입력

일일히 작성하기 귀찮으므로 템플릿 느낌으로 놔두고 필요할때 복붙사용하기

```js
const fs = require("fs");

//1. 하나의 값을 입력받을 때
const input = require("fs").readFileSync("/dev/stdin").toString().trim();

//1-1. 하나의 값을 입력받고 숫자로 사용
const input = parseInt(
    require("fs").readFileSync("/dev/stdin").toString().trim(),
);

//2. 공백으로 구분된 한 줄의 값들을 입력받을 때
const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(" ");

//3. 여러 줄의 값들을 입력받을 때
const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

//4. 첫 번째 줄에 자연수 n을 입력받고, 그 다음줄에 공백으로 구분된 n개의 값들을 입력받을 때
const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(/\s+/);
const [n, ...arr] = input;

//5. 첫 번째 줄에 자연수 n을 입력받고, 그 다음줄부터 n개의 줄에 걸쳐 한 줄에 하나의 값을 입력받을 때
const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");
const [n, ...arr] = input;
```

### 출력

출력은 간단.

```js
console.log("표현하고싶은 값");
```

---

# 자바스크립트에서 입력 이벤트 중단시키는 방법

코딩테스트를 로컬 Vscode에서 테스트해본 결과 어마어마한 결과가 발생했다.

그냥 무한입력된다..

그냥 1줄요약하자면 테스트 입력이 끝나면 control + D 눌러야 입력하는게 꺼진다. 이것만 기억하면 된다..
