// 백준 : 2839 설탕 배달
// 링크 : https://www.acmicpc.net/problem/2839
// 설명 : 5봉투와 3봉투를 몇개 사용하는것이 최선인지 체크하는 문제.
// 테스트 케이스가 커질 경우를 생각하여 반복문 미사용 로직 구현 실패 (5봉투의 사용갯수 카운트해야하기떄문)
// while문으로 풀이.

let input = Number(require("fs").readFileSync("/dev/stdin").toString().trim());

let cnt = 0;

while (true) {
    if (input % 5 === 0) {
        console.log(input / 5 + cnt);
        break;
    }

    if (input < 0) {
        console.log(-1);
        break;
    }

    cnt += 1;
    input -= 3;
}

// ------------------------------------------------------------------
// 결론 : 결국 5 사용횟수 체크해야하는데 while문같이 반복 불가피함.
// if (input % 5 === 0) {
//     console.log(input / 5);
// }
// let ans = [0, 0];
// let five = Math.floor(input / 5);
// let three = input - 5 * five;

// // 5봉투가 사용 가능한지 아닌지 체크-> 사용 가능

// if (five === 0) {
//     // 한마디로 5이하 케이스
//     if (String(three / 3).length !== 1) {
//         console.log("케이스1");
//         console.log(-1);
//     } else {
//         console.log("케이스2");
//         console.log(three / 3);
//     }
// } else {
//     // 5이상의 케이스
//     tmp = input % 5;
//     if (String(tmp / 3).length !== 1) {
//         if (input % 3 === 0) {
//             console.log("케이스3-1");
//             console.log(input / 3);
//         } else {
//             console.log("케이스3-2");
//             console.log(-1);
//         }
//     } else {
//         console.log("케이스4");
//         console.log(five + three / 3);
//     }
// }

// N킬로그램 배달해야함. 설탕 -> 봉지에 담겨있음.
// 봉지에는 3킬로 5킬로 2종류. 최대한 적은봉지.
// 18 -> 3키로 6개보다 5키로 3개 + 3키로1개

// 단순히 5나누고 3나눈방식은 문제접근 실패
// 케이스 2개나눠보자 5봉지 사용가능 불가능 -> 배열로 카운트
// [-1,2]

// 6이상일 경우 -> 5봉투 사용가능한지 : 5로 나누고 나머지 3으로 나눠지면 사용가능. 아니면 불가능
// 5봉투 사용 불가 ->

// 로직 정리
// 5봉투 사용가능 체크 true -> 5사용 개수 카운트 -
//      false
