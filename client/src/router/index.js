import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/Home')
    },
    {
      path: '/binary',
      name: 'binary',
      redirect: {
        name: 'binary.modules'
      },
      component: () => import('@/views/binary/Binary'),
      children: [
        {
          path: '/binary/modules',
          name: 'binary.modules',
          component: () => import('@/views/binary/Modules')
        },
        {
          path: '/binary/analysis/api',
          name: 'binary.analysis.api',
          component: () => import('@/views/binary/AnalysisApi')
        }
      ]
    },
    {
      path: '/source',
      name: 'source',
      redirect: {
        name: 'source.modules'
      },
      component: () => import('@/views/source/Source'),
      children: [
        {
          path: '/source/modules',
          name: 'source.modules',
          component: () => import('@/views/source/Modules')
        }
      ]
    }
  ]
})
