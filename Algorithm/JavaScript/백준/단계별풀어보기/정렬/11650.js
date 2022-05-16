// 백준 : 11650 좌표 정렬하기
// 링크 : https://www.acmicpc.net/problem/11650
// 설명 : 주어진 값들을 이중 정렬 해야하는 문제

const [N, ...arr] = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .split(" ");
console.log(arr);

const bucket = [];
for (i of arr) {
    bucket.push(i.split(" ").map(Number));
}

bucket.sort((a, b) => {
    if (a[0] === b[0]) {
        return a[1] - b[1];
    } else return a[0] - b[0];
});

for (i of bucket) {
    console.log(i[0] + " " + i[1]);
}
