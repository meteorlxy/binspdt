import helpers from '@/utils/helpers'

declare module 'vue/types/vue' {
  interface Vue {
    $helpers: any
  }
}
