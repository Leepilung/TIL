// 백준. 18108
// https://www.acmicpc.net/problem/18108
// 불교 어쩌구 저쩌구 문제 암튼 주어진 년도에서 543씩 빼면 되는 문제

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

const ans = parseInt(input);

console.log(ans - 543);
