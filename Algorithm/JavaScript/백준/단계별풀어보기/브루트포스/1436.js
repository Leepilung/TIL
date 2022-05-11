// 백준 : 1436 영화감독 숌
// 링크 : https://www.acmicpc.net/problem/1436
// 설명 : 666이 들어가는 숫자중 가장 작은 수 출력
// 단순 브루트포스의 정석. 666이 들어간 수중 작은거 출력
// 너무 어렵게 생각하는게 문제였던 문제. 풀고보면 별거아닌데 도출이 오래걸림-> 단순하게 풀생각을 하자

const input = Number(require("fs").readFileSync("/dev/stdin"));

let cnt = 0;
for (let i = 665; i++; ) {
    if (String(i).indexOf("666") !== -1) cnt++;
    if (cnt === input) {
        console.log(i);
        break;
    }
}
