// 백준 : 2231 분해합
// 링크 : https://www.acmicpc.net/problem/2231
// 설명 : 생성자라는 조건에 부합하는 수를 찾게끔 무식하게 처음부터 탐색하여 풀이하는 방법

const input = require("fs").readFileSync("/dev/stdin").toString().trim();
let [new_N, toggle] = [0, 0];

for (let i = 0; i < 1000000; i++) {
    new_N = i;
    for (let j = 0; j < String(i).length; j++) {
        new_N += Number(String(i)[j]);
    }
    if (new_N === Number(input)) {
        console.log(i);
        toggle = 1;
        break;
    }
}

if (toggle === 0) console.log(0);
