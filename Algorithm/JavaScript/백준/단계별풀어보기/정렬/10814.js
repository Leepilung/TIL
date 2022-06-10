// 백준 : 10814 나이순 정렬
// 링크 : https://www.acmicpc.net/problem/10814
// 설명 : 문제 설명은 아래와 같음. 정렬 알고리즘 sort()의 활용정도를 연습하기위한 문제.

// 입력 순서는 가입한대로.
// 회원들의 나이 오름차순. 나머진 먼저 가입한 사람이 앞에오는 순서대로 정렬되야 함.

const [N, ...arr] = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

bucket = [];
for (i of arr) {
    tmp = i.split(" ");
    // console.log(tmp);
    bucket.push([parseInt(tmp[0]), tmp[1]]);
}

// console.log(bucket);

bucket.sort((a, b) => {
    return a[0] - b[0];
});
let ans = "";
for (i of bucket) {
    ans += i[0] + " " + i[1] + "\n";
}

// console.log("-----------------");
console.log(ans);
