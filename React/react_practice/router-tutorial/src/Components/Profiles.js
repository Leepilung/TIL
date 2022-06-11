import React from "react";
import { NavLink, Route, Routes } from "react-router-dom";
import Profile from "./Profile";

// 컴포넌트 대신 div 구문 출력도 가능
// NavLink 구문에서 activeStyle, activeClassName은 삭제되었다.
// 무엇을 선택했느냐에 따라 다르게 스타일 적용 가능

const Profiles = () => {
    return (
        <div>
            <h3>사용자 목록 : </h3>
            <ul>
                <li>
                    <NavLink
                        to="/profiles/test"
                        style={({ isActive }) => ({
                            color: isActive ? "black" : "gray",
                        })}
                    >
                        김아무개
                    </NavLink>
                </li>
                <li>
                    <NavLink
                        to="/profiles/test2"
                        style={({ isActive }) => ({
                            color: isActive ? "black" : "gray",
                        })}
                    >
                        김테스트
                    </NavLink>
                </li>
            </ul>

            <Routes>
                <Route path="/*" element={<div> 사용자를 선택하시오. </div>} />
                {/* JSX 서브 라우트 구문*/}
                <Route path=":username" element={<Profile />} />
            </Routes>
        </div>
    );
};

export default Profiles;
