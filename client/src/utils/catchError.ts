import Vue from 'vue'
import { AxiosError, AxiosResponse } from 'axios'

export function requestCatch (
  error: AxiosError & { notify: Object },
  responseHandler?: (response: AxiosResponse) => any,
  otherHandler?: Function) {
  const response = error.response

  if (response) {
    if (typeof responseHandler === 'function') {
      return responseHandler(response)
    } else if (error.notify) {
      return Vue.notify(error.notify)
    }
  }

  if (typeof otherHandler === 'function') {
    return otherHandler(error)
  } else {
    throw error
  }
}

export default {
  requestCatch,
}
