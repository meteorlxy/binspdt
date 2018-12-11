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
  token,
  id,
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
  token,
  id,
}) => {
  return axios.request({
    url: `/api/v1/binary/modules/count/${id}`,
    method: 'delete',
    headers: {
      'Authorization': `Token ${token}`,
    },
  })
}

export const postModules = ({
  token,
  version = '6.8',
  files,
}) => {
  const formData = new FormData()
  for(const [index, file] of files.entries){
    formData.append(`files[${index}]`, file)
  }
  return axios.request({
    url: `/api/v1/binary/modules/v/${version}`,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data',
      'Authorization': `Token ${token}`,
    },
    data: formData,
  })
}

export default {
  getModules,
  getModulesCount,
  getModule,
  deleteModule,
  postModules,
}
