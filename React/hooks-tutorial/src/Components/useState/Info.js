import React from "react";
import useInputs from "./useInput"; // 컴포넌트 import 구문

const Info = () => {
    const [state, onChange] = useInputs({ // reducer function 삭제 후 해당 useInput 가져다가 사용
        name: "",
        nickname: "",
    });
    const { name, nickname } = state;

    return (
        <div>
            <div>
                <input name="name" value={name} onChange={onChange} />
                <input name="nickname" value={nickname} onChange={onChange} />
            </div>
            <div>
                <div>
                    <b>이름:</b> {name}
                </div>
                <div>
                    <b>닉네임: </b>
                    {nickname}
                </div>
            </div>
        </div>
    );
};

export default Info;
