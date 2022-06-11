// useNavigate 사용 방법
import { useNavigate } from "react-router-dom";

// v5에서의 history 객체는 라우트로 사용된 컴포넌트에게 match와 location등과 전달되는 props였다.
// v6에서는 useHistroy는 아예 사라졌고, 전부 useNavigate로 통합됨.

// block 사용하려면 block 커스텀훅 정의하고 불러와야됨.
import { usePrompt } from "../hooks/Blocker";

const NavigateSample = () => {
    const navigate = useNavigate();

    // 뒤로 가기
    const handleGoBack = () => {
        navigate(-1);
    };

    // 홈으로 이동
    const handleGoHome = () => {
        navigate("/");
    };

    // 블록 삽입 구문
    usePrompt("현재 페이지를 벗어나시겠습니까?", true);

    return (
        <div>
            <button onClick={handleGoBack}>뒤로</button>
            <button onClick={handleGoHome}>앞으로</button>
        </div>
    );
};

export default NavigateSample;
