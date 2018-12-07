import Vue from 'vue'
import Vuex from 'vuex'
import binary from './binary'
import website from './website'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    binary,
    website,
  },
})

export default store
