import React from "react";
import Counter from "./Components/Counter";
import Say from "./Components/Say";
import EventPractice from "./Components/ClassEventPractice";
import FuncEventPractice from "./Components/FuncEventPractice";
import ValidationSample from "./Components/ref/ValidationSample";
const App = () => {
    return (
        <>
            <Counter />; 안녕하세요;
            <hr />
            <Say />
            <hr />
            <EventPractice />
            <hr />
            <FuncEventPractice />
            <hr />
            <ValidationSample />
        </>
    );
};

export default App;
