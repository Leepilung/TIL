// 백준 : 7568 덩치
// 링크 : https://www.acmicpc.net/problem/7568
// 설명 :

const input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

// A = x,y / B = p,q
// x>p y>q일경우 A가 B보다 덩치가 더 크다.

N = Number(input.shift());
const bucket = [];

for (let i = 0; i < input.length; i++) {
    let count = 0;
    const h = input[i].split(" ").map(Number)[0];
    const w = input[i].split(" ").map(Number)[1];
    for (let j = 0; j < input.length; j++) {
        const new_h = input[j].split(" ").map(Number)[0];
        const new_w = input[j].split(" ").map(Number)[1];
        if (h < new_h && w < new_w) {
            count += 1;
        }
    }
    bucket.push(count + 1);
}

console.log(bucket.join(" "));

// 다음과 같이 묶어서 처리가능
const table = data.map((str) => str.split(" ").map(Number));
// [ [ 55, 185 ], [ 58, 183 ], [ 88, 186 ], [ 60, 175 ], [ 46, 155 ] ]
// for (let i of table) 하면 i[0],i[1]로 꺼낼 수 있음
