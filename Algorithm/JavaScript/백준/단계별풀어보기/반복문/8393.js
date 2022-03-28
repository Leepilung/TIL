// 백준 8393 합
// 링크 : https://www.acmicpc.net/problem/8393
// 설명 : n이 주어졌을 때, 1부터 n까지의 합을 구하는 프로그램 작성

const input = parseInt(
    require("fs").readFileSync("/dev/stdin").toString().trim(),
);

let ans = 0;
for (let i = 1; i <= input; i++) {
    ans += i;
}
console.log(ans);
