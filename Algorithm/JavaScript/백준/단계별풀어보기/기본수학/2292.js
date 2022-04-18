// 백준 : 2292 벌집
// 링크 : https://www.acmicpc.net/problem/2292
// 설명 : 풀긴 풀었는데 되게 멍청하게 풀었던 문제.
// 로직을 파악해놓고 간단화하지 못한 문제 -> 원하나가 늘수록 6개씩 증감

// 통과한 풀이
const input = Number(
    require("fs").readFileSync("/dev/stdin").toString().trim(),
);

let a = 3;
let b = 0;
let sum = 1;
let ans = 1;
while (true) {
    if (input === 1) {
        console.log(1);
        break;
    }
    sum += a * 2 + b * 2;
    ans += 1;
    a += 2;
    b += 1;
    console.log(sum, ans);
    if (input <= sum) {
        console.log(ans);
        break;
    }
}


// 풀이 간단화

let c = 1;
let d = 1;
while ( d < input) {
    d += 6*c
    c++
}