// 백준 : 2775 부녀회장이 될테야
// 링크 : https://www.acmicpc.net/problem/2775
// 설명 :

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .map(Number);
const Testcase = Number(input.shift());

for (let re = 0; re < Testcase * 2; re += 2) {
    const k = input[re];
    const n = input[re + 1];

    const house = Array.from(Array(k + 1), () => Array(n + 1).fill(0));

    for (let i = 1; i <= n; i++) {
        house[0][i] = i;
    }

    for (let i = 1; i <= k; i++) {
        for (let j = 1; j <= n; j++) {
            house[i][j] = house[i - 1][j] + house[i][j - 1];
        }
    }
    console.log(house[k][n]);
}

// k와 n에 k층 n호에 몇명이 사는지 출력 아파트 0층부터 있음.
// 첫줄 테스트케이스 T
// 각 케이스마다 k, n 주어짐.

// 0층의 i호에는 i명이 살고있다. 2층의 1호에 사려면 2-1층의 1호부터 1호까지
// 0층 / 1  2  3  4  5  6  7  9
// 1층 / 1  3  6  10 15 21 28 37    -> 0층 i호 까지의 합
// 2층 / 1  4  10 20 35 56
// 3층 / 1  5  15 35 70 126

// 로직 자체가 1층의 특정 값을 구하려면 이전 층의 값을계산해서 더해야하는 방식.
