import nprogress from 'nprogress'
import 'nprogress/nprogress.css'

export default function setNprogress(router) {
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
