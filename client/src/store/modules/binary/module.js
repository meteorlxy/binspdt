import axios from '@/utils/axios'
import api from '@/utils/api'
import { Message } from 'element-ui'
import i18n from '@/i18n'

const module = {
  namespaced: true,
  state: {
    modules: [],
    loading: false
  },
  mutations: {
    loading (state, data) {
      state.loading = data
    },
    set (state, data) {
      state.modules = data
    }
  },
  actions: {
    async get ({ commit, state }, showMessage = true) {
      try {
        commit('loading', true)
        const response = await axios.get(api.binary.modules.index())
        commit('set', response.data.data)
        if (showMessage) {
          Message({
            message: i18n.t('binary.modules.messages.get_success'),
            type: 'success'
          })
        }
        return response
      } catch (e) {
        if (showMessage) {
          Message.error(i18n.t('binary.modules.messages.get_error', { msg: `${e.description}` }))
        }
      } finally {
        commit('loading', false)
      }
    },
    async delete ({ commit, dispatch }, id) {
      try {
        commit('loading', true)
        const response = await axios.delete(api.binary.modules.delete(id))
        Message({
          message: i18n.t('binary.modules.messages.remove_success'),
          type: 'success'
        })
        return response
      } catch (e) {
        Message.error(i18n.t('binary.modules.messages.remove_error', { msg: `${e.description}` }))
      } finally {
        commit('loading', false)
        dispatch('get', false)
      }
    }
  }
}

export default module
