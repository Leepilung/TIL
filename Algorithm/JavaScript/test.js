a = [1, 2, 3, 4, 5];

const b = a.reduce(function (acc, cur, index) {
    return console.log(index);
});
console.log(b);
