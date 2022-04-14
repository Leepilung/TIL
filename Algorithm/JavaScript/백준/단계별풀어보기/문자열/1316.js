// 백준 : 1316 그룹 단어 체커
// 링크 : https://www.acmicpc.net/problem/1316
// 설명 : 그룹 단어 체크 문제. 바로 통과했는데 코드가 너무 길다.
// 요구하는 연습 사항은 그냥 잘 구현했는가 말곤 딱히..?

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split(/\s+/);

const [n, ...arr] = input;

let answer = 0;
for (let i of arr) {
    let bucket = [];
    let toggle = 0;
    let prev;
    for (let j of i) {
        if (prev !== undefined) {
            if (prev === j) {
                continue;
            } else {
                if (bucket.includes(j) === false) {
                    bucket.push(j);
                    prev = j;
                    continue;
                } else {
                    toggle = 1;
                    break;
                }
            }
        } else {
            prev = j;
            bucket.push(j);
        }
    }
    if (toggle !== 1) {
        answer += 1;
    }
}

console.log(answer);
