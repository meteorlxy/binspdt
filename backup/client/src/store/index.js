import Vue from 'vue'
import Vuex from 'vuex'
import binary from './modules/binary'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    binary
  }
})

export default store
