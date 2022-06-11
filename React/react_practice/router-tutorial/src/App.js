import { Route, Routes, Link } from "react-router-dom";
import Home from "./Components/Home";
import About from "./Components/About";
import Profiles from "./Components/Profiles";
import NavigateSample from "./Components/NavigateSample";

// React-route v6 기준
// Route 사용할거라면 <Routes>로 감싸줘야함
// component -> element로 바꿔서 사용해야함.
// 컴포넌트도 <컴포넌트이름/>의 형태
// v5에서 배열로 여러개의 패스를 지정하는 방식은 사용할 수 없음. 그냥 그 이전에 사용하던 대로 여러개의 패스를 만들어야 함.

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
                <li>
                    <Link to="history">History 예제</Link>
                </li>
            </ul>
            <hr />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/profiles/*" element={<Profiles />} />
                <Route path="/history" element={<NavigateSample />} />
            </Routes>
        </>
    );
};

export default App;
