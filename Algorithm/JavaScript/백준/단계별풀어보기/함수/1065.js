// 백준 : 1065 한수
// 링크 : https://www.acmicpc.net/problem/1065
// 설명 :

const input = Number(
    require("fs").readFileSync("/dev/stdin").toString().trim().split("\n"),
);

if (input < 100) {
    console.log(input);
} else {
    let ans = 99;
    for (let i = 100; i <= input; i++) {
        const chk = Hansoo(i);
        if (chk) ans += 1;
    }

    console.log(ans);
}

function Hansoo(N) {
    if (
        Number(String(N)[1]) - Number(String(N)[0]) ===
        Number(String(N)[2]) - Number(String(N)[1])
    ) {
        return true;
    }
}
