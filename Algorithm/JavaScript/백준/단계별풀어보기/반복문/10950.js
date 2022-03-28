// 백준 10950 A + B - 3
// 링크 : https://www.acmicpc.net/problem/10950
// 설명 : 간단하게 주어진 값을 더해서 출력하는 문제
// node.js를 IDE에서 I/O 처리하는게 파이썬과 너무다름.. 기초 문제를 더 풀어봄으로써 익숙해지는게 필요할듯.

const fs = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

for (let i = 1; i <= fs[0]; i++) {
    const n = fs[i].split(" ");
    console.log(Number(n[0]) + Number(n[1]));
}
