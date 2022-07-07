// 병행처리 로직

// 피드백 1 : async 라이브러리의 parallel 활용해서 console.time 처리.
// 피드백 2 : 순차처리 부분도 같이 정리하기.
var async = require('async');

const tasks = [5, 10, 3];

const processJob = (seconds, callback) => {
  setTimeout(() => {
    // console.log(`${seconds} work is done!`);
    // if (seconds === 10) console.timeEnd("total time");
    callback(null, `${seconds} work is done!`);
  }, seconds * 1000);
};

// (() => {
//   console.time('total time');
//   for (task of tasks) {
//     processJob(task);
//   }
// })();

// async parallel 사용 케이스

var async = require('async');

console.time('total time2');
async.parallel(
  [
    (cb) => processJob(5, cb),
    (cb) => processJob(10, cb),
    (cb) => processJob(3, cb),
  ],
  function (err, results) {
    if (err) return console.error(err);
    console.log(results);
    console.timeEnd('total time2');
  },
);
