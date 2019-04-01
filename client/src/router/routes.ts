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

  // Login
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/Login.vue'),
    meta: {
      requiresAuth: false,
    },
  },

  // Register
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/Register.vue'),
    meta: {
      requiresAuth: false,
    },
  },

  // Dashboard
  {
    path: '/dashboard',
    component: () => import('@/views/dashboard/Dashboard.vue'),
    meta: {
      requiresAuth: true,
      linkText: 'Dashboard',
    },
    children: [
      // Dashboard Home
      {
        path: '',
        name: 'dashboard',
        component: () => import('@/views/dashboard/home/Home.vue'),
        meta: {
          title: 'Dashboard',
        },
      },

      // Dashboard Modules
      {
        path: 'modules',
        component: () => import('@/views/dashboard/modules/Modules.vue'),
        meta: {
          linkText: 'Modules',
        },
        children: [
          // Dashboard Modules Index
          {
            path: '',
            name: 'dashboard.modules',
            component: () => import('@/views/dashboard/modules/ModulesIndex.vue'),
            meta: {
              title: 'Modules',
            },
          },

          // Dashboard Modules Upload
          {
            path: 'upload',
            name: 'dashboard.modules.upload',
            component: () => import('@/views/dashboard/modules/ModulesUpload.vue'),
            meta: {
              title: 'Upload Modules',
              linkText: 'Upload',
            },
          },

          // Dashboard Modules Details
          {
            path: ':id',
            name: 'dashboard.modules.details',
            component: () => import('@/views/dashboard/modules/ModulesDetails.vue'),
            props: route => ({ id: Number(route.params.id) }),
            meta: {
              title: 'Modules Details',
              linkText: 'Details',
            },
          },
        ],
      },

      // Dashboard Analyses
      {
        path: 'analyses',
        component: () => import('@/views/dashboard/analyses/Analyses.vue'),
        meta: {
          linkText: 'Analyses',
        },
        children: [
          // Dashboard Analyses Index
          {
            path: '',
            name: 'dashboard.analyses',
            component: () => import('@/views/dashboard/analyses/AnalysesIndex.vue'),
            meta: {
              title: 'Analyses',
            },
          },

          // Dashboard Analyses New
          {
            path: 'new',
            name: 'dashboard.analyses.new',
            component: () => import('@/views/dashboard/analyses/AnalysesNew.vue'),
            meta: {
              title: 'New Analysis',
              linkText: 'New',
            },
          },

          // Dashboard Analyses Details
          {
            path: ':id',
            name: 'dashboard.analyses.details',
            component: () => import('@/views/dashboard/analyses/AnalysesDetails.vue'),
            props: route => ({ id: Number(route.params.id) }),
            meta: {
              title: 'Analysis Details',
              linkText: 'Details',
            },
          },
        ],
      },

      // Dashboard Wiki
      {
        path: 'wiki',
        component: () => import('@/views/dashboard/wiki/Wiki.vue'),
        meta: {
          linkText: 'Wiki',
        },
        children: [
          // Dashboard Wiki Index
          {
            path: '',
            name: 'dashboard.wiki',
            component: () => import('@/views/dashboard/wiki/WikiIndex.vue'),
            meta: {
              title: 'Wiki',
            },
          },

          // Dashboard Wiki API Set
          {
            path: 'api-set',
            name: 'dashboard.wiki.api-set',
            component: () => import('@/views/dashboard/wiki/WikiAPISet.vue'),
            meta: {
              title: 'API Set',
              linkText: 'API Set',
            },
          },

          // Dashboard Wiki K-Gram
          {
            path: 'k-gram',
            name: 'dashboard.wiki.k-gram',
            component: () => import('@/views/dashboard/wiki/WikiKGram.vue'),
            meta: {
              title: 'K-Gram',
              linkText: 'K-Gram',
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
