// 백준 : 11021 A+B - 7
// 링크 : https://www.acmicpc.net/problem/11021
// 설명 : A+B를 출력하는 단순한 문제. 그러나 인덱싱 관리는 파이썬보다 단순하지 않았음.

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
    answer += "Case #" + i + ": " + num + "\n";
}

console.log(answer);
