import store from '../store'

export default function setAuth(router) {
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
