// 순차처리 - 프로미스
// 피드백 1 : Promise 동작 원리에 대해 자세히 더 공부하기 + callback
// 피드백 2 :  프로미스 구조 변경하기(Complete)

const processJob = (seconds) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (seconds === 5) return reject(new Error('-->>>>????'));
      resolve(`${seconds} is done!`);
    }, seconds * 1000);
  });
};

(() => {
  console.time('total time');
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
      console.timeEnd('total time');
    })
    .catch((err) => {
      return console.error('에러발생', err);
    });
})();
