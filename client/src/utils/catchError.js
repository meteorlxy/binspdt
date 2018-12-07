import Vue from 'vue'

export function requestCatch(error, responseHandler = undefined, otherHandler = undefined) {
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
