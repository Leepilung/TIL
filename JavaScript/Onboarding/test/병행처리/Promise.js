// 병행처리 - 프로미스

var async = require("async");

const processJob = (seconds) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (seconds === 3) return reject(new Error("error")); // reject 호출 시 return 구문이 없음
            resolve(`${seconds} is done`);
        }, seconds * 1000);
    });
};

console.time("total time");
Promise.all([processJob(3), processJob(10), processJob(5)])
    .then((res) => {
        console.log(res);
        console.timeEnd("total time");
    })
    .catch((err) => {
        console.error(err);
    });
