// 백준 2742 기찍 N
// 링크 : https://www.acmicpc.net/problem/2742
// 설명 : 찍기 반대로 하는 문제. 로직 거의 동일해서 간단.

const input = parseInt(
    require("fs").readFileSync("/dev/stdin").toString().trim(),
);

let answer = "";
for (let i = input; i > 0; i--) {
    answer += i + "\n";
}
console.log(answer);
