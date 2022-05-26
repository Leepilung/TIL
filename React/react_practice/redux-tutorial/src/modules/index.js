// 루트 리듀서(스토어 만들 때 리듀서 하나만 사용해야 하므로 합쳐주는 녀석)
import { combineReducers } from "@reduxjs/toolkit";
import counter from "./counter";
import todos from "./todos";

const rootReducer = combineReducers({
    counter,
    todos,
});

export default rootReducer;

// 나중에 import rootReducer from './modules'; 구문으로 삽입하면됨
