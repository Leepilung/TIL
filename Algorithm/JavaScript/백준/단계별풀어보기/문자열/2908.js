// 백준 : 2908 상수
// 링크 : https://www.acmicpc.net/problem/2908
// 설명 : 문자열의 반전, 형변환을 통한 크기 비교등을 다루는 문제(?)라고 생각


const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

const reverse_string = (s) => {
    return s.split("").reverse().join("");
};

const numbers = input[0].split(" ");

const a = Number(reverse_string(numbers[0]));
const b = Number(reverse_string(numbers[1]));

if (a > b) {
    console.log(a);
} else console.log(b);
