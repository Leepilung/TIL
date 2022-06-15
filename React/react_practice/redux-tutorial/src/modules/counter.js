// DUcks 패턴 -> 하나에 몰빵

// 1. 액션타입 정의 -> 대문자로, '모듈 이름/액션 이름'의 형태
const INCREASE = "counter/INCREASE";
const DECREASE = "counter/DECREASE";

// 2. 액션 생성 함수
export const increase = () => ({ type: INCREASE });
export const decrease = () => ({ type: DECREASE });

// 모듈 초기 상태 및 리듀서 함수

const initialState = {
    number: 0,  // 초기 상태
};

// 리듀서 함수
function counter(state = initialState, action) {
    switch (action.type) {
        case INCREASE:
            return {
                number: state.number + 1,
            };
        case DECREASE:
            return {
                number: state.number - 1,
            };
        default:
            return state;
    }
}

// export =>여러개 내보낼 수 있음 
// export default => 한개만 가능
export default counter; 
