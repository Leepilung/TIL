import React, { useState, Suspense } from "react";
import logo from "./logo.svg";
import "./App.css";

// React lazy 활용 구문
const SplitMe = React.lazy(() => import("./SplitMe"), {
    //loadable 사용 구문
});

function App() {
    const [visible, setVisible] = useState(false);

    const onClick = () => {
        // 아래와 같이 import를 함수로 사용하면 프로미스를 반환한다.
        // 이 함수를 통해 모듈을 불러올 때 모듈에서 default로 내보낸 것은 result.default로 참조해야 사용할 수 있다.
        // import("./notify").then((res) => res.default());

        setVisible(true);
    };

    // 마우스 오버 이벤트시 로딩 시작
    const onMouseOver = () => {
        SplitMe.preload();
    };

    // Suspense 사용하면 로딩중에 보여줄 수있는 구문 설정 가능

    // @lodable/component -> React.lazy와 유사하지만 Suspense 불필요함.
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p onClick={onClick} onMouseOver={onMouseOver}>
                    {" "}
                    Hello React!
                </p>
                <Suspense fallback={<div>loading...</div>}>
                    {visible && <SplitMe />}
                </Suspense>
            </header>
        </div>
    );
}

export default App;
