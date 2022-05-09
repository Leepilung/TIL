// 백준 : 1018 체스판 다시 칠하기
// 링크 : https://www.acmicpc.net/problem/1018
// 설명 : 체스판이 랜덤하게 주어지면 8*8 크기로 임의로 잘라쓸때 다시 색칠해야 하는 최소값 출력하는 문제

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");
const [n, ...arr] = input;

console.log(n);
console.log(arr);
[N, H] = n.split(" ").map(Number);
console.log(N, H);

let row = 0;
let col = 0;
let ans = 99999999999;
let toggle;
while (col + 8 <= N && row + 8 <= H) {
    if (arr[row][col] === "B") {
        toggle = true; // balck 은 true
    } else {
        // white 는 false
        toggle = false;
    }
    let count = 0;
    for (let i = col; i < col + 8; i++) {
        for (let j = row; j < row + 8; j++) {
            // console.log(i, j);
            if (
                (toggle === true && arr[i][j] === "W") ||
                (toggle === false && arr[i][j] === "B")
            ) {
                count++;
            }
            console.log(i, j, arr[i][j], "토글 값 : ", toggle, count);
            if (j === row + 7) {
                continue;
            }
            toggle = !toggle;
        }
    }
    if (ans > count) {
        ans = count;
    }
    console.log("-----------------------------");
    if (row + 8 !== N) {
        row++;
    } else col++;
}

console.log(ans);
//
