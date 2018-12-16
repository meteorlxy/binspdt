import axios from '@/libs/axios'

export const getAnalyses = ({
  token,
  page = 1,
  perPage = 25,
  orderBy = 'id',
  search,
}) => {
  return axios.request({
    url: '/api/v1/binary/analyses',
    method: 'get',
    params: {
      '_page': page,
      '_per_page': perPage,
      '_order_by': orderBy,
      '_search': search,
    },
    headers: {
      'Authorization': `Token ${token}`,
    },
  })
}

export const getAnalysesCount = ({
  token,
}) => {
  return axios.request({
    url: '/api/v1/binary/analyses/count',
    method: 'get',
    headers: {
      'Authorization': `Token ${token}`,
    },
  })
}

export const getAnalysis = ({
  token,
  id,
}) => {
  return axios.request({
    url: `/api/v1/binary/analyses/${id}`,
    method: 'get',
    headers: {
      'Authorization': `Token ${token}`,
    },
  })
}

export const deleteAnalysis = ({
  token,
  id,
}) => {
  return axios.request({
    url: `/api/v1/binary/analyses/${id}`,
    method: 'delete',
    headers: {
      'Authorization': `Token ${token}`,
    },
  })
}

export const deleteAnalyses = ({
  token,
  analyses,
}) => {
  return axios.request({
    url: `/api/v1/binary/analyses`,
    method: 'delete',
    headers: {
      'Authorization': `Token ${token}`,
    },
    data: {
      analyses,
    },
  })
}

export const postAnalysis = ({
  token,
  description,
  method,
  modules,
  params,
}) => {
  return axios.request({
    url: `/api/v1/binary/analyses`,
    method: 'post',
    headers: {
      'Authorization': `Token ${token}`,
    },
    data: {
      description,
      method,
      modules,
      params,
    },
  })
}

export default {
  getAnalyses,
  getAnalysesCount,
  getAnalysis,
  deleteAnalysis,
  deleteAnalyses,
  postAnalysis,
}
