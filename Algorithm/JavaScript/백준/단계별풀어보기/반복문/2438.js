// 백준 : 2438 별 찍기 - 1
// 링크 : https://www.acmicpc.net/problem/
// 설명 :

const input = parseInt(
    require("fs").readFileSync("/dev/stdin").toString().trim().split(" "),
);

let answer = "";
for (let i = 1; i <= input; i++) {
    answer += "*";
    console.log(answer);
}
