import React from "react";
import { useParams, useLocation, useNavigate } from "react-router-dom";

// withRouter는 v6에서 사라졌고 다음과 같은 구문들로 대체됨
// const useParamSample = ({ location, match, history }) => {

const UseParamSample = () => {
    const params = useParams();
    const location = useLocation();
    const navigate = useNavigate();
    console.log("파람 :", params);
    console.log("로케이션 :", location);

    return (
        <div>
            <h4>location</h4>
            <textarea value={JSON.stringify(location)} readOnly />

            <h4>params</h4>
            <textarea value={JSON.stringify(params)} readOnly />

            <button onClick={() => navigate("/")}> 홈으로 </button>
        </div>
    );
};

export default UseParamSample;
