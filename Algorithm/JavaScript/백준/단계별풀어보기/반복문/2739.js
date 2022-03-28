// 백준 2739 구구단
// 링크 : https://www.acmicpc.net/problem/2739
// 설명 : for문 이용한 템플릿 문자열 연습 문제
// 템플릿 문자열 레퍼런스 사이트 : https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Text_formatting

const N = parseInt(require("fs").readFileSync("/dev/stdin").toString().trim());

for (let i = 1; i < 10; i++) {
    console.log(N + " * " + i + " = " + N * i);
}
