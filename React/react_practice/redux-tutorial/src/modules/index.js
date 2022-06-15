// 루트 리듀서(스토어 만들 때 리듀서 하나만 사용해야 하므로 하나로 합침)
import { combineReducers } from "@reduxjs/toolkit";
import counter from "./counter";
import todos from "./todos";

// 루트 리듀서 만들 때에는 combineReducers라는 내부 유틸 메소드 사용.
const rootReducer = combineReducers({
    counter,
    todos,
});

export default rootReducer;

// 나중에 import rootReducer from './modules'; 구문으로 삽입하면됨
