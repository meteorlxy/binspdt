import Vue from 'vue'
import ElementUI from 'element-ui'
import i18n from '@/i18n'
import 'element-ui/lib/theme-chalk/index.css'
// import '@/assets/scss/element-variables.scss'
// import 'element-ui/lib/theme-chalk/display.css'

Vue.use(ElementUI, { i18n: (key, value) => i18n.t(key, value) })
