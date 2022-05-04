// 백준 : 10870 피보나치 수 5
// 링크 : https://www.acmicpc.net/problem/10870
// 설명 : 재귀함수를 응용하여 피보나치의 수를 구현해보라는 간단한 로직 구현 문제라고 판단.

const input = Number(require("fs").readFileSync("/dev/stdin"));

const fibo = (n) => {
    if (n === 0) {
        return 0;
    }
    if (n === 1) {
        return 1;
    }
    return fibo(n - 1) + fibo(n - 2);
};

console.log(fibo(input));
