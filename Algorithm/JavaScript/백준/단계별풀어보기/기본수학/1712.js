// 백준 : 1712 손익분기점
// 링크 : https://www.acmicpc.net/problem/1712
// 설명 :

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(" ")
    .map(Number);

[A, B, C] = input;
// A = 고정비용 , B = 가변비용, C = 노트북 가격
if (C - B <= 0) {
    console.log(-1);
} else console.log(Math.floor(A / (C - B)) + 1);
