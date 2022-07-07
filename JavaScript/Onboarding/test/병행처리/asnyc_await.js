// asybc && await

// 피드백 1 : 변수 명명시에 의미에 맞게 resolve -> results
// 피드백 2 : Array 다룰 때에는 Array 내장 함수로 다루는게 좋다.(map등이 더 좋다)
// map 활용 복습

const processJob = async (seconds) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // if (seconds === 10) return reject(new Error("에러발생에러발생에러발생")); // 에러 테스트 코드
      resolve(`${seconds} is done!`);
    }, seconds * 1000);
  });
};

(async () => {
  try {
    console.time('total time');
    // const results = await Promise.all([
    //     processJob(5),
    //     processJob(10),
    //     processJob(3),
    // ]);
    // results.map((result) => console.log(result));
    const tasks = [5, 10, 3].map((seconds) => processJob(seconds));
    const [result1, result2, result3] = await Promise.all(tasks); // 비구조화 할당 -> 개발 이유 : 받자마자 의미있는 변수가 되기 때문
    console.log(result2);
    console.timeEnd('total time');
  } catch (err) {
    console.error(err);
  }
})();
