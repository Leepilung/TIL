// 백준 : 11729 하노이의 탑 이동 순서
// 링크 : https://www.acmicpc.net/problem/11729
// 설명 : 하노이의 탑 이동 순서를 숫자로 표현해야 하는 문제

const input = Number(require("fs").readFileSync("/dev/stdin"));

const hanoi = (n, s, e) => {
    if (n === 1) {
        console.log(s, e);
        return;
    }

    hanoi(n - 1, s, 6 - s - e);
    console.log(s, e);
    hanoi(n - 1, 6 - s - e, e);
};

console.log(2 ** input - 1);
hanoi(input, 1, 3);
