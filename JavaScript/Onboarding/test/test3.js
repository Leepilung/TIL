function wakeUp() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("wake up");
        }, 100);
    });
}

function haveMeal() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("have meal");
        }, 100);
    });
}

function drinkSoju() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("drink soju");
        }, 100);
    });
}

function sleep() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("sleep");
        }, 100);
    });
}

wakeUp().then((data) => {
    console.log(data);

    haveMeal().then((data) => {
        console.log(data);

        drinkSoju().then((data) => {
            console.log(data);

            sleep().then((data) => {
                console.log(data);
            });
        });
    });
});
