// 백준 : 10818 최소, 최대
// 링크 : https://www.acmicpc.net/problem/10818
// 설명 :

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

const nums = input[1].split(" ").map(Number);

console.log(Math.min(...nums), Math.max(...nums));
