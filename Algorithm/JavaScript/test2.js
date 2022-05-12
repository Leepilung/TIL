// // let N = +require("fs").readFileSync("/dev/stdin").toString().trim();
// N = 9;
// const getTop = (next) => {
//     console.log(
//         "탑 호출 : ",
//         next.map((v) => v.repeat(3)),
//     );
//     return next.map((v) => v.repeat(3));
// };

// const getMiddle = (next) => {
//     console.log(
//         "미들 호출 : ",
//         next.map((v) => v + " ".repeat(v.length) + v),
//     );
//     return next.map((v) => v + " ".repeat(v.length) + v);
// };

// const solve = (N) => {
//     if (N === 1) {
//         const b = ["*"];
//         console.log("b : ", b);
//         return b;
//     }
//     N /= 3;
//     console.log("N :", N);
//     const next = solve(N);
//     const tmp = [...getTop(next), ...getMiddle(next), ...getTop(next)];
//     console.log(tmp);
//     return tmp;
// };

// console.log(solve(N));
// console.log(solve(N).join("\n"));

const arr = [12, 12, 12, 11];

const getMode = (arr) => {
    let mostFrequentCnt = 1;
    const mode = [];
    const _map = new Map();

    for (const item of arr) {
        const hasValue = _map.get(item);
        const cnt = hasValue === undefined ? 1 : hasValue + 1;
        _map.set(item, cnt);
    }

    for (const [key, value] of _map) {
        if (value > mostFrequentCnt) {
            mostFrequentCnt = value;
        }
    }

    if (mostFrequentCnt === 1) return null;
    for (const [key, value] of _map) {
        if (value === mostFrequentCnt) {
            mode.push(key);
        }
    }
    if (mostFrequentCnt === arr.length) return null;
    return mode;
};

if (getMode(arr)) {
    console.log("최빈값:", getMode(arr).join(","));
} else {
    console.log("없다");
}
