import Vue from 'vue'
import VueI18n from 'vue-i18n'
import en from '@/i18n/lang/en'
import zh from '@/i18n/lang/zh'

Vue.use(VueI18n)

const i18n = new VueI18n({
  locale: 'en',
  fallbackLocale: 'zh',
  messages: {
    en,
    zh
  }
})

export default i18n
