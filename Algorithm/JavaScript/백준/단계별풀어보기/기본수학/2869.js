// 백준 : 2869 달팽이는 올라가고 싶다
// 링크 : https://www.acmicpc.net/problem/2869
// 설명 : 달팽이는 V미터인 나무를 올라간다.
// 낮에는 A미터 상승, 밤에는 B 미터 하강. 정상일경우 미끄러지지 않음.
// A, B, V
// V >= (A-B)x + A
// V +1 - A / (A-B)
// V - A > (A-B)x
// V - A = (A-B)x

// V - A + 1
// 5  2 1 / 3 2 / 4 3 / 5

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(" ")
    .map(Number);

[A, B, V] = [...input];

console.log(Math.ceil((V - A) / (A - B)) + 1);

// 더 나은답
console.log((V - B) / (V - A));
