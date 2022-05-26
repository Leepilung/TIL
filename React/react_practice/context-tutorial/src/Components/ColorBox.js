import React from "react";
import ColorContext from "../contexts/color";
import { ColorConsumer } from "../contexts/color";

const ColorBox = () => {
    return (
        <ColorConsumer>
            {(value) => (
                <>
                    <div
                        style={{
                            width: "64px",
                            height: "64px",
                            background: value.state.color,
                        }}
                    />60         
                </>
            )}
        </ColorConsumer>
    );
};

export default ColorBox;
