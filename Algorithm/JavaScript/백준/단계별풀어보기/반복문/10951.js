// 백준 : 10951 A+B - 4
// 링크 : https://www.acmicpc.net/problem/10951
// 설명 : 그냥 더한거 출력하는 문제

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

for (let i = 0; i < input.length; i++) {
    const n = input[i].split(" ");
    console.log(Number(n[0]) + Number(n[1]));
}
