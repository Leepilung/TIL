import { Route, Routes, Link } from "react-router-dom";
import Home from "./Components/Home";
import About from "./Components/About";
import Profile from "./Components/Profile";

// Route 사용할거라면 <Routes>로 감싸줘야함
// component -> element로 바꿔서 사용해야함.
// 컴포넌트도 <컴포넌트이름/>의 형태

const App = () => {
    return (
        <>
            <ul>
                <li>
                    <Link to="/"> 홈</Link>
                </li>
                <li>
                    <Link to="/about">소개</Link>
                </li>
                <li>
                    <Link to="/profile/test">테스트 소개</Link>
                </li>
                <li>
                    <Link to="/profile/test2">인포인척 하는 소개</Link>
                </li>
            </ul>
            <hr />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/profile/:username" element={<Profile />} />
            </Routes>
        </>
    );
};

export default App;
