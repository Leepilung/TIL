import React from "react";
import Counter from "./components/Counter";
import Todos from "./components/Todos";
import MockTest from "./components/MockTest";

const App = () => {
    return (
        <div>
            <Counter number={0} />
            <hr />
            {/* <Todos />
            <hr />
            <MockTest /> */}
        </div>
    );
};

export default App;
