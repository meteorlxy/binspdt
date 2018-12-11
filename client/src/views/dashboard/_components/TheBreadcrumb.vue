<template>
  <VBreadcrumbs :items="items">
    <template
      slot="item"
      slot-scope="{ item: { text, href } }">
      <VBreadcrumbsItem
        :to="href"
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
    return this.$route.matched.filter(item => item.meta.linkText).map((item, index) => {
      return {
        text: item.meta.linkText,
        href: item.path,
      }
    })
  }
}
</script>
