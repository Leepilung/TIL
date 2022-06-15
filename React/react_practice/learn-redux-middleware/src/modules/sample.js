import { act } from "react-dom/test-utils";
import { handleActions } from "redux-actions";
import * as api from "../lib/api";

// 액션 타입 선언,
// 한 요청당 케이스별로 3개(pending,fulfill, rejcet) 만들어야 함

const GET_POST = "sample/GET_POST";
const GET_POST_SUCESS = "sample/GET_POST_SUECESS";
const GET_POST_FAILURE = "sample/GET_POST_FAILURE";

const GET_USERS = "sample/GET_USERS";
const GET_USERS_SUCCESS = "sample/GET_USERS_SUCCESS";
const GET_USERS_FAILURE = "sample/GET_USERS_FAILURE";

// thunk 함수 생성 구문
// thunk 함수 내부에서 시작, 성공, 실패 각각의 경우에 따른 액션을 디스패치한다.

export const getPost = (id) => async (dispatch) => {
    dispatch({ type: GET_POST });
    try {
        const response = await api.getPost(id);
        dispatch({
            type: GET_POST_SUCESS,
            payload: response.data,
        });
    } catch (e) {
        dispatch({
            type: GET_POST_FAILURE,
            payload: e,
            error: true,
        });
        throw e; // 컴포넌트 단에서도 에러를 조회할 수 있게 해주는 구문
    }
};

export const getUsers = () => async (dispatch) => {
    dispatch({ type: GET_USERS });
    try {
        const response = await api.getUsers();
        dispatch({
            type: GET_POST_SUCESS,
            payload: response.data,
        });
    } catch (e) {
        dispatch({
            type: GET_POST_FAILURE,
            payload: e,
            error: true,
        });
        throw e;
    }
};

// 초기 상태 선언 구문
// 요청의 로딩중 상태는 loading이라는 객체에서 관리한다.

const initialState = {
    loading: {
        GET_POST: false,
        GET_USERS: false,
    },

    post: null,
    users: null,
};

const sample = handleActions(
    {
        [GET_POST]: (state) => ({
            ...state,
            loading: {
                ...state.loading,
                GET_POST: true,
            },
        }),
        [GET_POST_SUCESS]: (state, action) => ({
            ...state,
            loading: {
                ...state.loading,
                GET_POST: false,
            },
            post: action.payload,
        }),
        [GET_POST_FAILURE]: (state, action) => ({
            ...state,
            loading: {
                ...state.loading,
                GET_POST: false,
            },
        }),
        [GET_USERS]: (state, action) => ({
            ...state,
            laoding: {
                ...state.loading,
                GET_USERS: true,
            },
        }),
        [GET_USERS_SUCCESS]: (state, action) => ({
            ...state,
            laoding: {
                ...state.loading,
                GET_USERS: false,
            },
            users: action.payload,
        }),
        [GET_USERS_FAILURE]: (state, action) => ({
            ...state,
            laoding: {
                ...state.loading,
                GET_USERS: false,
            },
        }),
    },
    initialState,
);

export default sample;
