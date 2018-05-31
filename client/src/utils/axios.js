import axios from 'axios'

const token = document.head.querySelector('meta[name="csrf_token"]')
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.headers.common['X-CSRFToken'] = token.content
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

// axios.interceptors.request.use(config => {
//   return config
// }, error => {
//   return Promise.reject(error)
// })

// axios.interceptors.response.use(response => {
//   return response
// }, error => {
//   return Promise.reject(error)
// })

export default axios
