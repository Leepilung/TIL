import React, { useState } from "react";

const MockTest = () => {
    const [test, setTest] = useState(null);
    const [error, setError] = useState(null);

    const handleClick3 = () => {
        fetch("https://picsum.photos/v2/list")
            .then((res) => {
                return res.json();
            })
            .then((json) => {
                setTest(json);
            })
            .catch((err) => {
                setError(`Someting Wrong : ${err}`);
                console.log(error);
            });
    };
    return (
        <div>
            <button onClick={handleClick3}> test 데이터 가져오기</button>
            {test && (
                <ul>
                    {test.map((data) => (
                        <div key={data.id}>
                            작가 : {data.author}
                            url : {data.url}
                            <hr />
                        </div>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default MockTest;
