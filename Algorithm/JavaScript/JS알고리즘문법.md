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

-   📝 EX )

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

## 다른 방법(forEach() 메소드)

forEach() 메소드를 활용하면 주어진 함수를 배열 요소 각각에 대해 실행한다.

다만 여기서 문자열은 함수자체가 동작하지 않는다.

-   🏷 구문

```js

```

-   📝 EX )

```js
const array1 = ["a", "b", "c"];

array1.forEach((element) => console.log(element));

// expected output: "a"
// expected output: "b"
// expected output: "c"

const string1 = "abc";

string1.forEach((e) => console.log(e));
// VM198:1 Uncaught TypeError: a.forEach is not a function 에러 발생
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

# Math.floor() vs parseInt() 차이점

<img src="https://velog.velcdn.com/images%2Fmnmm%2Fpost%2Ff506ad75-2f37-4df0-8b67-34db2c3b4b6e%2Fimage.png">

Math.floor의 경우 내림처리 하는 함수.
parseInt의 경우 문자열 인자를 파싱하여 진수에 해당하는 정수를 반환한다.(값없으면 10진수가 기본)
두 메서드는 양수일 경우 내림한 결과가 나온다.

```js
a = Math.floor("12.34"); // 12
b = Math.floor("56.78"); // 56

a2 = parseInt("12.34"); // 12
b2 = parseInt("56.78"); // 56
```

하지만 음수일 경우 차이가 있다.

```js
c = Math.floor("-12.34"); // -13
d = Math.floor("-56.78"); // -57

c2 = parseInt("-12.34"); // -12
d2 = parseInt("-56.78"); // -56
```

콘솔창에 보여지는 것과 같이 Math.floor 메서드는 소수 첫째 자리에서 양수일 때처럼 내림하는 반면, parseInt 메서드는 버림처리한다.

# 📚 반올림(round), 올림(ceil), 내림(floor) 함수

## 📕 올림(Math.ceil())함수

입력받은 숫자보다 크거나 같은 `정수 중 가장 작은 정수`를 리턴한다.

즉, 입력받은 숫자를 올림한 정수를 리턴하는 함수이다.

> 📝 EX

```js
// 1.올림
const ceil_1 = Math.ceil(1); // 1
const ceil_2 = Math.ceil(1.222); // 2
const ceil_3 = Math.ceil(1.5); // 2
const ceil_4 = Math.ceil(1.777); // 2

// 2. null 또는 0인 경우
const ceil_5 = Math.ceil(null); // 0
const ceil_6 = Math.ceil(0); // 0

// 3. 음수인 경우
const ceil_7 = Math.ceil(-1); // -1
const ceil_8 = Math.ceil(-1.111); // -1
const ceil_9 = Math.ceil(-1.5); // -1
const ceil_10 = Math.ceil(-1.777); // -1
```

```js
// 자릿수 지정(소수점 이하 or 10, 100단위)

// 1.소수점이하
const ceil_1 = Math.ceil(1.222 * 10) / 10; // 1.3
const ceil_2 = Math.ceil(1.222 * 100) / 100; // 1.23

// 2. 10단위, 100단위
const ceil_3 = Math.ceil(1222 / 10) * 10; // 1230
const ceil_4 = Math.ceil(1222 / 100) * 100; // 1300
```

Math.ceil함수가 실행되면 안에 들어간 값을 올림처리하고 뒤의 나눗셈 연산으로 해당값까지 표기하는 방식이라고 생각됨.

## 📗 내림(Math.floor()) 함수

숫자를 내림 처리할 때는 주로 Math.floor() 함수를 사용한다.

위에 parseInt와 비교하면서 올려놨다.

ceil과 반대로 입력받은 숫자보다 작거나 같은 `정수 중 가장 큰 정수`를 리턴한다.

즉, 입력받은 숫자를 내림한 정수를 리턴하는 함수이다.

> 📝 EX

```js
// 1.내림
const floor_1 = Math.floor(1); // 1
const floor_2 = Math.floor(1.222); // 1
const floor_3 = Math.floor(1.5); // 1
const floor_4 = Math.floor(1.777); // 1

// 2. null 또는 0인 경우
const floor_7 = Math.floor(-1); // -1
const floor_8 = Math.floor(-1.111); // -2
const floor_9 = Math.floor(-1.5); // -2
const floor_10 = Math.floor(-1.777); // -2
```

자릿수 지정의 경우 `ceil()`과 방법 동일함.

## 📘 반올림 (Math.round()) 함수

소수점이 0.5보다 `크면`, 입력받은 수보다 다음으로 높은 절대값을 가지는 정수를 리턴,

소수점이 0.5보다 `작으면`, 입력받은 수보다 절대값이 더 낮은 정수를 리턴,

소수점이 0.5와 같으면, 입력받은 수보다 큰 다음 정수를 리턴한다.

```js
// 1.반올림
const round_1 = Math.round(1); // 1
const round_2 = Math.round(1.222); // 1
const round_3 = Math.round(1.5); // 2
const round_4 = Math.round(1.777); // 2

// 2. null 또는 0인 경우
const round_5 = Math.round(null); // 0
const round_6 = Math.round(0); // 0

// 3. 음수인 경우
const round_7 = Math.round(-1); // -1
const round_8 = Math.round(-1.111); // -1
const round_9 = Math.round(-1.5); // -1
const round_10 = Math.round(-1.777); // -2
```

# 🏷 shift() 메소드

shift() 메소드는 배열에서 첫 번째 요소를 제거하고, 제거된 요소를 반환하는 메소드이다.

이 메소드는 원본 배열의 길이를 변하게 한다.

```js
const array1 = [1, 2, 3];

const firstElement = array1.shift();

console.log(array1);
// expected output: Array [2, 3]

console.log(firstElement);
// expected output: 1
```

# 📚 문자열 자르기 (인덱스 슬라이싱)

문자열을 잘라 리턴하는 메소드는 총 3가지

숫자의 경우 String변환해서 자르고 다시 형변환 하는 방식으로 사용해야 할 듯?

1. slice()
2. substring()
3. substr()

## 📕 slice ()

```js
// 기본 형태
문자열.slice(잘라올 첫 위치값, 잘라올 마지막 위치값)
```

배열에서도 사용이 가능하다.

```js
var test = [1, 2, 3, 4, 5, 6];
test.slice(0, 3); // (3) [1, 2, 3]
```

## 📗 substring()

```js
// 기본 형태
문자열.slice(잘라올 첫 위치값, 잘라올 마지막 위치값)
```

사용법은 slice()와 동일함. 단 negative index(-)를 사용할 수 없음.

## 📘 substr()

```js
// 기본 형태
문자열.substr(잘라올 첫 위치값, 문자열의 길이)
```

위의 두 메소드와 매우 유사하나 두번째 파라미터가 문자열의 길이라는 점만 다르다.

인덱스를 지정하는것이 아닌 시작점부터 몇글짜를 가져올 것인지를 정하는 것.
