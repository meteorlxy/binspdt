import store from '@/store'
import Router from 'vue-router'

export default function setAuth (router: Router) {
  router.beforeEach((to, from, next) => {
    const isLogined = store.getters['website/user/isLogined']

    if (to.matched.some(record => record.meta.requiresAuth)) {
      if (isLogined) {
        next()
      } else {
        next({
          name: 'login',
          query: { redirect: to.fullPath },
        })
      }
    } else {
      if (isLogined) {
        if (to.name === 'login' || to.name === 'register') {
          next({ name: 'dashboard' })
        } else {
          next()
        }
      } else {
        next()
      }
    }
  })
}
