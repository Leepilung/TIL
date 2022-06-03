import { handleActions } from "redux-actions";
import * as api from "../lib/api";

// 액션 타입 선언,
// 한 요청당 케이스별로 3개(pending,fulfill, rejcet) 만들어야 함


const GET_POST = 'sample/GET_POST';
const GET_POST_SUCESS = 'sample/GET_POST_SUECESS'
const GET_POST_FAILURE = 'sample/GET_POST_FAILURE'