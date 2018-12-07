import Vue from 'vue'
import Router from 'vue-router'
import routes from './routes'
import setAuth from './auth'
import setNprogress from './nprogress'

Vue.use(Router)

const router =  new Router({
  mode: 'history',

  linkActiveClass: 'active',

  routes,
})

setAuth(router)
setNprogress(router)

export default router
