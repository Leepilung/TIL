// 백준 : 10872 팩토리얼
// 링크 : https://www.acmicpc.net/problem/10872
// 설명 : 재귀함수를 맨처음 구현해보라는 아주 간단한 문제로 파악

const input = Number(require("fs").readFileSync("/dev/stdin"));

const factorial = (n) => {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
};

console.log(factorial(input));
