// 백준 : 1427 소트인사이드
// 링크 : https://www.acmicpc.net/problem/1427
// 설명 : 왜 실버5인지 모르겠음. 암튼 주어진 숫자를 내림차순 정렬하는 문제
// input에서 입력받을 때 좀더 깔끔하게 가능

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("")
    .map(Number);

// -- 생략 가능 --
// const bucket = [];

// for (i of input) {
//     bucket.push(Number(i));
// }

input.sort((a, b) => b - a);
console.log(input.join(""));
