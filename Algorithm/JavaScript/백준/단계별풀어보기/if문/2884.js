// 백준 2884 알람 시계
// 링크 : https://www.acmicpc.net/problem/2884
// 설명 : 알람시계를 맞춘다는데 45분 일찍 울려야함. 00 00 -> 23 15 이런식

const [H, M] = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(" ")
    .map(Number);

if (M - 45 >= 0) {
    console.log(H, M - 45);
} else {
    if (H === 0) {
        console.log(23, 60 + (M - 45));
    }
    if (H !== 0) {
        console.log(H - 1, 60 + (M - 45));
    }
}
