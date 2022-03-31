// 백준 : 3052 나머지
// 링크 : https://www.acmicpc.net/problem/3052
// 설명 : 

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .map(Number);

const bucket = [];
for (let i = 0; i < input.length; i++) {
    if (bucket.indexOf(input[i] % 42) === -1) {
        bucket.push(input[i] % 42);
    }
}

console.log(bucket.length);
