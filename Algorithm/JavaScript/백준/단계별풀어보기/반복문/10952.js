// 백준 : 10952 A + B -5
// 링크 : https://www.acmicpc.net/problem/10952
// 설명 :

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

let answer = "";
for (let i = 0; i < input.length - 1; i++) {
    const n = input[i].split(" ");
    console.log(Number(n[0]) + Number(n[1]));
}
