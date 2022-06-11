import React from "react";
import styled from "styled-components";
import { useLocation } from "react-router-dom";

// v5에서 location 객체에 있는 search 값에서 쿼리를 읽어올 수 있었고 qs라는 라이브러리를 사용해야 했음
// 그러나 v6기준으로 useLocation을 사용하면 손쉽게 가져올 수 있다.

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
