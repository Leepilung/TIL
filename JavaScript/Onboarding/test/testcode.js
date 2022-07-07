// 병행처리 - 프로미스

const processJob = (seconds) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(`${seconds} is done!`);
        }, seconds * 1000);
    });
};

// 프로미스 구조 변경하기.
// processJob에서 then에서 콘솔로그 받는 부분은 맞으나 Promise 동작원리 파악.

(() => {
    console.time("total time");
    processJob(5)
        .then((res) => {
            console.log(res);
            return processJob(10);
        })
        .then((res) => {
            console.log(res);
            return processJob(3);
        })
        .then((res) => {
            console.log(res);
            console.timeEnd("total time");
        })
        .catch((err) => {
            console.log("에러발생", err);
        });
})();

// Promise 동작 원리에 대해 자세히 더 공부하기 + callback
