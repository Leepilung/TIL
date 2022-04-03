// 백준 : 2675 문자열 반복
// 링크 : https://www.acmicpc.net/problem/2675
// 설명 : 문자열을 횟수만큼 반복해서 곱하고 출력하는 문제
// 문자열 곱하기는 repeat() 사용하면 됨.

const S = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

console.log(S);
for (let i = 1; i < S.length; i++) {
    tmp = S[i].split(" ");
    let answer = "";
    for (let j = 0; j < tmp[1].length; j++) {
        tmp_string = tmp[1][j].repeat(tmp[0]);
        answer += tmp_string;
    }
    console.log(answer);
}
``;
