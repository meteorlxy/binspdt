
import axios, {
  AxiosError,
  AxiosResponse,
} from 'axios'

axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

// axios.interceptors.request.use(config => {
//   return config
// }, error => {
//   return Promise.reject(error)
// })

axios.interceptors.response.use((response: AxiosResponse) => {
  return response
}, (error: AxiosError & { response: AxiosResponse, notify: Object }) => {
  const response = error.response

  error.notify = {
    type: 'error',
    title: 'Error',
    text: `[${response.status} ${response.statusText}] ${response.data.msg}`,
  }

  return Promise.reject(error)
})

export default axios
