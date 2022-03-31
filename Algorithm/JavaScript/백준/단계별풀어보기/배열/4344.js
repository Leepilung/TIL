// 백준 : 4344
// 링크 : https://www.acmicpc.net/problem/4344
// 설명 : 누산기(reduce 함수), filter 사용법, toFixed 사용법 숙지할 수 있던 문제

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

for (let i = 1; i < input.length; i++) {
    const Case = input[i].split(" ").map(Number);
    const N = Case[0];
    const Student = Case.slice([1]);

    const reducer = (acc, curr) => acc + curr;
    const Average = Student.reduce(reducer) / N;

    const StudentFilter = Student.filter((value) => value > Average);

    console.log(((StudentFilter.length / N) * 100).toFixed(3) + "%");
}
