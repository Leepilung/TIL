// 백준 : 1157
// 링크 : https://www.acmicpc.net/problem/1157
// 설명 : 알파벳 대소문자로 주어진 경우 가장 많이 사용된 알파벳 대문자로 출력하는 문제

// filter 사용을 연습하는 문제(?)

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

const arr = Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 97));
const bucket = Array.from({ length: 26 }, (v) => 0);

for (let i = 0; i < input[0].length; i++) {
    const temp = input[0][i].toLowerCase();
    bucket[arr.indexOf(temp)] += 1;
}
const max = Math.max(...bucket);
const condition1 = bucket.filter((v) => v >= max);

if (condition1.length >= 2) {
    console.log("?");
} else console.log(String.fromCharCode(bucket.indexOf(max) + 97).toUpperCase());
