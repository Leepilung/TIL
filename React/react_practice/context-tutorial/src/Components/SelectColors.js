import React from "react";
import { ColorConsumer } from "../contexts/color";

const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];

const SelectColors = () => {
    return (
        <div>
            <h1>색상을 선택하시오</h1>
            <ColorConsumer>
                {({ actions }) => (
                    <div style={{ display: "flex" }}>
                        {colors.map((color) => (
                            <div
                                key={color}
                                style={{
                                    background: color,
                                    width: "24px",
                                    height: "24px",
                                    cursor: "pointer",
                                }}
                                onClick={() => actions.setColor(color)}
                                onContextMenu={(e) => {
                                    // 마우스 우클릭 이벤트(onContextMenu)
                                    e.preventDefault();
                                    actions.setSubColor(color);
                                }}
                            />
                        ))}
                    </div>
                )}
            </ColorConsumer>
            <hr />
        </div>
    );
};

export default SelectColors;
