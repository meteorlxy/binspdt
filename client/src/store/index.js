import Vue from 'vue'
import Vuex from 'vuex'
import binaryModule from './modules/binary'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    binary: binaryModule
  }
})

export default store
