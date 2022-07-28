import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    token: [],
    user: null,
  },
  mutations: {
    // mutations의 주 역할은 state의 관리에 주안점을 두고 있다.
    // 유저 데이터를 로컬 스토리지와 VueX에 저장
    SET_USER_DATA(state, userData) {
      state.user = userData;
      localStorage.setItem('token', JSON.stringify(userData));
      // axios 헤더에 토큰 삽입
      console.log('유저 토큰 :', userData.token);
      axios.defaults.headers.common[
        'Authorization'
      ] = `Bearer ${userData.token}`;
    },
  },
  actions: {
    register({ commit }, credentials) {
      return axios
        .post('//localhost:3000/register', credentials)
        .then(({ data }) => {
          console.log('user data is', data);
          commit('SET_USER_DATA', data);
          // 여기까지 이상없이 넘어감
        });
    },
  },
  getters: {},
  modules: {},
});
