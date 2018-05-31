const api = {
  binary: {
    modules: {
      index: () => '/api/binary/modules',
      import: version => `/api/binary/modules/v/${version}`,
      detail: id => `/api/binary/modules/${id}`,
      delete: id => `/api/binary/modules/${id}`,
      load: id => `/api/binary/modules/${id}/load`,
      analysis: {
        api: () => '/api/binary/analysis/api'
      }
    },
    analysis: {
      api: {
        index: () => '/api/binary/analysis/api'
      }
    }
  }
}
export default api
