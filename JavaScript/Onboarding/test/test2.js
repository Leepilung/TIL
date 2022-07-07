var async = require("async");

console.time("t");
async.parallel(
    [
        function (callback) {
            setTimeout(() => {
                callback(null, "5 is done!");
            }, 5000);
        },
        function (callback) {
            setTimeout(() => {
                callback(null, "10 is done!");
            }, 10000);
        },
        function (callback) {
            setTimeout(() => {
                callback(null, "3 is done!");
            }, 3000);
        },
    ],
    function (err, results) {
        if (err) return console.error(err);
        console.log(results);
        console.timeEnd("t");
    },
);
