// 백준 2480 주사위 세개
// 링크 : https://www.acmicpc.net/problem/2480
// 설명 : 주사위 3개의 값을 확인하고 그에 맞게 값을 출력하는 문제

// 겹치는게 1개인 케이스는 뒤에 2개인 케이스와 나올 수 있었음. 바로 console.log 출력하는 방향에서답 갱신하는 방향으로 틀어서 풀이

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(" ")
    .map(Number);

for (let i = 0; i < input.length; i++) {
    let temp = input.filter((v) => v == input[i]);
    if (temp.length === 3) {
        var answer = 10000 + 1000 * temp[0];
        break;
    } else if (temp.length === 2) {
        var answer = 1000 + 100 * temp[0];
        break;
    } else if (temp.length === 1) {
        var answer = Math.max(...input) * 100;
    }
}

console.log(answer);

// -------------------- 좀더 짧고 간결한 풀이

const [a, b, c] = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(" ")
    .map(Number)
    .sort();

if (a === b && b === c) {
    console.log(10000 + a * 1000);
} else if (a === b || b === c) {
    console.log(1000 + b * 100);
} else {
    console.log(c * 100);
}
