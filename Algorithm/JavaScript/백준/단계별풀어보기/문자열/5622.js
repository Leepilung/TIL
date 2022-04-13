// 백준 : 5622 다이얼
// 링크 : https://www.acmicpc.net/problem/5622
// 설명 : 기가 막히게 삽질한 문제. 삽질한 과정을 놔뒀어야 하나 싶은 문제..

const text = require("fs").readFileSync("/dev/stdin").toString().trim();
var comb = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"];

let ans = 0;
for (let i of text) {
    ans += comb.findIndex((v) => v.includes(i)) + 3;
}

console.log(ans);

// 개인 피드백 사항 ( 너무 오래걸렸으므로 별도 기재)

// 초기 접근을 딕셔너리로 value값에 배열을 넣어두고 진행하였는데 굉장히 멍청한 접근이었다. 딕셔너리가 1:1로 대응하는 자료구조임을 생각해볼 때 value안에 배열을 넣어두는 것은 1:1 대응안에서 추가로 for문을 돌려야하는 매우 비효율적 구조였음.

// 초기 접근에만 상당한 시간을 날리고서야 위와 같은 사고를 끌어낼 수 있었고 그 다음 진행한 접근 풀이 방식은 2 - A, B, C라면 A : 2, B : 2, C : 2와 같이 모든 알파벳에 key value를 연결하는 방식. 이걸로도 풀렸으나 코드길이가 너무 길어 간단화하는 방향으로 선회

// 배열에 담아두고 포함되있는지를 체크하면 굳이 딕셔너리도 안쓰고 단순 배열로 가능할거라 생각. 그러나 in 연산자는 node.js에서 동작 안함 -> includes, findIndex 조합하면 원하는 결과 도출가능
