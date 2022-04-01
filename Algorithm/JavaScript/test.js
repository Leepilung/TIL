a = [1, 2, 3, 4, 5];

b = [1, 3, 5];

c = a.filter((x) => !b.includes(x));
// [ 2, 4 ] 출력
console.log(c);
