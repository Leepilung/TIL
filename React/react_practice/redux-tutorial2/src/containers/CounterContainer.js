import React from "react";
import { connect } from "react-redux";
import Counter from "../components/Counter";
// 액션 생성 함수 불러오기
import { increase, decrease } from "../modules/counter";

const CounterContainer = ({ number, increase, decrease }) => {
    return (
        <div>
            <Counter
                number={number}
                onIncrease={increase}
                onDecrease={decrease}
            />
        </div>
    );
};

// // state를 파라미터로 받아 오며, 이 값은 스토어가 지니고 있는 상태를 가리킨다.
// const mapStateToProps = (state) => ({
//     number: state.counter.number,
// });

// // store의 내장 함수 dispatch를 파라미터로 가져옴.
// const mapDispatchToProps = (dispatch) => ({
//     // 임시 함수
//     increase: () => {
//         console.log("increase");
//         dispatch(increase());
//     },
//     decrease: () => {
//         console.log("decrease");
//         dispatch(decrease());
//     },
// });

// connect 사용하면 리덕스랑 연동됨.
// connect 사용하려면 위의 2 함수 선언하고 사용해야함.익명함수로 써도됨
export default connect(
    (state) => ({
        number: state.counter.number,
    }),
    { increase, decrease },
)(CounterContainer);
