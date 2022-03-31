// 백준 : 2562 최댓값
// 링크 : https://www.acmicpc.net/problem/2562
// 설명 : 최댓값 어딨는지 찾고 최대값 인덱스 출력

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .map(Number);

console.log(Math.max(...input));
console.log(input.indexOf(Math.max(...input)) + 1);
