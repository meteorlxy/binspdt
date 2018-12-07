import axios from '@/libs/axios'

export const getModules = ({
  token,
  page = 1,
  perPage = 25,
  orderBy = 'id',
}) => {
  return axios.request({
    url: '/api/v1/binary/modules',
    method: 'get',
    params: {
      'page': page,
      'per_page': perPage,
      'order_by': orderBy,
    },
    headers: {
      'Authorization': `Token ${token}`,
    },
  })
}

export const getModulesCount = ({
  token,
}) => {
  return axios.request({
    url: '/api/v1/binary/modules/count',
    method: 'get',
    headers: {
      'Authorization': `Token ${token}`,
    },
  })
}

export const getModule = ({
  id,
  token,
}) => {
  return axios.request({
    url: `/api/v1/binary/modules/count/${id}`,
    method: 'get',
    headers: {
      'Authorization': `Token ${token}`,
    },
  })
}

export const deleteModule = ({
  id,
  token,
}) => {
  return axios.request({
    url: `/api/v1/binary/modules/count/${id}`,
    method: 'delete',
    headers: {
      'Authorization': `Token ${token}`,
    },
  })
}

export default {
  getModules,
  getModulesCount,
  getModule,
  deleteModule,
}
