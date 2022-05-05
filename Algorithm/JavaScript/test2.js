let N = +require("fs").readFileSync("/dev/stdin").toString().trim();

const getTop = (next) => {
    console.log(
        "탑 호출 : ",
        next.map((v) => v.repeat(3)),
    );
    return next.map((v) => v.repeat(3));
};

const getMiddle = (next) => {
    console.log(
        "미들 호출 : ",
        next.map((v) => v + " ".repeat(v.length) + v),
    );
    return next.map((v) => v + " ".repeat(v.length) + v);
};

const solve = (N) => {
    if (N === 1) {
        const b = ["*"];
        console.log("b : ", b);
        return b;
    }
    N /= 3;
    console.log("N :", N);
    const next = solve(N);
    const tmp = [...getTop(next), ...getMiddle(next), ...getTop(next)];
    console.log(tmp);
    return tmp;
};

console.log(solve(N));
console.log(solve(N).join("\n"));
