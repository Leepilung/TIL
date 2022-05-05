const test = (N) => {
    return ["*"];
};

console.log(test());

const getTop = (next) => {
    return next.map((v) => v.repeat(3));
};

const getMiddle = (next) => {
    return next.map((v) => v + " ".repeat(v.length) + v);
};

const ans = (N) => {
    return [...getTop(test()), ...getTop(["a"]), getMiddle(["a"])];
};
// ans =  [ '***', 'aaa', [ 'a a' ] ] 출력

const ans2 = (N) => {
    return [...getTop(test()), ...getTop(["a"]), ...getMiddle(["a"])];
};
// ans2 = [ '***', 'aaa', 'a a' ] 출력 

console.log(ans());
