// 백준 : 10757 큰 수 A + B
// 링크 : https://www.acmicpc.net/problem/10757
// 설명 : 매우 큰 정수가 주어졌을때 어떻게 처리해야할지를 해결해야하는 문제.
// 자바스크립트의 경우 2^62 이상의 숫자가 주어지면 지수 표현식으로 처리되는데
// BigInt사용하면 뒤에 n을 붙인채로 아무리 큰 숫자여도 그대로 표기해줌

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(" ")
    .map(BigInt);

console.log(String(BigInt(input[0] + input[1])).slice(0));
