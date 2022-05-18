import React, { useState } from "react";
import Counter from "./Components/useState/Counter";
import Info from "./Components/useState/Info";
import Average from "./Components/useState/Average";

const App = () => {
    const [visible, setVisible] = useState(false);

    return (
        <div>
            <h1>Counter 컴포넌트</h1>
            <Counter />
            <hr />
            <h1> Info 컴포넌트</h1>
            <button
                onClick={() => {
                    setVisible(!visible);
                }}
            >
                {visible ? "숨기기" : "보이기"}
            </button>
            <br />
            {visible && <Info />}
            <hr />
            <h1> Average 컴포넌트</h1>
            <Average />
            <hr />
        </div>
    );
};

export default App;
