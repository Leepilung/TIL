// 백준 : 1181 단어 정렬
// 링크 : https://www.acmicpc.net/problem/1181
// 설명 : 문제의 설명은 아래 대충 적어놨고 의도는 다음과 같이 파악됨
// 자바스크립트의 sort()를 활용함에 있어 내부 function을 알고리즘 문제와 같이 문제가 요구하는 조건을 잘 구현해 낼 수 있는가
// 자바스크립트 sort() 특징으로 각문자를 비교하고 1이나 -1등으로 두수의 비교하는지 그 값으로 정렬하는지는 좀 더 공부해야할듯.

// 알파벳 소문자로 이뤄진 N개의 단어가 들어오면
// 1. 길이가 짧은 것부터
// 2. 길이가 같으면 사전 순으로 정렬하기.

let [N, ...arr] = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

let ans = "";

arr.sort((a, b) => {
    if (a.length > b.length) return 1; // 길이 순 정렬
    if (a.length === b.length) { // 길이 같으면 사전 순
        if (a > b) {
            return 1;
        } else return -1;
    } else return -1;
});

arr = new Set(arr);
for (i of arr) {
    ans += i + "\n";
}

console.log(ans);
