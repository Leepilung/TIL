// 순차처리 asybc && await

const processJob = async (seconds) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // if (seconds === 10) return reject(new Error("error다요!"));
            resolve(`${seconds} is done`);
        }, seconds * 1000);
    });
};

(async () => {
    try {
        console.time("total time");
        const five = await processJob(5);
        console.log(five);
        const ten = await processJob(10);
        console.log(ten);
        const three = await processJob(3);
        console.log(three);
        console.timeEnd("total time");
    } catch (err) {
        console.error(err);
    }
})();

// 에러처리 추가하기
