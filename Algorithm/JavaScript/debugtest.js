// const test = (N) => {
//     return ["*"];
// };

// console.log(test());

// const getTop = (next) => {
//     return next.map((v) => v.repeat(3));
// };

// const getMiddle = (next) => {
//     return next.map((v) => v + " ".repeat(v.length) + v);
// };

// const ans = (N) => {
//     return [...getTop(test()), ...getTop(["a"]), getMiddle(["a"])];
// };
// // ans =  [ '***', 'aaa', [ 'a a' ] ] 출력

// const ans2 = (N) => {
//     return [...getTop(test()), ...getTop(["a"]), ...getMiddle(["a"])];
// };
// // ans2 = [ '***', 'aaa', 'a a' ] 출력

// console.log(ans());
let input = require("fs")
    .readFileSync(__dirname + "/예제.txt")
    .toString()
    .split("\n");

const [n, ...arr] = input;

console.log(n);
console.log(arr);
[N, H] = n.split(" ").map(Number);
console.log(N, H);

let row = 0;
let col = 0;
let ans = 99999999999;
let toggle;
while (col + 8 <= N && row + 8 <= H) {
    if (arr[row][col] === "B") {
        toggle = true; // balck 은 true
    } else {
        // white 는 false
        toggle = false;
    }
    let count = 0;
    for (let i = col; i < col + 8; i++) {
        for (let j = row; j < row + 8; j++) {
            // console.log(i, j);
            if (
                (toggle === true && arr[i][j] === "W") ||
                (toggle === false && arr[i][j] === "B")
            ) {
                count++;
            }
            console.log(i, j, arr[i][j], "토글 값 : ", toggle, count);
            if (j === row + 7) {
                continue;
            }
            toggle = !toggle;
        }
    }
    if (ans > count) {
        ans = count;
    }
    console.log("-----------------------------");
    if (row + 8 !== N) {
        row++;
    } else {
        col++;
        row = 0;
    }
}

console.log(ans);
//
