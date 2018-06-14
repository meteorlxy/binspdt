import axios from '@/utils/axios'
import api from '@/utils/api'
import i18n from '@/i18n'
import { Message, Notification } from 'element-ui'

const modulesModule = {
  namespaced: true,

  state: {
    modules: [],
    modules_details: new Map(),

    isLoading: false,
    modules_isLoading_details: [],
    modules_isDeleting: []
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
    async get ({ state, commit }, showMessage = true) {
      if (state.isLoading) {
        return false
      }

      try {
        commit('setLoading', true)
        const response = await axios.get(api.binary.modules.index())
        const modules = response.data.data
        commit('setModules', modules)
        if (showMessage) {
          Message.success(i18n.t('binary.modules.messages.get_success'))
        }
        return modules
      } catch (e) {
        if (showMessage) {
          Message.error(i18n.t('binary.modules.messages.get_error'))
        }
      } finally {
        commit('setLoading', false)
      }
    },

    async details ({ state, commit }, id) {
      if (state.modules_isLoading_details.includes(id)) {
        return false
      }

      if (state.modules_details.has(id)) {
        return state.modules_details.get(id)
      }

      try {
        commit('addLoadingDetails', id)
        const response = await axios.get(api.binary.modules.details(id))
        const details = response.data.data
        commit('setModuleDetails', { id, details })

        Notification.success({
          title: i18n.t('messages.title.success'),
          message: i18n.t('binary.modules.messages.details_success', {
            name: `[${id}]`
          })
        })
        return details
      } catch (e) {
        Notification.error({
          title: i18n.t('messages.title.error'),
          message: i18n.t('binary.modules.messages.details_error', {
            name: `[${id}]`
          })
        })
      } finally {
        commit('removeLoadingDetails', id)
      }
    },

    async delete ({ state, commit, dispatch }, id) {
      if (state.modules_isDeleting.includes(id)) {
        return false
      }

      try {
        commit('addDeleting', id)
        const response = await axios.delete(api.binary.modules.delete(id))
        Notification.success({
          title: i18n.t('messages.title.success'),
          message: i18n.t('binary.modules.messages.remove_success', {
            name: `[${id}]`
          })
        })
        dispatch('get', false)
        return response
      } catch (e) {
        Notification.error({
          title: i18n.t('messages.title.error'),
          message: i18n.t('binary.modules.messages.remove_error', {
            name: `[${id}]`
          })
        })
      } finally {
        commit('removeDeleting', id)
      }
    }
  }
}

export default modulesModule
