// 백준 : 2439 별 찍기 -2
// 링크 : https://www.acmicpc.net/problem/2439
// 설명 :

const input = parseInt(
    require("fs").readFileSync("/dev/stdin").toString().trim().split(" "),
);

let answer = "";
for (let i = 1; i <= input; i++) {
    answer = " ".repeat(input - i) + "*".repeat(i);
    console.log(answer);
}
