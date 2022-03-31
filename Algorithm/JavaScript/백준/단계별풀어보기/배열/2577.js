// 백준 : 2577 숫자의 개수
// 링크 : https://www.acmicpc.net/problem/2577
// 설명 :

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .map(Number);

const sum = String(input[0] * input[1] * input[2]);
let count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
for (let i = 0; i < sum.length; i++) {
    count[sum[i]] += 1;
}
for (let i = 0; i < count.length; i++) {
    console.log(count[i]);
}

// 훨씬 간결한 풀이
// 굳이 배열 만들 필요도 없음. 0~9까지의 사용빈도만 알면되니 각각의 값으로 split

const input2 = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .map(Number);

const sum2 = String(input2[0] * input2[1] * input2[2]);

for (let i = 0; i <= 9; i++) {
    console.log(sum2.split(i).length - 1);
}
