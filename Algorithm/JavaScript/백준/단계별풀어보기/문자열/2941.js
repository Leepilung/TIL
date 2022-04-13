// 백준 : 2941 크로아티아 알파벳
// 링크 : https://www.acmicpc.net/problem/2941
// 설명 : 문자열 치환을 연습하는 문제(?). replaceAll이 안된다고 알고 있었는데 MDN 기준 2022년 2월에 추가되있는걸 확인했다.

let input = require("fs").readFileSync("/dev/stdin").toString().trim();
const alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="];

for (i of alpha) {
    input = input.replaceAll(i, "#");
}
console.log(input.length);
