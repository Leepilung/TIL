// 백준 : 11022 A+B - 8
// 링크 : https://www.acmicpc.net/problem/11022
// 설명 : 11021과 그냥 같은데 조금만 다른 문제

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

const T = Number(input[0]);
let answer = "";

for (let i = 1; i <= T; i++) {
    n = input[i].split(" ");
    num = parseInt(n[0]) + parseInt(n[1]);
    answer += "Case #" + i + ": " + n[0] + " + " + n[1] + " = " + num + "\n";
}

console.log(answer);
