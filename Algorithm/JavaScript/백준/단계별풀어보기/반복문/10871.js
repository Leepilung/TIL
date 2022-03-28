// 백준 : 10871 X보다 작은 수
// 링크 : https://www.acmicpc.net/problem/10871
// 설명 :

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

const X = input[0].split(" ")[1];
const b = input[1].split(" ");
let answer = "";

for (let i = 0; i < b.length; i++) {
    if (Number(b[i]) < Number(X)) {
        answer += b[i] + " ";
    }
}
console.log(answer);
