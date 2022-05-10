// 백준 : 1018 체스판 다시 칠하기
// 링크 : https://www.acmicpc.net/problem/1018
// 설명 : 체스판이 랜덤하게 주어지면 8*8 크기로 임의로 잘라쓸때 다시 색칠해야 하는 최소값 출력하는 문제
// 시작이 검은색일때의 로직만 체크해서 8개 중 테스트 케이스 1개를 통과못함.
// 흰색일때 로직도 구현하여 체크하게 하여 통과.
// 로직 구현을 반만하여 시간을 굉장히 오래잡아먹혔던 문제
const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");
const [n, ...arr] = input;

[N, H] = n.split(" ").map(Number);
var ans = []; // 정답 담을 배열
let row = 0; // 행
let col = 0; // 열
let ans = 99999999999;
let toggle;
while (row + 8 <= N && col + 8 <= H) {
    toggle = true; // balck 은 true
    let count = 0;
    for (let i = row; i < row + 8; i++) {
        for (let j = col; j < col + 8; j++) {
            if (
                (toggle === true && arr[i][j] === "W") ||
                (toggle === false && arr[i][j] === "B")
            ) {
                count++;
            }
            if (j === col + 7) {
                continue;
            }
            toggle = !toggle;
        }
    }
    ans.push(count);

    toggle = false;
    let count2 = 0;
    for (let i = row; i < row + 8; i++) {
        for (let j = col; j < col + 8; j++) {
            if (
                (toggle === false && arr[i][j] === "B") ||
                (toggle === true && arr[i][j] === "W")
            ) {
                count2++;
            }
            if (j === col + 7) {
                continue;
            }
            toggle = !toggle;
        }
    }
    ans.push(count2);

    if (col + 8 !== H) {
        col++;
    } else {
        row++;
        col = 0;
    }
}

console.log(Math.min.apply(null, ans));
