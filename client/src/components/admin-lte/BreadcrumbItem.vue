<template>
  <li class="breadcrumb-item">
    <RouterLink
      :is="component"
      :exact="exact"
      :tag="tag"
      :to="to">
      <slot />
    </RouterLink>
  </li>
</template>

<script>
export default {
  name: 'Breadcrumb',

  props: {
    exact: {
      type: Boolean,
      required: false,
      default: true,
    },

    tag: {
      type: String,
      required: false,
      default: 'a',
    },

    to: {
      type: [Object, String],
      required: false,
      default: '',
    },
  },

  computed: {
    component() {
      return this.to === '' ? 'span' : 'RouterLink'
    },
  },
}
</script>

<style lang="scss" scoped>
.breadcrumb-item :not(a) {
  cursor: default;
}
</style>
