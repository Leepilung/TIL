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

```js
// filter까지 활용한 사용 예시
a = [1, 2, 3, 4, 5];

b = [1, 3, 5];

c = a.filter((x) => !b.includes(x));
// [ 2, 4 ] 출력
console.log(c);
```

# 📚 배열 검색 메소드들

find, findIndex, indexOf 등의 문법이 있다.

자바스크립트 Array.prototype에 속해있고 배열에서 원하는 값 또는 식별자를 찾아내는 메소드들.

배열을 순차적으로 반복한다.

## 📕 find

find는 인자로 받은 판별 함수를 만족하는 첫 번째 요소를 반환한다.

```js
// 기본 형태
arr.find(callback);

callback(element, index, array); // -> 콜백 함수가 받는 인자들
```

반환 타입은 찾은 요소의 타입을 갖는다. 없다면 undefined 반환

원하는 요소를 찾을 때 까지 반복한다. 찾는다면 메소드를 바로 죵로함.

-   📝 EX

```js
const arr = [5, 6, 9, 1, 6, 3, 2, 1, 2, 7, 9, 4, 3];

const find1 = arr.find((element, index, array) => {
    // 인덱스 2인 요소를 찾을 때 까지 반복
    console.log('콜백함수를 실행한 배열은? ', array);
    return index == 2;
});
const find2 = arr.find((element, index, arr) => element === 3);
const find3 = arr.find((e) => e > 8);
const find4 = arr.find((e) => e > 10);

console.log('find1:', find1);
console.log('find2:', find2);
console.log('find3:', find3);
console.log('find4:', find4);

// 실행 결과

// find1안의 console.log 출력문( index == 2 일때 까지 반복)
콜백함수를 실행한 배열은?  [5, 6, 9, 1, 6, 3, 2, 1, 2, 7, 9, 4, 3]
콜백함수를 실행한 배열은?  [5, 6, 9, 1, 6, 3, 2, 1, 2, 7, 9, 4, 3]
콜백함수를 실행한 배열은?  [5, 6, 9, 1, 6, 3, 2, 1, 2, 7, 9, 4, 3]

find1: 9
find2: 3
find3: 9
find4: undefined
```

## 📗 findIndex

findIndex는 판별 함수를 만족하는 첫 식별자를 반환한다.

기본적으로 index를 반환하므로 반환 타입은 number이고 값이 없다면 -1을 반환한다.

```js
// 기본 형태
arr.findIndex(callback);

callback(element, index, array); // -> 콜백 함수가 받는 인자들(각 인자는 findIndex 메소드를 호출한 배열에서 받아온다)
```

원하는 요소를 찾자마자 메소드를 종료한다.

-   📝 EX

```js
const arr = [5, 6, 9, 1, 6, 3, 2, 1, 2, 7, 9, 4, 3];

const find1 = arr.findIndex((element, index, array) => {
    return index < 7 && index > 5;
});
const find2 = arr.findIndex((element, index, arr) => element === 3);
const find3 = arr.findIndex((e) => e > 8);
const find4 = arr.findIndex((e) => e > 10);

console.log("findIndex1:", find1);
console.log("findIndex2:", find2);
console.log("findIndex3:", find3);
console.log("findIndex4:", find4);

// 실행 결과
findIndex1: 6;
findIndex2: 5;
findIndex3: 2;
findIndex4: -1;
```

## 📘 indexOf

인자로 받은 값을 찾아 맞는 식별자를 반환한다.

```js
// 기본 형태
arr.indexOf(search, fromIndex);

// search 매개변수는 배열에서 찾을 요소를 의미한다.
```

findIndex와 마찬가지로 index값을 반환받으므로 반환 타입 기본값은 number, 없을 경우 -1

-   📝 EX

