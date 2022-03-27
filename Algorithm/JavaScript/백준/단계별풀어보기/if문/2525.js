// 백준 2525 오븐 시계
// 링크 : https://www.acmicpc.net/problem/2525
// 설명 : 첫째 줄에 현재 시간과 분, 다음줄에 걸리는 분이 주어짐. 최종적으로 걸리는 작업 시간을 출력하는 문제.

// 반례 찾는 실력을 좀더 갈고 닦아야할듯. 로직 구현보다 반례 찾는데 오래걸린듯

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(/\s+/)
    .map(Number);

const [A, B, C] = input;

if (B + C >= 60) {
    const addA = parseInt((B + C) / 60);
    if (A + addA >= 24) {
        console.log(Math.abs(24 - (A + addA)), (B + C) % 60);
    } else {
        console.log(A + addA, (B + C) % 60);
    }
} else console.log(A, B + C);
