import axios from '@/libs/axios'

export const login = ({
  username,
  password,
}) => {
  return axios.request({
    url: '/api/v1/auth/login',
    method: 'post',
    data: {
      username,
      password,
    },
  })
}

export const logout = () => {
  return axios.request({
    url: '/api/v1/auth/logout',
    method: 'post',
  })
}

export const register = ({
  username,
  password,
  passwordConfirm,
  email,
}) => {
  return axios.request({
    url: '/api/v1/auth/register',
    method: 'post',
    data: {
      username,
      email,
      password,
      passwordConfirm,
    },
  })
}

export const resetPassword = ({
  username,
  email,
}) => {
  return axios.request({
    url: '/api/v1/auth/reset_password',
    method: 'post',
    data: {
      username,
      email,
    },
  })
}

export default {
  login,
  logout,
  register,
  resetPassword,
}
