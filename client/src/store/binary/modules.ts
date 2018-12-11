import {
  getModules,
  getModule,
  deleteModule,
  deleteModules,
  postModules,
} from '@/api/binary/modules'

export default {
  namespaced: true,

  state: {
    modules: {
      count: 0,
      page: 1,
      perPage: 25,
      data: [],
    },

    isLoading: false,
  },

  mutations: {
    setLoading (state, data) {
      state.isLoading = data
    },

    setModules (state, data) {
      state.modules = data
    },
  },

  actions: {
    async getModules ({ state, commit, rootState }, params) {
      if (state.isLoading) {
        return false
      }

      try {
        commit('setLoading', true)
        const response = await getModules({
          token: rootState.token,
          ...params,
        })
        const modules = response.data
        commit('setModules', modules)
        return modules
      } catch (e) {
        throw e
      } finally {
        commit('setLoading', false)
      }
    },

    async getModule ({ state, commit, rootState }, { id }) {
      if (state.isLoading) {
        return false
      }

      try {
        commit('setLoading', true)
        const response = await getModule({
          token: rootState.token,
          id,
        })
        return response
      } catch (e) {
        throw e
      } finally {
        commit('setLoading', false)
      }
    },

    async deleteModule ({ state, commit, rootState }, { id }) {
      if (state.isLoading) {
        return false
      }

      try {
        commit('setLoading', true)
        const response = await deleteModule({
          token: rootState.token,
          id,
        })
        return response
      } catch (e) {
        throw e
      } finally {
        commit('setLoading', false)
      }
    },

    async deleteModules ({ state, commit, rootState }, { modules }) {
      if (state.isLoading) {
        return false
      }

      try {
        commit('setLoading', true)
        const response = await deleteModules({
          token: rootState.token,
          modules,
        })
        return response
      } catch (e) {
        throw e
      } finally {
        commit('setLoading', false)
      }
    },

    async postModules ({ rootState }, {
      files,
      version,
      onUploadProgress,
    }) {
      try {
        const response = await postModules({
          token: rootState.token,
          files,
          version,
          onUploadProgress,
        })
        return response
      } catch (e) {
        throw e
      }
    },
  },
}