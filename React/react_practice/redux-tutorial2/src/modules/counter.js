import { createAction, handleActions } from "redux-actions";

// 액션 정의
const INCREASE = "counter/INCREASE";
const DECREASE = "counter/DECREASE";

// 액션 생성 함수
// export const increase = () => ({ type: INCREASE });
// export const decrease = () => ({ type: DECREASE });

//redux-actions 깔면 아래처럼 바뀜 {createAction} import 하면됨
export const increase = createAction(INCREASE);
export const decrease = createAction(DECREASE);

// 초기 상태
const initialState = {
    number: 0,
};

// 리듀서

// function counter(state = initialState, action) {
//     switch (action.type) {
//         case INCREASE:
//             return {
//                 number: state.number + 1,
//             };
//         case DECREASE:
//             return {
//                 number: state.number - 1,
//             };
//         default:
//             return state;
//     }
// }

// { handleActions} import 하면 아래처럼됨.
const counter = handleActions(
    {
        [INCREASE]: (state, action) => ({ number: state.number + 1 }),
        [DECREASE]: (state, action) => ({ number: state.number - 1 }),
    },
    initialState,
);

export default counter;
