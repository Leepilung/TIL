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
    .split(" ")
    .map(Number);

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

//6. 첫 번째 줄에 자연수 n개 입력받고, 그 다음줄에 여러개의 값을 받을 때
const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(/\s+/)
    .map(Number); // map함수로 숫자형 변환

const [A, B, ...arr] = input; // 비구조화 할당으로 선언하는 만큼 첫재쭐의 변수 사용 가능

// 7. 첫 번째 줄에 자연수 n을 입력받고, 그 다음줄에 여러개의 값을 입력 받을 때

// 입력 예시
5
1 1
2 3
3 4
9 8
5 2

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

// 출력 예시
[ '5', '1 1', '2 3', '3 4', '9 8', '5 2' ]
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

# 자바스크립트 negative index (ex list[-1])

빌어먹을 자바스크립트는 Negative index를 지원하지 않는다고 한다.. 어쩐지 undefined만 출력됨..

고로 index를 이용하여 배열의 마지막 인덱스에 접근하기 위한 방법은 다음과 같은 방법 뿐이다

```js
const number = [1, 2, 3, 4, 5];
console.log(number[number.length - 1]);
```

# 자바스크립트 배열에서 최대값, 최소값 가져오는 방법

Math모듈 사용해야함.

```js
const number = [1, 2, 3, 4, 5];

// 최댓값
console.log(Math.max(...number));
// 최솟값
console.log(Math.min(...number));

// 주의점 -> 배열에서 스프레드 연산자 안쓰면 인식안함.
```

# 배열안에서 특정값이 있는지 아닌지 찾는 방법

레퍼런스 : https://hianna.tistory.com/403

배열안에서 파이썬에서 흔히사용하는 in은 똑같이 작동한다.

그러나 not in의 경우 not in으로 사용하면 아예 동작하지 않았음. 다르게 사용해야함

```js
const number = [1, 2, 3, 4, 5];

// 1이 있는지 아닌지 찾고싶다면
if (number.indexOf(1) === -1) {
    console.log("1이 없는 것");
}
```

indexOf() 메소드나, lastIndexOf() 메소드는 찾으려는 값이 배열안에 없으면 -1을 반환하는 함수다.

-   lastIndexOf()함수

이녀석은 찾으려는 값과 정확하게 일치(===)하는 '마지막' element의 index를 리턴한다.

좀더 깔끔한 함수는 includes()함수인 듯?

## includes()

```js
arr.includes(valueToFind[,fromIndex])
```

includes()함수는 배열이 특정 값을 포함하고 있는지의 여부를 boolean 값으로 반환한다.

-   파라미터

    -   `valueToFind` : 찾으려는 값을 의미
    -   `fromIndex`: 검색을 시작할 index를 의미, 기본값은 0, 음수가 입력될 경우 arr.length + fromIndex로 계산한다.

-   리턴값

    배열이 valueToFind의 값을 포함하고 있는지의 여부인 true, false 두개의 boolean 값 중 하나를 반환한다.

```js
// include 함수 사용 예시

const number = [1, 2, 3, 4, 5];

number.includes(1); // ture
number.includes(3); // ture
number.includes(1, 3); // ture
number.includes(6); // false
```

# 두 개의 배열 비교하여 중복 제거하는 방법

```js
a = [1, 2, 3, 4, 5];

b = [1, 3, 5];

c = a.filter((x) => !b.includes(x));
// [ 2, 4 ] 출력
console.log(c);
```

# 알파벳 소문자, 대문자로 이 뤄진 배열 만드는 방법

```js
// 대문자의 경우
const arr = Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 65));
console.log(arr);

// 소문자의 경우
const arr = Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 97));
console.log(arr);
```

# 빈 배열 만들기

```js
const tmp = Array.from({length : 원하는 길이(숫자값)})
```

위와 같이 원하는 길이를 Number값으로 저장하고 출력하며 원하는 길이의 빈배열 탄생

# 문자열 반전

내장 함수인 split(), reverse(), join()을 사용하ㅐ면 간단하게 문자열의 반전이 가능하다.

```js
function reverse_string(s) {
    return s.split("").reverse().join("");
}

var example = revers("love");
console.log(example); // -> "evol" 출력됨
```
