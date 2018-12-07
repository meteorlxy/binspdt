import {
  getModules,
} from '@/api/binary/modules'

export default {
  namespaced: true,

  state: {
    modules: [],
  },

  mutations: {
    setLoading (state, data) {
      state.isLoading = data
    },

    setModules (state, data) {
      state.modules = data
    },

    setModuleDetails (state, { id, details }) {
      state.modules_details.set(id, details)
    },

    addLoadingDetails (state, id) {
      state.modules_isLoading_details.push(id)
    },

    removeLoadingDetails (state, id) {
      state.modules_isLoading_details.splice(state.modules_isLoading_details.indexOf(id), 1)
    },

    addDeleting (state, id) {
      state.modules_isDeleting.push(id)
    },

    removeDeleting (state, id) {
      state.modules_isDeleting.splice(state.modules_isDeleting.indexOf(id), 1)
    }
  },

  actions: {
    async getModules ({ state, commit, rootState }, params = {}) {
      if (state.isLoading) {
        return false
      }

      try {
        commit('setLoading', true)
        const response = await getModules({
          ...params,
          token: rootState.token,
        })
        const modules = response.data.data
        commit('setModules', modules)
        return modules
      } catch (e) {

      } finally {
        commit('setLoading', false)
      }
    },

    async deleteModule ({ state, commit, rootState }) {
      if (state.isLoading) {
        return false
      }

      try {
        commit('setLoading', true)
        const response = await getModules({ token: rootState.token })
        return response
      } catch (e) {

      } finally {
        commit('setLoading', false)
      }
    },
  },
}
