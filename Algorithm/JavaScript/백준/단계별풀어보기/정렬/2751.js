// 백준 : 2751 수 정렬하기 2
// 링크 : https://www.acmicpc.net/problem/2750
// 설명 : 오름차순 정렬하는 문제. 시간제한 부여되있는 문제.
// for문 순회하면 늦어질것같아 join으로 묶어서 출력하니 통과
const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .map(Number);
const N = input.shift();
input.sort((a, b) => a - b);
console.log(input.join("\n"));
