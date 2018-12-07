import api from '@/libs/api'
import i18n from '@/i18n'
import Vue from 'vue'

export default {
  namespaced: true,

  state: {
    results: [],
    count: 0,
    numPages: 1,
    page: 1,
    perPage: 20,

    isLoading: false,
    isLoadingDetails: false
  },

  mutations: {
    setResults (state, data) {
      state.results = data.data
      state.count = data.count
      state.numPages = data.num_pages
      state.page = data.page
      state.perPage = data.per_page
    },

    setLoading (state, data) {
      state.isLoading = data
    },

    setLoadingDetails (state, data) {
      state.isLoadingDetails = data
    }
  },

  actions: {
    async get ({ state, commit }, { page = 1, perPage = 20 }) {
      if (state.isLoading) {
        return false
      }

      try {
        commit('setLoading', true)
        const response = await axios.get(api.binary.results.index(), {
          params: {
            page: page,
            per_page: perPage
          }
        })
        const results = response.data.data
        commit('setResults', results)

        Vue.notify({
          type: 'success',
          title: i18n.t('messages.title.success'),
          text: i18n.t('binary.results.messages.get_success')
        })
        return results
      } catch (e) {
        Vue.notify({
          type: 'danger',
          title: i18n.t('messages.title.error'),
          text: i18n.t('binary.results.messages.get_error')
        })
      } finally {
        commit('setLoading', false)
      }
    },

    async details ({ state, commit }, id) {
      if (!state.results.find(result => result.id === id).finished_at) {
        return false
      }

      if (state.isLoadingDetails) {
        return false
      }

      try {
        commit('setLoadingDetails', id)
        const response = await axios.get(api.binary.results.details(id))
        const details = response.data.data

        Vue.notify({
          type: 'success',
          title: i18n.t('messages.title.success'),
          text: i18n.t('binary.results.messages.details_success', {
            name: `[${id}]`
          })
        })
        return details
      } catch (e) {
        Vue.notify({
          type: 'danger',
          title: i18n.t('messages.title.error'),
          text: i18n.t('binary.results.messages.details_error', {
            name: `[${id}]`
          })
        })
        throw e
      } finally {
        commit('setLoadingDetails', false)
      }
    }
  }
}
