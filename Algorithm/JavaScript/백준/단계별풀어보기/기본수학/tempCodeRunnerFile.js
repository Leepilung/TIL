const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(" ")
    .map(Number);

[A, B, C] = input;
// A = 고정비용 , B = 가변비용, C = 노트북 가격
ans = A / (C - B);

if (ans <= 0) {
    console.log(-1);
} else console.log(ans + 1);