import { Route, Routes, Link } from "react-router-dom";
import Home from "./Components/Home";
import About from "./Components/About";
import Profiles from "./Components/Profiles";

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
                    <Link to="/profiles">프로필</Link>
                </li>
            </ul>
            <hr />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/profiles/*" element={<Profiles />} />
            </Routes>
        </>
    );
};

export default App;
