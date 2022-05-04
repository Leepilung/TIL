// 백준 : 2447 별 찍기 - 10
// 링크 : https://www.acmicpc.net/problem/2447
// 설명 :

// 이중for문으로 순회해야할듯?(N*N구조)
// 각 부분을 빈칸으로할지 아닐지 체크하는 로직구현

const input = Number(require("fs").readFileSync("/dev/stdin"));
let ans = "";
const recur = (i, j) => {
    if (i % 3 === 1 && j % 3 === 1) {
        ans += " ";
    } else {
        if (Math.floor(i / 3) === 0 && Math.floor(j / 3) === 0) {
            ans += "*";
        } else {
            recur(Math.floor(i / 3), Math.floor(j / 3));
        }
    }
};

for (let i = 0; i < input; i++) {
    for (let j = 0; j < input; j++) {
        recur(i, j);
    }
    if (i !== input - 1) {
        ans += "\n";
    }
}
console.log(ans);
