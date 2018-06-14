import Vue from 'vue'
import App from '@/App'
import router from '@/router'
import store from '@/store'
import i18n from '@/i18n'
import api from '@/utils/api'
import axios from '@/utils/axios'
import '@/utils/element-ui'
import '@/assets/scss/fonts.scss'

Vue.config.productionTip = false
Vue.prototype.$api = api
Vue.prototype.$axios = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  i18n,
  render: h => h(App)
})
