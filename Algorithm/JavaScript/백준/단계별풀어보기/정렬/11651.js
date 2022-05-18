// 백준 : 11651 좌표 정렬하기 2
// 링크 : https://www.acmicpc.net/problem/11651
// 설명 : 11650과 그냥 거의 유사한 문제. 규칙만 조금 다름

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
    if (a[1] === b[1]) {
        return a[0] - b[0];
    } else return a[1] - b[1];
});

let ans = "";
for (i of bucket) {
    ans += i[0] + " " + i[1] + "\n";
}
console.log(ans);
