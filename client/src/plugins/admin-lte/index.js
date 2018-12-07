import Vue from 'vue'
import init from './init'
import 'admin-lte/build/js/AdminLTE'
import '@/assets/scss/admin-lte.scss'

Vue.prototype.$adminlte = {
  init,
}
