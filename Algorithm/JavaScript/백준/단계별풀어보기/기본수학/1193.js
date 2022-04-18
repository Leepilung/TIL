// 백준 : 1193 분수찾기
// 링크 : https://www.acmicpc.net/problem/1193
// 설명 : 지그재그로 값이 바뀌는 분수를 출력하는 문제.
// 가장 중요한건 변화하는 로직을 어떻게 구현하느냐를 묻는 문제라고 파악.

const input = Number(require("fs").readFileSync("/dev/stdin"));

// 1/1 -> 1/2 -> 2/1 -> 1/3 -> 2/2 -> 3/1
// 1/4 ->

let a = 1;
let b = 2;
let max = 2;
let cnt = 2;
let toggle = 0; // 0 내리막 1 오르막
while (cnt < input) {
    if (b > 1 && toggle === 0) {
        b -= 1;
        a += 1;
        cnt += 1;
        continue;
    }
    if (a === max && b === 1 && toggle === 0) {
        max += 1;
        a = max;
        toggle = 1;
        cnt += 1;
        continue;
    }
    if (a > 1 && toggle === 1) {
        a -= 1;
        b += 1;
        cnt += 1;
        continue;
    }
    if (b === max && a === 1 && toggle === 1) {
        max += 1;
        b = max;
        toggle = 0;
        cnt += 1;
        continue;
    }
}
if (input === 1) {
    console.log(1 + "/" + 1);
} else console.log(a + "/" + b);
