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
        ],
      },

      // Dashboard Analysis
      {
        path: 'analysis',
        component: () => import('@/views/dashboard/analysis/Analysis.vue'),
        meta: {
          linkText: 'Analysis',
        },
        children: [
          // Dashboard Analysis Index
          {
            path: '',
            name: 'dashboard.analysis',
            component: () => import('@/views/dashboard/analysis/AnalysisIndex.vue'),
            meta: {
              title: 'Analysis',
            },
          },

          // Dashboard Analysis Results
          {
            path: 'new',
            name: 'dashboard.analysis.new',
            component: () => import('@/views/dashboard/analysis/AnalysisNew.vue'),
            meta: {
              title: 'New Analysis',
              linkText: 'New',
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
