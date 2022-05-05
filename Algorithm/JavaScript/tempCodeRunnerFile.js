
const getMiddle = (next) => {
    return next.map((v) => v + " ".repeat(v.length) + v);
};
