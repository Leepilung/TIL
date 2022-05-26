import React from "react";
import TodosContainer from "./components/Todos";
import CounterContainer from "./containers/CounterContainer";

const App = () => {
    return (
        <div>
            <CounterContainer />
            <hr />
            <TodosContainer />
        </div>
    );
};

export default App;
