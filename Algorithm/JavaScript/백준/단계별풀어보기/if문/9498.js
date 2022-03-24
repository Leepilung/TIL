// 백준 9498 시험 성적
// 링크 : https://www.acmicpc.net/problem/9498
// 설명 : 각 점수에 따라 등급이 표기되도록 하는 문제

// 코드 풀이

const score = parseInt(
    require("fs").readFileSync("/dev/stdin").toString().trim(),
);

console.log(
    score >= 90
        ? "A"
        : score >= 80
        ? "B"
        : score >= 70
        ? "C"
        : score >= 60
        ? "D"
        : "F",
);
