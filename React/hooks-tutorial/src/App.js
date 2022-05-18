import React, { useState } from "react";
import Counter from "./Components/useState/Counter";
import Info from "./Components/useState/Info";
import Average from "./Components/useState/Average";

const App = () => {
    const [visible, setVisible] = useState(false);

    return (
        <div>
            <Counter />
            <hr />
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
            <Average />
        </div>
    );
};

export default App;
