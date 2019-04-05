import {
  getAnalyses,
  getAnalysis,
  deleteAnalysis,
  deleteAnalyses,
  postAnalysis,
} from '@/api/binary/analyses'

export default {
  namespaced: true,

  state: {
    analyses: {
      count: 0,
      page: 1,
      perPage: 25,
      data: [],
    },

    isLoading: false,

    methods: [
      {
        name: 'read_write_sequence',
        text: 'Read-Write Sequence - Sequence of Instructions Read-Write Operations',
        paramsComponent: () => import('@/views/dashboard/analyses/_components/read-write-sequence/ReadWriteSequenceParams.vue'),
        resultComponent: () => import('@/views/dashboard/analyses/_components/read-write-sequence/ReadWriteSequenceResult.vue'),
      },
      {
        name: 'api_set',
        text: 'API Set - Set of System API calls in Functions',
        paramsComponent: () => import('@/views/dashboard/analyses/_components/api-set/APISetParams.vue'),
        resultComponent: () => import('@/views/dashboard/analyses/_components/api-set/APISetResult.vue'),
      },
      {
        name: 'k_gram',
        text: 'K-Gram - Set of Subsequence of Instruction Mnemonic',
        paramsComponent: () => import('@/views/dashboard/analyses/_components/k-gram/KGramParams.vue'),
        resultComponent: () => import('@/views/dashboard/analyses/_components/k-gram/KGramResult.vue'),
      },
      {
        name: 'api_frequency',
        text: 'API Frequency - Vector of API calls Frequency',
        paramsComponent: () => import('@/views/dashboard/analyses/_components/api-frequency/APIFrequencyParams.vue'),
        resultComponent: () => import('@/views/dashboard/analyses/_components/api-frequency/APIFrequencyResult.vue'),
      },
    ],

    functionMatchAlgorithms: [
      {
        name: 'km',
        text: 'Kuhn-Munkres Algorithm',
      },
    ],
  },

  mutations: {
    setLoading (state, data) {
      state.isLoading = data
    },

    setAnalyses (state, data) {
      state.analyses = data
    },
  },

  actions: {
    async getAnalyses ({ state, commit, rootState }, params) {
      if (state.isLoading) {
        return false
      }

      try {
        commit('setLoading', true)
        const response = await getAnalyses({
          token: rootState.token,
          ...params,
        })
        const analyses = response.data
        commit('setAnalyses', analyses)
        return analyses
      } catch (e) {
        throw e
      } finally {
        commit('setLoading', false)
      }
    },

    async getAnalysis ({ rootState }, { id }) {
      try {
        const response = await getAnalysis({
          token: rootState.token,
          id,
        })
        return response
      } catch (e) {
        throw e
      }
    },

    async deleteAnalysis ({ state, commit, rootState }, { id }) {
      if (state.isLoading) {
        return false
      }

      try {
        commit('setLoading', true)
        const response = await deleteAnalysis({
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

    async deleteAnalyses ({ state, commit, rootState }, { analyses }) {
      if (state.isLoading) {
        return false
      }

      try {
        commit('setLoading', true)
        const response = await deleteAnalyses({
          token: rootState.token,
          analyses,
        })
        return response
      } catch (e) {
        throw e
      } finally {
        commit('setLoading', false)
      }
    },

    async postAnalysis ({ rootState }, {
      description,
      method,
      modules,
      params,
    }) {
      try {
        const response = await postAnalysis({
          token: rootState.token,
          description,
          method,
          modules,
          params,
        })
        return response
      } catch (e) {
        throw e
      }
    },
  },
}
