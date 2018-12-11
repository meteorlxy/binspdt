import axios from '@/libs/axios'
import { noop } from '@/utils/helpers'

export const getModules = ({
  token,
  page = 1,
  perPage = 25,
  orderBy = 'id',
  search,
}) => {
  return axios.request({
    url: '/api/v1/binary/modules',
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
    url: `/api/v1/binary/modules/${id}`,
    method: 'delete',
    headers: {
      'Authorization': `Token ${token}`,
    },
  })
}

export const deleteModules = ({
  token,
  modules,
}) => {
  return axios.request({
    url: `/api/v1/binary/modules`,
    method: 'delete',
    headers: {
      'Authorization': `Token ${token}`,
    },
    data: {
      modules,
    },
  })
}

export const postModules = ({
  token,
  files,
  version = '6.8',
  onUploadProgress = noop,
}) => {
  const formData = new FormData()
  for (const file of <Array<File>>files) {
    formData.append(`file`, file)
  }
  return axios.request({
    url: `/api/v1/binary/modules/v/${version}`,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data',
      'Authorization': `Token ${token}`,
    },
    data: formData,
    onUploadProgress,
  })
}

export default {
  getModules,
  getModulesCount,
  getModule,
  deleteModule,
  postModules,
}
