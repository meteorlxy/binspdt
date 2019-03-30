<template>
  <VBreadcrumbs :items="items">
    <template v-slot:item="{ item: { text, href, disabled } }">
      <VBreadcrumbsItem
        :to="href"
        :disabled="disabled"
        exact>
        {{ text }}
      </VBreadcrumbsItem>
    </template>
  </VBreadcrumbs>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class TheBreadcrumb extends Vue {
  get items () {
    const matchedRoutes = this.$route.matched.filter(item => item.meta.linkText)
    return matchedRoutes.map((item, index) => {
      return {
        text: item.meta.linkText,
        href: item.path,
        disabled: index === matchedRoutes.length - 1,
      }
    })
  }
}
</script>
