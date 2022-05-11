// 백준 : 2750 수 정렬하기
// 링크 : https://www.acmicpc.net/problem/2750
// 설명 : 오름차순 정렬하는 문제
// 단순 sort()로는 통과못함. 단순 sort로는 111이 2나 3과같은 수보다 앞에와서 그런듯.

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .map(Number);
const N = input.shift();
input.sort((a, b) => a - b);
for (i of input) console.log(i);
