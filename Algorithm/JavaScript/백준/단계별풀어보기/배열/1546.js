// 백준 : 1546 평균
// 링크 : https://www.acmicpc.net/problem/1546
// 설명 : 멍청헀음. 가장 큰 점수도 당연히 100점으로 갱신해야함~

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

scores = input[1].split(" ").map(Number);
N = Number(input[0]);
M = Math.max(...scores);

let sum = 0;
for (let i = 0; i < scores.length; i++) {
    const a = (scores[i] / M) * 100;
    sum += a;
}
console.log(sum / N);
