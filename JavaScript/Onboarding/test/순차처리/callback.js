// 콜백 케이스
// 피드백 1 : console.log(`${seconds} work is done!`); 콘솔구문 매개변수로
// 피드백 2 : 첫번째 -> 에러 , 두번째 데이터 (결과)의 형태  -> 5에서 에러 발생시 10 작동안되게끔 에러처리
// error -> err
// qoute -> single qoute로 변경(prettier 설정도 유의하기)
// waterfall로 처리해보기

const processJob = (seconds, callback) => {
  setTimeout(() => {
    // 에러 테스트 케이스
    // if (seconds === 5) {
    //     throw new Error("에러다!!!!");
    // }
    callback(null, seconds);
  }, seconds * 1000);
};

(() => {
  console.time('total time');
  processJob(5, (err, seconds) => {
    if (err) return console.error(err);
    console.log(`${seconds} is done!`);
    processJob(10, (err, seconds) => {
      if (err) return console.error(err);
      console.log(`${seconds} is done!`);
      processJob(3, (err, seconds) => {
        if (err) return console.error(err);
        console.log(`${seconds} is done!`);
        console.timeEnd('total time');
      });
    });
  });
})();
