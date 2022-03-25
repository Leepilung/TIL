// 백준 14681 사분면
// 링크 : https://www.acmicpc.net/problem/14681
// 설명 :

const input = require("fs")
    .readFileSync(0)
    .toString()
    .trim()
    .split("\n")
    .map(Number);

const [x, y] = input;

console.log(
    x > 0 && y > 0
        ? 1
        : x < 0 && y > 0
        ? 2
        : x < 0 && y < 0
        ? 3
        : x > 0 && y < 0
        ? 4
        : "nothing",
);
