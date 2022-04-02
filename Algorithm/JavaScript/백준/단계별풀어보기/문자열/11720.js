// 백준 : 11720 숫자의 합
// 링크 : https://www.acmicpc.net/problem/11720
// 설명 :

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

const A = input[1];
let answer = 0;
for (let i = 0; i < A.length; i++) {
    answer += Number(A[i]);
}

console.log(answer);
