// 백준 : 18870 좌표 압축
// 링크 : https://www.acmicpc.net/problem/18870
// 설명 :

const [N, ...arr] = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

let tmp = arr[0].split(" ").map(Number);

let ans = "";
for (let i = 0; i < N; i++) {
    let tmp2 = tmp.filter((x) => x < tmp[i]);
    if (i === N - 1) ans += tmp2.length;
    else ans += tmp2.length + " ";
}

console.log(ans);
