// 백준 2753 윤년
// 링크 : https://www.acmicpc.net/problem/2753
// 설명 : 연도가 주어졌을 때 윤년이면 1, 아니면 0 출력

const year = require("fs").readFileSync("/dev/stdin").toString().trim();

console.log(
    year % 4 === 0 ? (year % 100 !== 0 || year % 400 === 0 ? 1 : 0) : 0,
);