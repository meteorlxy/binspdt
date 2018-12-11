import { NotificationOptions } from 'vue-notification'

declare module 'vue/types/vue' {
  interface VueConstructor {
    notify (options: NotificationOptions | string): void;
  }
}
