import { createStore } from 'vuex'

export default createStore({
  state: {
    user: {}
  },
  getters: {
  },
  mutations: {
    user (state, data) {
      state.user = data
    }
  },

  actions: {
  },
  modules: {
  }
})
