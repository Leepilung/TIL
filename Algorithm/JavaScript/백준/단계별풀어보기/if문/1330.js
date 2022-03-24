// 백준 1330 두 수 비교하기
// 링크 : https://www.acmicpc.net/problem/1330
// 설명 : if문 사용해서 두 수 비교하는 문제

// 코드 풀이
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

const a = parseInt(input[0]);
const b = parseInt(input[1]);

if (a > b) {
    console.log(">");
}

if (a < b) {
    console.log("<");
}

if (a === b) {
    console.log("==");
}

// 리팩토링 답안

// if문을 굳이 3개로 분기할 필요가 없음. 3항연산자 이용하면 훨씬 깔끔
// 비구조화 할당으로 map함수 사용해서 Number로 바꾸면 굳이 변수 재할당 및 선언도 생략 가능
const [c, d] = require("fs").readFileSync("/dev/stdin").toString().split(" ").map(Number);

console.log(c > d ? ">" : c < d ? "<" : "==");
