// 백준 : 2108 통계학
// 링크 : https://www.acmicpc.net/problem/2108
// 설명 : 쉬운줄 알았으나 개골떄렸던 문제. 정렬문제라는데.. 최빈값이 제일 골치아팠음
// 최빈값의 경우 조건이 또 여러개면 두번째로 작은값 골라야되는 문제
// 코드 길이가 너무긴데 단순화는 복기하면서 다시금 해봐야할듯.
// https://www.acmicpc.net/source/31944332 숏코딩으로 복기한번 다시하기.

const [N, ...nums] = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .map(Number);

const sum = nums.reduce((acc, cur) => acc + cur, 0);
// 산술 평균
if (Math.round(sum / N) === -0) console.log(0);
else console.log(Math.round(sum / N));
// 중앙값
console.log(nums.sort((a, b) => a - b)[Math.floor(N / 2)]);

// 빈도값
nums.sort((a, b) => a - b);
const Chk = Array.from({ length: nums.length }, (v) => 0);
const check = {};
// console.log("정렬 후 nums : ", nums);
nums.forEach((x) => {
    // 빈도수 정렬
    check[x] = (check[x] || 0) + 1;
});
// console.log("정렬 전 체크 값 : ", check);

const result = [];
for (let key in check) {
    result.push([Number(key), check[key]]);
}
// console.log("배열에 담은 값들 : ", result);
result.sort((first, second) => {
    return first[0] - second[0];
});
// console.log("정렬 후 결과 값 : ", result);
const mode = result.sort((first, second) => {
    return second[1] - first[1];
})[0][1];
let index = [];
for (let i = 0; i < result.length; i++) {
    if (result[i][1] === mode) {
        index.push(i);
    }
}
if (index.length !== 1) {
    index.sort((a, b) => a - b);
    console.log(Number(result[index[1]][0]));
} else console.log(Number(result[index[0]][0]));

// 범위
if (nums.length === 1) console.log(0);
else console.log(Math.abs(nums[0] - nums[nums.length - 1]));
