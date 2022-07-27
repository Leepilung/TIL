// VueX 관련 실습 파일
import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      // store에서 사용하는  변수 선언하는 부분
      count: 0,
      cart: [
        { product_id: 1, product_name: '아이폰 거치대', category: 'A' },
        { product_id: 2, product_name: '아이폰', category: 'B' },
      ],
    };
  },
  // store안의 변수는 mutations에 정의된 함수가 아니면 변경이 불가능하다..
  mutations: {
    increment(state) {
      state.count += 1;
    },
  },
  getters: {
    cartCount: state => {
      return state.cart.length;
    },
    productACount: state => {
      return state.cart.filter(p => p.category == 'A').length;
    },
  },
});

// 스토어는 사용자 로그인 정보를 store에 담아서 로그인 여부를 체크하는 모든 컴포넌트에서는 computed로 유저정보가 있는지 체크해서 사용
// 장바구니 목록같은 경우도 store로 관리하면 편함
export default store;
