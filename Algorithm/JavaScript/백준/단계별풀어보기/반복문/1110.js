// 백준 : 1110 더하기 사이클
// 링크 : https://www.acmicpc.net/problem/1110
// 설명 : 아우 지긋지긋한 문제. 로직 자체에서 주어진 10미만의 수 조건처리를 안해서 시간을 오래잡아먹힘.
// 언제나 문제에 주어진 조건사항을 자세히 읽고 분할로 정복하는 버릇을 들이자...

let N = require("fs").readFileSync("/dev/stdin").toString().trim();
const answer = N;
let num;
let count = 0;

while (true) {
    if (Number(N) < 10) {
        num = N;
    } else {
        num = String(Number(N[0]) + Number(N[1]));
    }
    N = N[N.length - 1] + num[num.length - 1];
    count += 1;
    if (parseInt(N) === parseInt(answer)) {
        console.log(count);
        break;
    }
}
