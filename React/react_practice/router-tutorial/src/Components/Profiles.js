import React from "react";
import { Link, Route, Routes } from "react-router-dom";
import Profile from "./Profile";

const Profiles = () => {
    return (
        <div>
            <h3>사용자 목록 : </h3>
            <ul>
                <li>
                    <Link to="/profiles/test">김아무개</Link>
                </li>
                <li>
                    <Link to="/profiles/test2">김테스트</Link>
                </li>
            </ul>

            <Routes>
                <Route path="/*" element={<div> 사용자를 선택하시오. </div>} />
                <Route path=":username" element={<Profile />} />
            </Routes>
        </div>
    );
};

export default Profiles;
