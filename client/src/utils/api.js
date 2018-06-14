const api = {
  binary: {
    modules: {
      index: () => '/api/binary/modules',
      import: version => `/api/binary/modules/v/${version}`,
      details: id => `/api/binary/modules/${id}`,
      delete: id => `/api/binary/modules/${id}`,
      load: id => `/api/binary/modules/${id}/load`
    },
    analysis: {
      api: () => '/api/binary/analysis/api'
    },
    results: {
      index: () => '/api/binary/results',
      details: id => `/api/binary/results/${id}`
    }
  }
}
export default api
