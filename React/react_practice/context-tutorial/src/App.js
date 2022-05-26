import React from "react";
import ColorBox from "./Components/ColorBox";
import ColorContext from "./contexts/color";
import { ColorProvider } from "./contexts/color";

// Provider 사용시 value 안쓰면 오류남.

const App = () => {
    return (
        <ColorProvider>
            <div>
                <ColorBox />
            </div>
        </ColorProvider>
    );
};

export default App;
