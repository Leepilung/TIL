import React from "react";
import ColorBox from "./Components/ColorBox";
import { ColorProvider } from "./contexts/color";
import SelectColors from "./Components/SelectColors";

// Provider 사용시 value 안쓰면 오류남.

const App = () => {
    return (
        <ColorProvider>
            <div>
                <SelectColors />
                <ColorBox />
            </div>
        </ColorProvider>
    );
};

export default App;
