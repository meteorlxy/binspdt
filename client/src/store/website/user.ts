import {
  login,
  logout,
  register,
} from '@/api/website/auth'

import {
  getUserInfo,
} from '@/api/website/user'

import storage from '@/utils/storage'

export default {
  namespaced: true,

  state: {
    token: storage.getToken() || null,
    username: '',
    email: '',
    lastLogin: '',
    rememberMe: storage.getRememberMe() !== false,
    isLoading: false,
  },

  mutations: {
    setToken (state, token) {
      state.token = token
      if (token === null) {
        storage.removeToken()
      } else {
        storage.setToken(token, state.rememberMe)
      }
    },
    setUsername (state, username) {
      state.username = username
    },
    setEmail (state, email) {
      state.email = email
    },
    setLastLogin (state, lastLogin) {
      state.lastLogin = lastLogin
    },
    setIsLoading (state, isLoading) {
      state.isLoading = isLoading
    },
    setRememberMe (state, rememberMe) {
      state.rememberMe = rememberMe
      storage.setRememberMe(rememberMe)
    },
  },

  actions: {
    async login ({ commit }, { username, password }) {
      try {
        commit('setIsLoading', true)
        const res = await login({
          username,
          password,
        })
        commit('setUsername', res.data.username)
        commit('setToken', res.data.token)
        return res
      } catch (e) {
        throw e
      } finally {
        commit('setIsLoading', false)
      }
    },

    async logout ({ commit }) {
      try {
        commit('setIsLoading', true)
        const res = await logout()
        commit('setUsername', '')
        commit('setToken', null)
        commit('setEmail', '')
        commit('setLastLogin', '')
        return res
      } catch (e) {
        throw e
      } finally {
        commit('setIsLoading', false)
      }
    },

    async getUserInfo ({ state, commit }) {
      if (state.token === '') {
        return false
      }

      try {
        commit('setIsLoading', true)
        const res = await getUserInfo({
          token: state.token,
        })
        commit('setUsername', res.data.username)
        commit('setEmail', res.data.email)
        commit('setLastLogin', res.data.lastLogin)
        return res
      } catch (e) {
        throw e
      } finally {
        commit('setIsLoading', false)
      }
    },

    async register (ctx, form) {
      const res = await register(form)
      return res
    },
  },

  getters: {
    isLogined: state => Boolean(state.token),
  },
}
