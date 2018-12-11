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
    component: () => import('@/views/Login.vue'),
    meta: {
      requiresAuth: false,
    },
  },

  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/Register.vue'),
    meta: {
      requiresAuth: false,
    },
  },

  {
    path: '/dashboard',
    component: () => import('@/views/dashboard/Dashboard.vue'),
    meta: {
      requiresAuth: true,
      linkText: 'Dashboard',
    },
    children: [
      {
        path: '',
        name: 'dashboard',
        component: () => import('@/views/dashboard/home/Home.vue'),
        meta: {
          title: 'Dashboard',
        },
      },
      {
        path: 'modules',
        component: () => import('@/views/dashboard/modules/Modules.vue'),
        meta: {
          linkText: 'Modules',
        },
        children: [
          {
            path: '',
            name: 'dashboard.modules',
            component: () => import('@/views/dashboard/modules/ModulesIndex.vue'),
            meta: {
              title: 'Modules',
            },
          },
          {
            path: 'upload',
            name: 'dashboard.modules.upload',
            component: () => import('@/views/dashboard/modules/ModulesUpload.vue'),
            meta: {
              title: 'Upload Modules',
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
    component: () => import('@/views/NotFound.vue'),
    meta: {
      requiresAuth: false,
    },
  },
]
