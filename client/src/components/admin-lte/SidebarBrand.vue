<template>
  <RouterLink
    class="brand-link"
    :to="to">
    <slot />
  </RouterLink>
</template>

<script>
export default {
  name: 'SidebarBrand',

  props: {
    to: {
      type: [Object, String],
      required: false,
      default: '',
    },
  }
}
</script>

