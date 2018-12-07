import axios from '@/libs/axios'

export const getUserInfo = ({
  token,
}) => {
  return axios.request({
    url: '/api/v1/user',
    method: 'get',
    headers: {
      'Authorization': `Token ${token}`,
    },
  })
}

export default {
  getUserInfo,
}
