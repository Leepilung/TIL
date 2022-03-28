// 백준 2741 N 찍기
// 링크 : https://www.acmicpc.net/problem/2741
// 설명 : 특정 값을 받고 특정값까지 1부터 출력하는 문제
// 하나하나 console.log찍는게 생각보다 타임복잡도를 많이 잡아먹는 듯?

const input = parseInt(
    require("fs").readFileSync("/dev/stdin").toString().trim(),
);

let answer = "";
for (let i = 1; i <= input; i++) {
    answer += i + "\n";
}

console.log(answer);
