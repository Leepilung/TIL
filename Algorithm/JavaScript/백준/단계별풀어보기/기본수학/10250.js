// 백준 : 10250 ACM 호텔
// 링크 : https://www.acmicpc.net/problem/10250
// 설명 : 호텔 층, 호수, 고객 수 주어지고 호텔이 머물 층수를 구하는 문제
// 점화식 파악이 제일 중요한 문제. 여기서 여러번 틀린 이유 -> 멍청한 실수(문자열 변환안함)

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

for (let i = 0; i < input[0]; i++) {
    [H, W, N] = [...input[i + 1].split(" ").map(Number)];
    let ans = "";
    let prev = Math.ceil(N % H);
    if (prev === 0) prev = H;
    let next = Math.ceil(N / H);
    if (next < 10) ans = prev + "0" + next;
    else ans += Number(String(prev) + String(next));

    console.log(ans);
}
