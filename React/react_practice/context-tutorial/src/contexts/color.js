import { useState, createContext } from "react";

// 새로운 context 생성시 createContext 사용 (파라미터는 기본 상태값)
const ColorContext = createContext({
    state: { color: "black", subcolor: "red" },
    actions: {
        setColor: () => {},
        setSubColor: () => {},
    },
});

const ColorProvider = ({ children }) => {
    const [color, setColor] = useState("black");
    const [subcolor, setSubColor] = useState("red");

    const value = {
        state: { color, subcolor },
        actions: { setColor, setSubColor },
    };
    return (
        <ColorContext.Provider value={value}>{children}</ColorContext.Provider>
    );
};

// const ColorConsumer = ColorContext.Consumer와 같은 의미
const { Consumer: ColorConsumer } = ColorContext;

// ColorProvider와 ColorConsumer 내보내기 구문
export { ColorProvider, ColorConsumer };

export default ColorContext;
