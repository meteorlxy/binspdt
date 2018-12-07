<template>
  <ContentWrapper>
    <ContentHeader>
      <template>
        {{ pageTitle }}
      </template>

      <TheBreadcrumb slot="right" />
    </ContentHeader>

    <ContentMain>
      <TransitionFadeSlide>
        <slot />
      </TransitionFadeSlide>
    </ContentMain>
  </ContentWrapper>
</template>

<script>
import TheBreadcrumb from './TheBreadcrumb'
import TransitionFadeSlide from '@/components/TransitionFadeSlide'
import ContentHeader from '@/components/admin-lte/ContentHeader'
import ContentMain from '@/components/admin-lte/ContentMain'
import ContentWrapper from '@/components/admin-lte/ContentWrapper'

export default {
  name: 'TheMainContent',

  components: {
    TheBreadcrumb,
    TransitionFadeSlide,
    ContentHeader,
    ContentMain,
    ContentWrapper,
  },

  computed: {
    pageTitle () {
      return this.$route.meta.title || 'Dashboard'
    }
  },
}
</script>

