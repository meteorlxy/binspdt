import nprogress from 'nprogress'
import Router from 'vue-router'
import 'nprogress/nprogress.css'

export default function setNprogress (router: Router) {
  nprogress.configure({ showSpinner: false })

  router.beforeEach((to, from, next) => {
    if (to.path !== from.path) {
      nprogress.start()
    }
    next()
  })

  router.afterEach(() => {
    nprogress.done()
  })
}
