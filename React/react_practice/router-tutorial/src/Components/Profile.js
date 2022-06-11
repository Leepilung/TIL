import React from "react";
import { useParams } from "react-router-dom";
import UseParamSample from "./UseParamSample";

const data = {
    test: {
        name: "김아무개",
        description: "리액트 테스트용",
    },
    test2: {
        name: "김테스트",
        description: "리액트 테스트용2",
    },
};

const Profile = () => {
    const { username } = useParams();
    console.log("유저 네임 : ", { username });
    const profile = data[username];
    console.log("프로필 데이터 :", profile);

    if (!profile) {
        return <div>존재하지 않는 사용자임</div>;
    }
    return (
        <div>
            <h3>
                {username}({profile.name})
            </h3>
            <p>{profile.description}</p>
            <UseParamSample />
        </div>
    );
};

export default Profile;
