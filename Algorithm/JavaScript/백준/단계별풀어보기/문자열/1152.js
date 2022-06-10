// 백준 : 1152 단어의 개수
// 링크 : https://www.acmicpc.net/problem/1152
// 설명 : 아마도 문자열에 포함되있는 공백을 어떻게 처리하는지에 대해 연습하는 문제라고 생각
// JS로 이 문제를 접근할 때에는 trim으로 공백을 처리하고 시작하기 때문에 간단
// 그러나 입력이 단순히 공백인 케이스 처리를 제대로 하지 못해 시간이 다소 오래 걸린듯.

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

const a = input[0].split(" ");
console.log(input, a);
if (input[0] == "") {
    console.log(0);
} else console.log(a.length);
