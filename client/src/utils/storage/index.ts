import cookie from 'js-cookie'
import keys from './keys'

export const getRememberMe = () => cookie.get(keys.REMEMBER_ME) === 'true'
export const setRememberMe = rememberMe => cookie.set(keys.REMEMBER_ME, rememberMe)

export const getToken = () => {
  return sessionStorage.getItem(keys.TOKEN) || localStorage.getItem(keys.TOKEN)
}
export const setToken = (token, rememberMe = true) => {
  if (rememberMe) {
    localStorage.setItem(keys.TOKEN, token)
  } else {
    sessionStorage.setItem(keys.TOKEN, token)
  }
}
export const removeToken = () => {
  sessionStorage.removeItem(keys.TOKEN)
  localStorage.removeItem(keys.TOKEN)
}

export default {
  getRememberMe,
  setRememberMe,
  getToken,
  setToken,
  removeToken,
}