```js
// 일반적인 사용 예
const arr = [5, 6, 9, 1, 6, 3, 2, 1, 2, 7, 9, 4, 3];
const find1 = arr.indexOf(1);
const find2 = arr.indexOf(2);
const find3 = arr.indexOf(3);
const find4 = arr.indexOf(4);

console.log("findIndex1:", find1);
console.log("findIndex2:", find2);
console.log("findIndex3:", find3);
console.log("findIndex4:", find4);

// 실행 결과
findIndex1: 3;
findIndex2: 6;
findIndex3: 5;
findIndex4: 11;

// 하나의 배열에서 찾으려는 값을 모두 찾으려는 경우

const arr = [5, 6, 9, 1, 6, 3, 2, 1, 2, 7, 9, 4, 3];
const search = 9; // 찾으려는 값
const searchResult = []; // 찾은 값을 보관할 배열
let index = arr.indexOf(search);
while (index != -1) {
    searchResult.push(index);
    index = arr.indexOf(search, index + 1);
}
console.log(searchResult);
// 실행 결과
[2, 10];
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

# 입력한 단일 문자열 for문으로 바로 순회하는 문법

Python에서 문자열 인덱스 슬라이싱으로 알아서 나눠서 출력하는 문법.

```js
const text = require("fs").readFileSync("/dev/stdin").toString().trim();

for (let i of text) {
    console.log(i); // Python에서 문자열을 for문에 넣었을떄와 동일하게 출력
}
```

# 딕셔너리

기본적인 구조는 기존에 공부한 것과 동일

선언도 동일.

```js
// 딕셔너리 기초 문법

// 선언
var dict = {};

// 삽입(추가))
dict["banana"] = "바나나";
dict["orange"] = "오렌지";
console.log(dict); // Object {banana : '바나나', orange : '오렌지' } 출력됨.

// 제거
delete dict["orange"]; // 삭제 (제대로 삭제 되면 true, 안되면 false 출력)
```

## 딕셔너리활용 문법

### 딕셔너리 키, 벨류 출력

딕셔너리의 키값과 벨류값 출력 하는 방법

```js
for (var key in dictObject) {
    console.log("key : " + key + ", value : " + dictObject[key]);
}
```

기존 파이썬 문법과 동일하다.

### 모든 key값 가져오는 방법

```js
Object.keys(dict); // ['banana', 'orange']
```

### 딕셔너리의 길이 구하는 방법

```js
Object.keys(dict).length; // 2 출력
```

### key값이 존해자는지 체크하는 방법

기존의 in 문법이 통용되는 것 같다. value로 배열을 갖는 경우에는 전혀 다른 얘기.

```js
"banana" in dict; // true
"kiwi" in dict; // false
```

### key의 마지막 값 가져오는 방법

```js
// key의 마지막 값 가져오는 방법
var lastKey = Object.keys(dict)[Object.keys(dict).length - 1];
console.log("last key = " + lastKey); // 'orange'
```

# 문자열로 이뤄진 배열 안에서 특정 문자열 포함되있는지 확인하는 방법

includes 하나만 쓰면 동작을 안하는데 이상하게 findIndex와 묶으니까 동작한다.. 해당 문법들에 대한 이해가 좀 더 필요한듯

```js
// input
const text = require("fs").readFileSync("/dev/stdin").toString().trim();

var comb = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"];

for (let i of text) {
    console.log(i); // text의 문자열을 인덱스 슬라이싱하여 하나씩 출력
    console.log(comb.findIndex((v) => v.includes(i))); // 슬라이싱 된 문자열 한개가 포함되있는 element의 인덱스 반환
}
```

# 📚 문자열 변환

JS로 문자열을 바꾸는 방법은 replace, replace에 정규표현식을 이용한 방법, replaceAll()등의 메소드가 존재한다.

## 📕 replace()

replace() 메소드는 어떤 패턴에 일치하는 일부 혹은 모든 부분이 교체된 새로운 문자열을 반환한다.

패턴에는 특정 문자열이나 정규식(RegExp)등이 가능하다.

패턴이 문자열인 경우, 첫 번째 문자열만 치환되며 원래 문자열은 변경되지 않는다(새로운 문자열을 반환한다는 것)

```js
const text = "the black wall is very big and tall";

text.replace("black", "white"); // black -> white로 변경
// 실행 결과
("the white wall is very big and tall");
```
