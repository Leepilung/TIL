// 백준 : 1712 손익분기점
// 링크 : https://www.acmicpc.net/problem/1712
// 설명 : 얼탱이 없는 문제
// Math.floor와 parseInt는 매우 큰차이가 있다.
// Math.floor와 parseInt는 둘다 양수에선 올림처리를 하나
// Math.floor는 음수에서도 내림처리를 하지만 parseInt는 버림처리를 하여 값이 아예 다르다.

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
