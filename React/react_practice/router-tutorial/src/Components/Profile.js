import React from "react";
import { Link, useParams } from "react-router-dom";

const data = {
    test: {
        name: "김아무개",
        description: "리액트 테스트용",
    },
    test2: {
        name: "김테스트",
        description: "fldorxm xptmxmdyd2",
    },
};

const Profile = () => {
    const { username } = useParams();
    const profile = data[username];

    if (!profile) {
        return <div>존재하지 않는 사용자임</div>;
    }
    return (
        <div>
            <h3>
                {username}({profile.name})
            </h3>
            <p>{profile.description}</p>
        </div>
    );
};

export default Profile;
