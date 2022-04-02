// 백준 : 11654 아스키 코드
// 링크 : https://www.acmicpc.net/problem/11654
// 설명 : 문자열이 주어지면 아스키코드 값으로 바꾸는 문제
// charCodeAt -> 문자열 하나를 아스키코드 번호로 바꿔줌
// formCharCode -> 아스키코드 번호를 받아 문자열로 바꿔줌

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

console.log(input[0].charCodeAt(0));
