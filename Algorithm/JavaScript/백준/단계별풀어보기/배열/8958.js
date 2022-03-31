// 백준 : 8958 OX퀴즈
// 링크 : https://www.acmicpc.net/problem/8958
// 설명 :

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

let score = 0;

const TestScore = (a) => {
    if (a === 1) {
        score += 1;
        return score;
    } else {
        score += a;
        TestScore(a - 1);
    }
};

for (let i = 1; i < input.length; i++) {
    const a = input[i].split("X");
    score = 0;
    for (let j = 0; j < a.length; j++) {
        if (a[j] === "") continue;
        else {
            TestScore(a[j].length);
        }
    }
    console.log(score);
}
