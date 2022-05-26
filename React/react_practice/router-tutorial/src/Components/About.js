import React from "react";
import styled from "styled-components";
import { useLocation } from "react-router-dom";

const About = () => {
    const { search } = useLocation();
    console.log(search); // ?detail=true 쿼리값만 딱가져옴.

    const showDetail = search === "?detail=true";
    console.log(showDetail);

    return (
        <div>
            <h1>소개</h1>
            <p>예제 프로젝트</p>
            {showDetail && <p>detail 값이 true로 설정됨!</p>}
        </div>
    );
};

export default About;
