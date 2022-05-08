// 백준 : 2798 블랙잭
// 링크 : https://www.acmicpc.net/problem/2798
// 설명 : 블랙잭의 로직을 구현하는 문제. 단순 무식하게 다순회해야함.
// label 활용해서 중간에 빠져나가서 속도 최적화 비스무리하게 시도해봤는데 유의미한듯?

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

[N, M] = input[0].split(" ").map(Number);
let Nums = input[1].split(" ").map(Number);
let ans = 0;

cond: for (let i = 0; i < N; i++) {
    for (let j = i + 1; j < N; j++) {
        for (let k = j + 1; k < N; k++) {
            let tmp = Nums[i] + Nums[j] + Nums[k];
            if (tmp === M) {
                console.log(M);
                break cond;
            }
            if (tmp <= M && tmp > ans) {
                ans = tmp;
            }
        }
    }
    if (i === N - 1) console.log(ans);
}
