total_sp = 121;

skills = [
    [1, 2],
    [1, 3],
    [3, 6],
    [3, 4],
    [3, 5],
];

let a = {};
let b = {};

for (let i = 0; i < skills.length; i++) {
    tmp = skills[i];
    if (isKeyExists(a, tmp[0]) === true) {
    } else {
        a[tmp[0]] = [];
        b[tmp[0]] = 0;
    }
    a[tmp[0]].push(tmp[1]);
}
const tmp_a = Object.keys(a);
console.log("tmp_a 값 : ", tmp_a);

let count = 0;
for (let i = tmp_a.length - 1; i >= 0; i--) {
    tmp = a[tmp_a[i]];
    for (let j = 0; j < tmp.length; j++) {
        if (isKeyExists(a, tmp[j]) === false) {
            if (isKeyExists(b, tmp[j]) === false) {
                b[tmp[j]] = 0;
            }
            b[tmp[j]] += 1;
            if (i === 0) {
                count += b[a[tmp_a[i]][j]];
            }
            delete a[tmp_a[i]][j];
        } else {
            b[tmp[j]] += a[tmp[j]].length;
            if (i === 0) {
                console.log("0일때의 값", b[a[tmp_a[i]][j]]);
                count += b[a[tmp_a[i]][j]];
            }
            delete a[tmp_a[i]][j];
        }
    }
    if (i === 0) {
        b[1] += count;
    }
}
const Value = Object.values(b).reduce((acc, curr) => acc + curr);
const skill_point = total_sp / Value;
console.log(skill_point);

const pre_answer = Object.values(b).map((v) => v * skill_point);
console.log(pre_answer);

function isKeyExists(obj, key) {
    return key in obj;
}
