export default [
  {
    path: '/',
    name: 'home',
    redirect: {
      name: 'dashboard',
    },
    // component: () => import('@/views/Home'),
    // meta: {
    //   requiresAuth: false,
    // },
  },

  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/Login'),
    meta: {
      requiresAuth: false,
    },
  },

  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/Register'),
    meta: {
      requiresAuth: false,
    },
  },

  {
    path: '/dashboard',
    component: () => import('@/views/dashboard/Dashboard'),
    meta: {
      requiresAuth: true,
      linkText: 'Dashboard',
    },
    children: [
      {
        path: '',
        name: 'dashboard',
        component: () => import('@/views/dashboard/home/Home'),
        meta: {
          title: 'Dashboard',
        },
      },
      {
        path: 'modules',
        component: () => import('@/views/dashboard/modules/Modules'),
        meta: {
          linkText: 'Modules',
        },
        children: [
          {
            path: '',
            name: 'dashboard.modules',
            component: () => import('@/views/dashboard/modules/Index'),
            meta: {
              title: 'Modules',
            },
          },
          {
            path: 'modules',
            name: 'dashboard.modules.upload',
            component: () => import('@/views/dashboard/modules/Upload'),
            meta: {
              title: 'Modules',
              linkText: 'Upload',
            },
          },
        ],
      },
    ],
  },
  
  {
    path: '*',
    name: 'NotFound',
    component: () => import('@/views/NotFound'),
    meta: {
      requiresAuth: false,
    },
  },

//   {
//     path: '/binary',
//     name: 'binary',
//     redirect: {
//       name: 'binary.modules'
//     },
//     component: () => import('@/views/binary/Binary'),
//     children: [
//       {
//         path: '/binary/modules',
//         name: 'binary.modules',
//         component: () => import('@/views/binary/Modules')
//       },
//       {
//         path: '/binary/results',
//         name: 'binary.results',
//         component: () => import('@/views/binary/Results')
//       },
//       {
//         path: '/binary/analysis/api',
//         name: 'binary.analysis.api',
//         component: () => import('@/views/binary/Analysis/AnalysisApi')
//       }
//     ]
//   },
//   {
//     path: '/source',
//     name: 'source',
//     redirect: {
//       name: 'source.modules'
//     },
//     component: () => import('@/views/source/Source'),
//     children: [
//       {
//         path: '/source/modules',
//         name: 'source.modules',
//         component: () => import('@/views/source/Modules')
//       }
//     ]
//   }
]
