import Vue from 'vue'
import App from '@/App'
import router from '@/router'
import store from '@/store'
import i18n from '@/i18n'
import api from '@/utils/api'
import axios from '@/utils/axios'
import helpers from '@/utils/helpers'
import '@/utils/element-ui'
import '@/assets/scss/fonts.scss'
import PageTitle from '@/components/global/PageTitle'

Vue.component('PageTitle', PageTitle)

Vue.config.productionTip = false
Vue.prototype.$api = api
Vue.prototype.$axios = axios
Vue.prototype.$helpers = helpers
Vue.prototype.$noop = _ => {}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  i18n,
  render: h => h(App)
})
