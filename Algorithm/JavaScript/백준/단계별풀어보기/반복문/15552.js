// 백준 15552 빠른 A+B
// 링크 : https://www.acmicpc.net/problem/15552
// 설명 : 기존 A+B보다 빡빡한 조건의 문제인듯. console.log로 매번 조합해서 출력하는게 제법 시간복잡도를 잡아먹는것 같음.
// 하나의 문자열로 조합하고 한번에 출력하는게 더 빠른거같음.

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

let answer = "";

for (let i = 1; i <= input[0]; i++) {
    const n = input[i].split(" ");
    answer += parseInt(n[0]) + parseInt(n[1]) + "\n";
}

console.log(answer);
