import Vue from 'vue'
import Router from 'vue-router'
import Component from 'vue-class-component'
import routes from './routes'
import setAuth from './auth'
import setNprogress from './nprogress'

Component.registerHooks([
  'beforeRouteEnter',
  'beforeRouteLeave',
  'beforeRouteUpdate',
])

Vue.use(Router)

const router = new Router({
  mode: 'history',

  base: process.env.BASE_URL,

  routes,
})

setAuth(router)
setNprogress(router)

export default router
