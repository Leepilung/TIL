// 백준 : 4673 셀프 넘버
// 링크 : https://www.acmicpc.net/problem/4673
// 설명 :

let self_number = [];
let bucket = [...Array(100)].map((v, i) => i);

for (let i = 0; i < 100; i++) {
    const tmp = selfNumber(i);
    if (tmp in self_number) {
        continue;
    } else self_number.push(tmp);
}

function selfNumber(N) {
    const n_length = String(N).length;
    let new_N = N;
    for (let i = 0; i < n_length; i++) {
        new_N += Number(String(N)[i]);
    }
    return new_N;
}

const ans = bucket.filter((x) => !self_number.includes(x));
let answer = "";
for (let i = 0; i < ans.length; i++) {
    answer += ans[i] + "\n";
}

console.log(answer);
