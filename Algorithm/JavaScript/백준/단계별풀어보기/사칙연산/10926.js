// 10926 ??!
// https://www.acmicpc.net/problem/10926
// 그냥 입력되있는 값에 ??!만 붙이면 되는 문제
// 문제는 JS로 푸는 알고리즘에서 입력 부분이 상당히 까다로웠다는 점이 문제였다.
// readline과 readFileSync 2개가 존재하는데 스트링값으로 변환을 안하면 버퍼값에 담겨있기 때문에 
// 문자열로 변환은 필수. 문제는 개행문자가 포함되있기 때문에 trin()을 무조건 써줘야한다.. 안써서 틀림..


var fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
console.log(input[0] + "??!");
