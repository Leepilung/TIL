// 백준 : 10809 알파벳 찾기
// 링크 : https://www.acmicpc.net/problem/10809
// 설명 :

const text = require("fs").readFileSync("/dev/stdin").toString().trim();
const arr = Array.from({ length: 26 }, (v, i) => String.fromCharCode(i + 97));

const tmp = Array.from({ length: 26 }, (v) => -1);
for (let i = 0; i < text.length; i++) {
    const alpha = arr.indexOf(text[i]);
    if (tmp[alpha] !== -1) continue;
    tmp[alpha] = i;
}

console.log(tmp.join(" "));
console.log(
    "1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1",
);
