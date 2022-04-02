function solution(phone_number) {
    var answer = -1;
    const c = phone_number.split("+82-10");
    console.log(c);
    if (c.length === 2 && c[1].length == 10) {
        const c_1 = c[1].split("-");
        console.log(c_1);
        if (c_1.length === 3 && c[1].length === 4 && c[2].length === 4) {
            answer = 3;
            return answer;
        }
    }
    const b_m = phone_number.includes("-");
    const b_p = phone_number.includes("+");
    if (b_m === false && b_p === false && phone_number.length === 11) {
        answer = 2;
        return answer;
    }
    const a = phone_number.split("-");
    if (
        a.length === 3 &&
        a[0].length === 3 &&
        a[1].length === 4 &&
        a[2].length === 4
    ) {
        answer = 1;
        return answer;
    }
    return answer;
}

console.log(solution("+82-10-XXXX-XXXX"));
