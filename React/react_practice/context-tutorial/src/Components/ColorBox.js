import React, { useContext } from "react";
import ColorContext, { ColorConsumer } from "../contexts/color";

// useContext를 활용하여 코드 간결화 가능.

const ColorBox = () => {
    const { state } = useContext(ColorContext);

    return (
        <>
            <>
                <div
                    style={{
                        width: "64px",
                        height: "64px",
                        background: state.color,
                    }}
                />
                <div
                    style={{
                        width: "32px",
                        height: "32px",
                        background: state.subcolor,
                    }}
                />
            </>
        </>
    );
};

export default ColorBox;
