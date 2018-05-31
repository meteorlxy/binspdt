import axios from '@/utils/axios'
import api from '@/utils/api'

const module = {
  namespaced: true,
  state: {
  },
  mutations: {
  },
  actions: {
    async api ({ commit }) {
      commit('loading', true)
      try {
        const response = await axios.get(api.binary.analysis.api.index())
        commit('set', response.data.data)
        return response
      } catch (e) {
        throw e
      } finally {
        commit('loading', false)
      }
    }
  }
}

export default module
