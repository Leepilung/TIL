// 백준 : 11650 좌표 정렬하기
// 링크 : https://www.acmicpc.net/problem/11650
// 설명 : 주어진 값들을 이중 정렬 해야하는 문제
// 퀵정렬로 안풀리는 문제인 줄 알았으나 console.log를 여려번 찍어서 오래걸렸던 것.
// console.log 한번만 써보니 통과.

const [N, ...arr] = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

const bucket = [];
for (i of arr) {
    bucket.push(i.split(" ").map(Number));
}
bucket.sort((a, b) => {
    if (a[0] === b[0]) {
        return a[1] - b[1];
    } else return a[0] - b[0];
});

let ans = "";
for (i of bucket) {
    ans += i[0] + " " + i[1] + "\n";
}
console.log(ans);
