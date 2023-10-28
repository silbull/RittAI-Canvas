import { createStore } from 'vuex'

export default createStore({
  state: {
    geoGebraState: null,
  },
  mutations: {
    setGeoGebraState(state, payload) {
      state.geoGebraState = payload;
    },
  },
  actions: {
    saveGeoGebraState({ commit }, payload) {
      commit('setGeoGebraState', payload);
    },
  },
})